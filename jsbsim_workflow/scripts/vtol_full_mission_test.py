#!/usr/bin/env python3
"""Full normal-scenario VTOL mission test.

arm -> takeoff -> climb -> transition(FW) -> waypoint leg 1 -> waypoint leg 2
(turn) -> RTL -> back-transition(MC) -> land -> disarm.

Uses MAV_CMD_DO_REPOSITION for waypoint legs (simpler/more robust than full
mission upload protocol) plus explicit MAV_CMD_NAV_RETURN_TO_LAUNCH and
MAV_CMD_DO_VTOL_TRANSITION for the RTL/back-transition legs, so every phase
the user asked about is explicitly exercised regardless of what PX4's
automatic RTL logic would do on its own.
"""
import time
import sys
from pymavlink import mavutil

def log(msg):
    print(f"[{time.time():.1f}] {msg}", flush=True)

def send_cmd(m, command, p1=0, p2=0, p3=0, p4=0, p5=0, p6=0, p7=0):
    m.mav.command_long_send(m.target_system, m.target_component, command, 0,
                              p1, p2, p3, p4, p5, p6, p7)

def wait_ack(m, command, timeout=5):
    t0 = time.time()
    while time.time() - t0 < timeout:
        msg = m.recv_match(type='COMMAND_ACK', blocking=True, timeout=max(0.1, timeout - (time.time() - t0)))
        if msg is None:
            return None
        if msg.command == command:
            return msg.result
    return None

def get_global_pos(m, timeout=2):
    return m.recv_match(type='GLOBAL_POSITION_INT', blocking=True, timeout=timeout)

def get_vtol_state(m, timeout=1):
    return m.recv_match(type='EXTENDED_SYS_STATE', blocking=True, timeout=timeout)

def monitor(m, seconds, label):
    log(f"--- monitoring: {label} ({seconds}s) ---")
    t0 = time.time()
    last_state = None
    while time.time() - t0 < seconds:
        vs = get_vtol_state(m, timeout=1)
        pos = get_global_pos(m, timeout=1)
        parts = []
        if vs is not None:
            state_names = {0: 'UNDEF', 1: 'TRANS_TO_FW', 2: 'TRANS_TO_MC', 3: 'MC', 4: 'FW'}
            sname = state_names.get(vs.vtol_state, str(vs.vtol_state))
            if sname != last_state:
                log(f"  ** vtol_state changed -> {sname} **")
                last_state = sname
            parts.append(f"vtol={sname}")
        if pos is not None:
            gs = (pos.vx**2 + pos.vy**2)**0.5 / 100.0
            parts.append(f"gs={gs:.1f}m/s alt={pos.relative_alt/1000.0:.1f}m lat={pos.lat/1e7:.5f} lon={pos.lon/1e7:.5f}")
        if parts:
            log("  " + " ".join(parts))
    return last_state

