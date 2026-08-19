import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
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
        self.pitch_deg = -pitch_deg
        self.yaw_deg = yaw_deg
        self.roll_deg = roll_deg

        # 기본 파라미터
        self.setup_parameters()

        # Cessna 172 기본 파라미터
        self.init_aircraft_parameters()

    def setup_parameters(self):
        self.rho = 1.225        # 공기 밀도 (kg/m^3)
        self.g = 9.80665        # 중력 가속도 (m/s^2)
        self.cd = 1.16          # fragment drag coefficient

        # simulation setup
        self.dt = 0.01          # 시간 간격 (s)
        self.t_max = 120        # 최대 시뮬레이션 시간 (s)
        self.steps = int(self.t_max / self.dt)

    def init_aircraft_parameters(self, xml_path=r"DB\aircraft\cessna172_config.xml"):
        """XML에서 기체 파라미터 불러오기"""
        tree = ET.parse(xml_path)
        root = tree.getroot()

        mp = root.find("mass_properties")
        inertia = mp.find("inertia")
        aero = root.find("aero_coefficients")

        self.m = float(mp.find("mass").text)
        self.S = float(mp.find("wing_area").text)
        self.c = float(mp.find("mean_chord").text)
        self.b = float(mp.find("wing_span").text)

        self.Ix = float(inertia.find("Ix").text)
        self.Iy = float(inertia.find("Iy").text)
        self.Iz = float(inertia.find("Iz").text)

        self.CL = float(aero.find("CL").text)
        self.CD = float(aero.find("CD").text)
        self.Cm = float(aero.find("Cm").text)
        self.CY = float(aero.find("CY").text)
        self.Cl = float(aero.find("Cl").text)
        self.Cn = float(aero.find("Cn").text)

        # print("[정보] aircraft parameters XML 로딩 완료")


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


        for step in range(self.steps):
            V = np.sqrt(u**2 + v**2 + w**2)
            if V < 1e-6:
                break

            alpha = np.arctan2(w, u)
            q_dyn = 0.5 * self.rho * V**2

            # 공력 계산
            L = q_dyn * self.S * self.CL
            D = q_dyn * self.S * self.CD
            Y = q_dyn * self.S * self.CY

            Fx = -D * np.cos(alpha) - L * np.sin(alpha)
            Fy = Y
            Fz = -D * np.sin(alpha) + L * np.cos(alpha)

            # 회전 행렬 (Body → Inertial)
            R_bi = self.rotation_matrix(phi, theta, psi)

            g_vec = np.array([0, 0, -self.g])
            g_body = R_bi.T @ g_vec

            ax_b = Fx / self.m + g_body[0]
            ay_b = Fy / self.m + g_body[1]
            az_b = Fz / self.m + g_body[2]

            u += ax_b * self.dt
            v += ay_b * self.dt
            w += az_b * self.dt

            Mx = q_dyn * self.S * self.b * self.Cl
            My = q_dyn * self.S * self.c * self.Cm
            Mz = q_dyn * self.S * self.b * self.Cn

            dp = (Mx + (self.Iy - self.Iz) * q * r) / self.Ix
            dq = (My + (self.Iz - self.Ix) * r * p) / self.Iy
            dr = (Mz + (self.Ix - self.Iy) * p * q) / self.Iz

            p += dp * self.dt
            q += dq * self.dt
            r += dr * self.dt

            if abs(np.cos(theta)) < 1e-3:
                break

            phi_dot = p + np.tan(theta) * (q * np.sin(phi) + r * np.cos(phi))
            theta_dot = q * np.cos(phi) - r * np.sin(phi)
            psi_dot = (q * np.sin(phi) + r * np.cos(phi)) / np.cos(theta)

            phi += phi_dot * self.dt
            theta += theta_dot * self.dt
            psi += psi_dot * self.dt

            vel_inertial = R_bi @ np.array([u, v, w])
            x += vel_inertial[0] * self.dt
            y += vel_inertial[1] * self.dt
            z += vel_inertial[2] * self.dt

            x_arr.append(x)
            y_arr.append(y)
            z_arr.append(z)
            vel = np.sqrt(u**2 + v**2 + w**2)
            vel_arr.append(vel)

            # 진행방향 기준 pitch angle 계산 (rad → deg)
            horizontal_speed = np.sqrt(u**2 + v**2)
            traj_pitch_angle = np.arctan2(w, horizontal_speed)  # 지면 기준 기울기
            traj_pitch_angle_arr.append(np.rad2deg(traj_pitch_angle))



            if z <= 0:
                break

        trajectory_vel_pitch = np.column_stack((
            x_arr, y_arr, z_arr,   # 위치
            vel_arr,               # 속도 크기
            traj_pitch_angle_arr              # pitch 각도
        ))
        uam_traj_data = [trajectory_vel_pitch]
        uam_mass = [self.m]

        return uam_mass, uam_traj_data

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
    v_y = 50
    v_z = 0
    pitch_deg = 0
    yaw_deg = 0
    roll_deg = 0

    simulation = UAM_dynamic_simulation(h, v_x, v_y, v_z, pitch_deg, yaw_deg, roll_deg)
    UAM_mass, UAM_traj_data = simulation.run_simulation()
    simulation.plot_trajectories(UAM_traj_data)



if __name__ == "__main__":
    main()
