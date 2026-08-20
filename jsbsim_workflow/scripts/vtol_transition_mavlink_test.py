#!/usr/bin/env python3
"""Proper VTOL transition test: arm, takeoff, reposition forward, then transition.

Unlike the earlier PX4-shell-only test (which called `commander transition`
while the vehicle held a static position with no forward destination), this
script gives the navigator an actual forward target via MAV_CMD_DO_REPOSITION
before/while transitioning, so the vehicle has a real reason to accelerate.
"""
import time
import sys
from pymavlink import mavutil

LOG = []
def log(msg):
    line = f"[{time.time():.1f}] {msg}"
    print(line, flush=True)
    LOG.append(line)

def wait_heartbeat(m, timeout=30):
    log("Waiting for heartbeat...")
    hb = m.wait_heartbeat(timeout=timeout)
    if hb is None:
        log("ERROR: no heartbeat received")
        sys.exit(1)
    log(f"Heartbeat OK: sys={m.target_system} comp={m.target_component}")

def send_cmd(m, command, p1=0, p2=0, p3=0, p4=0, p5=0, p6=0, p7=0):
    m.mav.command_long_send(
        m.target_system, m.target_component,
        command, 0, p1, p2, p3, p4, p5, p6, p7
    )

def wait_ack(m, command, timeout=5):
    t0 = time.time()
    while time.time() - t0 < timeout:
        msg = m.recv_match(type='COMMAND_ACK', blocking=True, timeout=timeout - (time.time() - t0))
        if msg is None:
            return None
        if msg.command == command:
            return msg.result
    return None

def get_global_pos(m, timeout=3):
    msg = m.recv_match(type='GLOBAL_POSITION_INT', blocking=True, timeout=timeout)
    return msg

def get_vtol_state(m, timeout=1):
    msg = m.recv_match(type='EXTENDED_SYS_STATE', blocking=True, timeout=timeout)
    return msg

def main():
    m = mavutil.mavlink_connection('udpout:127.0.0.1:18570', source_system=250)
    # send a heartbeat first so PX4 (server-mode mavlink) learns our address
    m.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
    wait_heartbeat(m)

    # ARM
    log("Arming...")
    send_cmd(m, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 1)
    r = wait_ack(m, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM)
    log(f"Arm ack: {r}")
    time.sleep(3)

    # Get current position as home reference
    pos = get_global_pos(m)
    if pos is None:
        log("ERROR: no GLOBAL_POSITION_INT")
        sys.exit(1)
    home_lat = pos.lat / 1e7
    home_lon = pos.lon / 1e7
    home_alt = pos.alt / 1000.0  # AMSL meters
    log(f"Home: lat={home_lat} lon={home_lon} alt_amsl={home_alt}")

    target_alt_rel = 30.0  # takeoff to 30m AGL (more room to accelerate than 20m default)

    # TAKEOFF
    log("Commanding takeoff...")
    send_cmd(m, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, float('nan'),
              home_lat, home_lon, home_alt + target_alt_rel)
    r = wait_ack(m, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF)
    log(f"Takeoff ack: {r}")

    # Wait for altitude
    log("Waiting to reach takeoff altitude...")
    t0 = time.time()
    while time.time() - t0 < 40:
        pos = get_global_pos(m, timeout=2)
        if pos is None:
            continue
        rel_alt = pos.relative_alt / 1000.0
        if int(time.time() - t0) % 3 == 0:
            log(f"  alt={rel_alt:.1f}m")
        if rel_alt >= target_alt_rel - 2.0:
            log(f"Reached altitude: {rel_alt:.1f}m")
            break
    else:
        log("WARNING: did not confirm altitude within 40s, continuing anyway")

    time.sleep(3)

    # REPOSITION forward (north ~600m) at same altitude, so the navigator has
    # a real destination and the vehicle will actually accelerate that way.
    forward_lat = home_lat + 0.0054  # ~600m north
    forward_lon = home_lon
    log(f"Sending DO_REPOSITION to lat={forward_lat} lon={forward_lon} alt_amsl={home_alt+target_alt_rel}")
    send_cmd(m, mavutil.mavlink.MAV_CMD_DO_REPOSITION, -1, 0, 0, float('nan'),
              forward_lat, forward_lon, home_alt + target_alt_rel)
    r = wait_ack(m, mavutil.mavlink.MAV_CMD_DO_REPOSITION)
    log(f"Reposition ack: {r}")

    # let it start moving forward for a bit before commanding transition
    log("Letting vehicle accelerate forward for 10s before transition...")
    t0 = time.time()
    while time.time() - t0 < 10:
        pos = get_global_pos(m, timeout=2)
        if pos is not None:
            gs = (pos.vx**2 + pos.vy**2)**0.5 / 100.0  # cm/s -> m/s
            log(f"  groundspeed={gs:.2f} m/s alt={pos.relative_alt/1000.0:.1f}m")

    # TRANSITION to FW (VEHICLE_VTOL_STATE_FW = 4)
    log("Commanding DO_VTOL_TRANSITION -> FW (4)...")
    send_cmd(m, mavutil.mavlink.MAV_CMD_DO_VTOL_TRANSITION, 4)
    r = wait_ack(m, mavutil.mavlink.MAV_CMD_DO_VTOL_TRANSITION)
    log(f"Transition ack: {r}")

    # Monitor for 40s
    log("Monitoring transition progress for 40s...")
    t0 = time.time()
    while time.time() - t0 < 40:
        vs = get_vtol_state(m, timeout=1)
        pos = get_global_pos(m, timeout=1)
        parts = []
        if vs is not None:
            parts.append(f"vtol_state={vs.vtol_state}")
        if pos is not None:
            gs = (pos.vx**2 + pos.vy**2)**0.5 / 100.0
            parts.append(f"gs={gs:.2f}m/s alt={pos.relative_alt/1000.0:.1f}m")
        if parts:
            log("  " + " ".join(parts))

    # LAND
    log("Commanding land...")
    send_cmd(m, mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, float('nan'), 0, 0, 0)
    r = wait_ack(m, mavutil.mavlink.MAV_CMD_NAV_LAND)
    log(f"Land ack: {r}")

    # Monitor until disarm or timeout
    t0 = time.time()
    while time.time() - t0 < 60:
        hb = m.recv_match(type='HEARTBEAT', blocking=True, timeout=5)
        if hb is None:
            continue
        armed = bool(hb.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED)
        pos = get_global_pos(m, timeout=1)
        alt = pos.relative_alt/1000.0 if pos else None
        log(f"  armed={armed} alt={alt}")
        if not armed:
            log("Disarmed - landing complete")
            break

    log("Test complete.")

if __name__ == '__main__':
    main()
