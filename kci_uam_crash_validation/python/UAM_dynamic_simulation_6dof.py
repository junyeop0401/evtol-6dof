# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 10:08:27 2025
Revised: beta(sideslip)-dependent lateral-directional aerodynamics added,
hardcoded Cm_q placeholder replaced with a sourced value.

@author: junyeop
"""

import numpy as np
import pandas as pd  # 로그 저장용 pandas
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.interpolate import interp1d  # 공력 계수 보간용
import xml.etree.ElementTree as ET


class UAM_dynamic_simulation:
    def __init__(self, h, v_x, v_y, v_z, pitch_deg, yaw_deg, roll_deg):
        """UAM Simulator 초기화

        Parameters
        ----------
        h: float
            UAM initial height [m]
        v_x: float
            UAM initial x_velocity [m/s]
        v_y: float
            UAM initial y_velocity [m/s]
        v_z: float
            UAM initial z_velocity [m/s]
        pitch_deg: float
            UAM initial pitch deg [deg]
        yaw_deg: float
            UAM initial yaw deg [deg]
        roll deg: float
            UAM initial roll deg [deg]

        """
        self.h = h
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z
        self.pitch_deg = pitch_deg
        self.yaw_deg = yaw_deg
        self.roll_deg = roll_deg

        # 기본 파라미터
        self.setup_parameters()

        # Cessna 172 기본 파라미터
        self.init_aircraft_parameters()

    def setup_parameters(self):
        self.rho = 1.225        # 공기 밀도 (kg/m^3)
        self.g = 9.80665        # 중력 가속도 (m/s^2)
        # self.cd = 1.16          # fragment drag coefficient

        # simulation setup
        self.dt = 0.01          # 시간 간격 (s)
        self.t_max = 120        # 최대 시뮬레이션 시간 (s)
        self.steps = int(self.t_max / self.dt)

    def init_aircraft_parameters(self, xml_path=r"DB\aircraft\cessna172_config.xml",
                                  aero_xlsx_path="Cessna172_AeroCoefficients_Basic.xlsx"):
        """XML/xlsx에서 기체 파라미터 불러오기

        alpha 의존(세로축) 계수 CL/CD/Cm은 기존과 동일하게 엑셀 테이블 보간으로
        읽는다. beta(옆미끄럼각)와 각속도(p, r, q) 의존 계수(CYb/CYp/CYr,
        Clb/Clp/Clr, Cnb/Cnp/Cnr, Cmq)는 XML의 <aero_derivatives>에서 스칼라
        미계수로 읽는다 — 이 부분은 alpha 테이블이 아니라 "선형 안정미계수"
        방식이므로 run_simulation에서 beta*deriv + (b/2V)*rate*deriv 형태로
        직접 조합한다.
        """
        tree = ET.parse(xml_path)
        root = tree.getroot()

        mp = root.find("mass_properties")
        inertia = mp.find("inertia")

        self.m = float(mp.find("mass").text)
        self.S = float(mp.find("wing_area").text)
        self.c = float(mp.find("mean_chord").text)
        self.b = float(mp.find("wing_span").text)

        self.Ix = float(inertia.find("Ix").text)
        self.Iy = float(inertia.find("Iy").text)
        self.Iz = float(inertia.find("Iz").text)
        Ixz_elem = inertia.find("Ixz")
        self.Ixz = float(Ixz_elem.text) if Ixz_elem is not None else 0.0
        self.I = np.array([[self.Ix, 0, -self.Ixz], [0, self.Iy, 0], [-self.Ixz, 0, self.Iz]])  # 관성 텐서

        # === 세로축(longitudinal) alpha 테이블: 엑셀에서 CL/CD/Cm 보간 ===
        df = pd.read_excel(aero_xlsx_path, sheet_name="Sheet1")
        alpha = df["alpha [deg]"].values

        self.CL = interp1d(alpha, df["CL [-]"].values, kind="linear", bounds_error=False, fill_value="extrapolate")
        self.CD = interp1d(alpha, df["CD [-]"].values, kind="linear", bounds_error=False, fill_value="extrapolate")
        self.Cm = interp1d(alpha, df["Cm [-]"].values, kind="linear", bounds_error=False, fill_value="extrapolate")

        # === 가로/방향(lateral-directional) 선형 안정미계수: XML에서 스칼라로 읽음 ===
        deriv = root.find("aero_derivatives")
        if deriv is None:
            raise ValueError(
                "aircraft config XML에 <aero_derivatives> 블록이 없습니다. "
                "CYb/CYp/CYr/Clb/Clp/Clr/Cnb/Cnp/Cnr/Cmq를 채워야 beta 의존 "
                "가로/방향 동역학과 피치 감쇠가 반영됩니다."
            )
        self.CYb = float(deriv.find("CYb").text)
        self.CYp = float(deriv.find("CYp").text)
        self.CYr = float(deriv.find("CYr").text)
        self.Clb = float(deriv.find("Clb").text)
        self.Clp = float(deriv.find("Clp").text)
        self.Clr = float(deriv.find("Clr").text)
        self.Cnb = float(deriv.find("Cnb").text)
        self.Cnp = float(deriv.find("Cnp").text)
        self.Cnr = float(deriv.find("Cnr").text)
        self.Cmq = float(deriv.find("Cmq").text)

        # print("[정보] aircraft parameters XML/xlsx 로딩 완료")

    def run_simulation(self):
        """Run UAM Crash Trajectory Simulation (6DOF Dynamics)

        Returns
        -------
        uam_mass: List[float]
            A list containing mass values of the UAM(or fragments)

        uam_traj_data: List[np.ndarray]
            A list of arrays, where each array contains 6DOF trajectory data of the UAM(or fragments)
        """

        # 초기 조건 설정
        x, y, z = 0.0, 0.0, self.h
        u, v, w = self.v_x, self.v_y, self.v_z
        phi, theta, psi = 0.0, np.deg2rad(self.pitch_deg), 0.0
        p, q, r = 0.0, 0.0, 0.0

        x_arr, y_arr, z_arr = [], [], []
        vel_arr = []
        traj_pitch_angle_arr = []
        p_arr, q_arr, r_arr = [], [], []
        phi_arr, theta_arr, psi_arr = [], [], []
        beta_arr = []
        time_arr = []   # 시간 기록용

        for step in range(self.steps):
            # === 회전행렬 (Body→Inertial, 중력 투영용) ===
            R_bi = self.rotation_matrix(phi, theta, psi)

            # === 속도/동압/공기밀도 ===
            V = np.sqrt(u*u + v*v + w*w)
            if V < 1e-6:
                break
            # 간단 ISA 근사 (z는 지면 위 고도만 사용)
            z_clamp = max(z, 0.0)
            rho = 1.225 * (1.0 - 2.25577e-5 * z_clamp)**4.2561
            q_dyn = 0.5 * rho * V*V

            # === 받음각/옆미끄럼각 ===
            alpha = np.arctan2(w, u)              # [rad]
            a_deg = np.clip(np.degrees(alpha), -20.0, 20.0)   # 외삽 폭 제한(테이블 범위)
            beta = np.arcsin(np.clip(v / V, -1.0, 1.0))       # [rad] JSBSim aero/beta-rad과 동일 정의

            # === 세로축 공력계수(alpha 테이블 보간) ===
            CL = float(self.CL(a_deg))
            CD = float(self.CD(a_deg))
            Cm = float(self.Cm(a_deg))

            # === 가로/방향 공력계수(beta + 각속도 선형 미계수 조합) ===
            b2V = self.b / (2.0 * V + 1e-9)
            c2V = self.c / (2.0 * V + 1e-9)
            CY = self.CYb * beta + self.CYp * b2V * p + self.CYr * b2V * r
            Cl = self.Clb * beta + self.Clp * b2V * p + self.Clr * b2V * r
            Cn = self.Cnb * beta + self.Cnp * b2V * p + self.Cnr * b2V * r
            Cm_total = Cm + self.Cmq * c2V * q

            # === 공력(Body) : L/D 분해 ===
            L = q_dyn * self.S * CL
            D = q_dyn * self.S * CD
            Y = q_dyn * self.S * CY
            ca, sa = np.cos(alpha), np.sin(alpha)
            Fx = -D*ca - L*sa
            Fy = Y
            Fz = -D*sa + L*ca

            # === 중력(Body) ===
            g_body = R_bi.T @ np.array([0.0, 0.0, -self.g])

            # === 회전좌표 보정항: - ω × v_b ===
            cor_x = q*w - r*v
            cor_y = r*u - p*w
            cor_z = p*v - q*u

            # === 병진가속도 (Body) ===
            ax_b = Fx/self.m + g_body[0] - cor_x
            ay_b = Fy/self.m + g_body[1] - cor_y
            az_b = Fz/self.m + g_body[2] - cor_z

            # === 속도 적분 ===
            u += ax_b * self.dt
            v += ay_b * self.dt
            w += az_b * self.dt

            # === 모멘트 ===
            Mx = q_dyn * self.S * self.b * Cl
            My = q_dyn * self.S * self.c * Cm_total
            Mz = q_dyn * self.S * self.b * Cn

            # === 회전 동역학 (Ixz 포함 일반식) ===
            Ix, Iy, Iz, Ixz = self.Ix, self.Iy, self.Iz, self.Ixz
            K = Ix*Iz - Ixz*Ixz
            # JSBSim 계열 형태
            p_dot = ( Ixz*(Ix - Iy + Iz)*p*q - (Iz*(Iz - Iy) + Ixz*Ixz)*q*r + Iz*Mx + Ixz*Mz ) / K
            q_dot = ( (Iz - Ix)*p*r - Ixz*(p*p - r*r) + My ) / Iy
            r_dot = ( ( Ix*(Ix - Iy) + Ixz*Ixz )*p*q - Ixz*(Ix - Iy + Iz)*q*r + Ixz*Mx + Ix*Mz ) / K

            # === 각속도 적분 ===
            p += p_dot * self.dt
            q += q_dot * self.dt
            r += r_dot * self.dt

            # === 오일러 운동학 ===
            cth = np.cos(theta)
            if abs(cth) < 1e-3:
                break
            phi_dot   = p + np.tan(theta)*(q*np.sin(phi) + r*np.cos(phi))
            theta_dot = q*np.cos(phi) - r*np.sin(phi)
            psi_dot   = (q*np.sin(phi) + r*np.cos(phi)) / cth

            phi   += phi_dot   * self.dt
            theta += theta_dot * self.dt
            psi   += psi_dot   * self.dt

            # === 위치 적분 (Inertial) ===
            R_bi = self.rotation_matrix(phi, theta, psi)
            vel_I = R_bi @ np.array([u, v, w])
            x += vel_I[0] * self.dt
            y += vel_I[1] * self.dt
            z += vel_I[2] * self.dt

            # === 진행방향 기준 pitch(Flight-path angle) 로그 ===
            hs = np.hypot(u, v)
            traj_pitch_angle = np.degrees(np.arctan2(w, hs))

            # === 로그 ===
            time_arr.append(step * self.dt)
            x_arr.append(x); y_arr.append(y); z_arr.append(z)
            vel_arr.append(V)
            traj_pitch_angle_arr.append(traj_pitch_angle)
            p_arr.append(p); q_arr.append(q); r_arr.append(r)
            phi_arr.append(phi); theta_arr.append(theta); psi_arr.append(psi)
            beta_arr.append(np.degrees(beta))

            if z <= 0.0:
                break

        # 로그 DataFrame 구성
        log_df = pd.DataFrame({
            "time [s]": time_arr,
            "x [m]": x_arr,
            "y [m]": y_arr,
            "z [m]": z_arr,
            "V [m/s]": vel_arr,
            "γ [deg]": traj_pitch_angle_arr,
            "p [deg/s]": np.degrees(p_arr),
            "q [deg/s]": np.degrees(q_arr),
            "r [deg/s]": np.degrees(r_arr),
            "phi [deg]": np.degrees(phi_arr),
            "theta [deg]": np.degrees(theta_arr),
            "psi [deg]": np.degrees(psi_arr),
            "beta [deg]": beta_arr,
        })

        # plot용 데이터 (x,y,z만 numpy로)
        uam_traj_data = [log_df[["x [m]", "y [m]", "z [m]"]].to_numpy()]
        uam_mass = [self.m]

        return uam_mass, uam_traj_data, log_df

    def rotation_matrix(self, phi, theta, psi):
        """Body → Inertial 회전 행렬 계산"""
        R11 = np.cos(theta) * np.cos(psi)
        R12 = np.cos(theta) * np.sin(psi)
        R13 = -np.sin(theta)
        R21 = np.sin(phi) * np.sin(theta) * np.cos(psi) - np.cos(phi) * np.sin(psi)
        R22 = np.sin(phi) * np.sin(theta) * np.sin(psi) + np.cos(phi) * np.cos(psi)
        R23 = np.sin(phi) * np.cos(theta)
        R31 = np.cos(phi) * np.sin(theta) * np.cos(psi) + np.sin(phi) * np.sin(psi)
        R32 = np.cos(phi) * np.sin(theta) * np.sin(psi) - np.sin(phi) * np.cos(psi)
        R33 = np.cos(phi) * np.cos(theta)
        return np.array([[R11, R12, R13],
                         [R21, R22, R23],
                         [R31, R32, R33]])

    def plot_trajectories(self, UAM_traj_data):
        fig = plt.figure(figsize=(12,8))
        ax = fig.add_subplot(111, projection='3d')

        # (1) UAM(드론)의 궤적(파란색)
        for trajectory in UAM_traj_data:
            ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], 'b-', linewidth=1)

        ax.view_init(elev=0, azim=90)

        custom_lines = [
            Line2D([0], [0], color='b', lw=4),  # 파란색 (UAM)
        ]
        ax.legend(custom_lines, ['UAM Trajectory'], loc='upper right', fontsize='medium')

        plt.show()


#%% 테스트
def main():
    print("▶ main 함수 실행됨")  # 출력 테스트용

    h = 400
    v_x = 50.33
    v_y = 0.0   # 참고: y-velocity(측풍/횡방향)를 0이 아닌 값으로 주면 beta가 즉시
                # 발생해 이번 수정의 CYb/Clb/Cnb 경로를 바로 확인할 수 있음
    v_z = 0
    pitch_deg = 0
    yaw_deg = 0
    roll_deg = 0

    simulation = UAM_dynamic_simulation(h, v_x, v_y, v_z, pitch_deg, yaw_deg, roll_deg)
    UAM_mass, UAM_traj_data, log_df = simulation.run_simulation()
    simulation.plot_trajectories(UAM_traj_data)

    # 로그 확인
    print("\n=== 시뮬레이션 로그 (앞부분 5줄) ===")
    print(log_df.head())

    print("\n=== 시뮬레이션 로그 (마지막 5줄) ===")
    print(log_df.tail())

    # 엑셀 파일로 저장
    log_df.to_excel("UAM_simulation_log.xlsx", index=False)
    print("\n[완료] 로그가 'UAM_simulation_log.xlsx' 파일로 저장되었습니다.")


if __name__ == "__main__":
    main()