def main():
    m = mavutil.mavlink_connection('udpout:127.0.0.1:18570', source_system=250)
    m.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
    log("Waiting for heartbeat...")
    m.wait_heartbeat(timeout=30)
    log(f"Connected: sys={m.target_system}")

    # ARM
    log("=== PHASE: ARM ===")
    send_cmd(m, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 1)
    log(f"Arm ack: {wait_ack(m, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM)}")
    time.sleep(3)

    pos = get_global_pos(m)
    home_lat, home_lon, home_alt = pos.lat / 1e7, pos.lon / 1e7, pos.alt / 1000.0
    log(f"Home: lat={home_lat} lon={home_lon} alt_amsl={home_alt}")
    cruise_alt_rel = 40.0
    cruise_alt_amsl = home_alt + cruise_alt_rel

    # TAKEOFF / CLIMB
    log("=== PHASE: TAKEOFF/CLIMB ===")
    send_cmd(m, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, float('nan'),
              home_lat, home_lon, cruise_alt_amsl)
    log(f"Takeoff ack: {wait_ack(m, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF)}")
    t0 = time.time()
    while time.time() - t0 < 45:
        pos = get_global_pos(m, timeout=2)
        if pos and pos.relative_alt / 1000.0 >= cruise_alt_rel - 3.0:
            log(f"Reached cruise altitude: {pos.relative_alt/1000.0:.1f}m")
            break
    time.sleep(3)

    # LEG 1 forward, build airspeed
    log("=== PHASE: TRANSITION (build airspeed via reposition) ===")
    wp1_lat, wp1_lon = home_lat + 0.0054, home_lon  # ~600m north
    send_cmd(m, mavutil.mavlink.MAV_CMD_DO_REPOSITION, -1, 0, 0, float('nan'), wp1_lat, wp1_lon, cruise_alt_amsl)
    log(f"Reposition(leg1) ack: {wait_ack(m, mavutil.mavlink.MAV_CMD_DO_REPOSITION)}")
    monitor(m, 10, "accelerating toward leg1")

    send_cmd(m, mavutil.mavlink.MAV_CMD_DO_VTOL_TRANSITION, 4)
    log(f"Transition->FW ack: {wait_ack(m, mavutil.mavlink.MAV_CMD_DO_VTOL_TRANSITION)}")
    monitor(m, 20, "transition to FW")

    # MISSION LEG 2 - turn to a new waypoint (east)
    log("=== PHASE: MISSION LEG 2 (turn/waypoint) ===")
    wp2_lat, wp2_lon = home_lat + 0.0054, home_lon + 0.0068  # ~600m north + ~600m east -> a turn
    send_cmd(m, mavutil.mavlink.MAV_CMD_DO_REPOSITION, -1, 0, 0, float('nan'), wp2_lat, wp2_lon, cruise_alt_amsl)
    log(f"Reposition(leg2/turn) ack: {wait_ack(m, mavutil.mavlink.MAV_CMD_DO_REPOSITION)}")
    monitor(m, 20, "flying leg2 (turn)")

    # MISSION LEG 3 - another waypoint/turn back toward home area
    log("=== PHASE: MISSION LEG 3 (second turn/waypoint) ===")
    wp3_lat, wp3_lon = home_lat + 0.001, home_lon + 0.001
    send_cmd(m, mavutil.mavlink.MAV_CMD_DO_REPOSITION, -1, 0, 0, float('nan'), wp3_lat, wp3_lon, cruise_alt_amsl)
    log(f"Reposition(leg3/turn) ack: {wait_ack(m, mavutil.mavlink.MAV_CMD_DO_REPOSITION)}")
    monitor(m, 20, "flying leg3 (turn)")

    # RETURN TO HOME
    log("=== PHASE: RETURN TO HOME ===")
    send_cmd(m, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH)
    log(f"RTL ack: {wait_ack(m, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH)}")
    last_state = monitor(m, 20, "RTL inbound")

    # BACK-TRANSITION (explicit, in case RTL logic hasn't already done it)
    log("=== PHASE: BACK-TRANSITION TO MC ===")
    send_cmd(m, mavutil.mavlink.MAV_CMD_DO_VTOL_TRANSITION, 3)
    log(f"Transition->MC ack: {wait_ack(m, mavutil.mavlink.MAV_CMD_DO_VTOL_TRANSITION)}")
    monitor(m, 15, "back-transition to MC")

    # LAND
    log("=== PHASE: LAND ===")
    send_cmd(m, mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, float('nan'), home_lat, home_lon, home_alt)
    log(f"Land ack: {wait_ack(m, mavutil.mavlink.MAV_CMD_NAV_LAND)}")

    log("=== PHASE: MONITOR UNTIL DISARM ===")
    t0 = time.time()
    while time.time() - t0 < 80:
        hb = m.recv_match(type='HEARTBEAT', blocking=True, timeout=5)
        if hb is None:
            continue
        armed = bool(hb.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED)
        pos = get_global_pos(m, timeout=1)
        alt = pos.relative_alt / 1000.0 if pos else None
        log(f"  armed={armed} alt={alt}")
        if not armed:
            log("DISARMED - mission complete")
            break

    log("=== TEST COMPLETE ===")

if __name__ == '__main__':
    main()
