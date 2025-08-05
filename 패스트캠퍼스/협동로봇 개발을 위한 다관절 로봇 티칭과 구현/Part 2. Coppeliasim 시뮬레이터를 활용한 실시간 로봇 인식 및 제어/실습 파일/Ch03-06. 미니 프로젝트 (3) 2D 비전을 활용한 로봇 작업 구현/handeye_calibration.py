import time
import numpy as np
import cv2
import Command
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import json

# ArUco dictionary
ARUCO_DICT = {
    "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000
}

Type = 'DICT_5X5_1000'
sizeofmarker = 0.1

# CoppeliaSim 연결
client = RemoteAPIClient()
sim = client.require('sim')

if sim.simulation_advancing_running == sim.getSimulationState():
    sim.stopSimulation()
    time.sleep(1)
sim.loadScene('C:/src/resource/coppeliasim/scene/vision_realsense_pick_and_place.ttt')
vision_sensor_handle = sim.getObject('/visionSensor')
rg2_handle = sim.getObject('/UR10/RG2') 
tip_handle = sim.getObject('/UR10/UR10_tip')  # UR10의 엔드이펙터(TCP)
target_handle = sim.getObject('/UR10_target')  # UR10의 목표점
base_handle = sim.getObject('/UR10')  # UR10 베이스
target_handle = sim.getObject('/UR10_target')  # UR10 목표점

# 속도, 가속도, 델타 값 설정
vel = 110 * np.pi / 180
accel = 40 * np.pi / 180
jerk = 80 * np.pi / 180

maxVel = [vel, vel, vel, vel, vel, vel]
maxAccel = [accel, accel, accel, accel, accel, accel]
maxJerk = [jerk, jerk, jerk, jerk, jerk, jerk]

def euler_to_quaternion(roll, pitch, yaw):
    """
    오일러 각도를 쿼터니언(qx, qy, qz, qw)으로 변환하는 함수
    """

    roll = np.deg2rad(roll)
    pitch = np.deg2rad(pitch)
    yaw = np.deg2rad(yaw)

    cy = np.cos(yaw * 0.5)
    sy = np.sin(yaw * 0.5)
    cp = np.cos(pitch * 0.5)
    sp = np.sin(pitch * 0.5)
    cr = np.cos(roll * 0.5)
    sr = np.sin(roll * 0.5)

    qw = cr * cp * cy + sr * sp * sy
    qx = sr * cp * cy - cr * sp * sy
    qy = cr * sp * cy + sr * cp * sy
    qz = cr * cp * sy - sr * sp * cy

    return [qx, qy, qz, qw]

def quaternion_offset(q, offset):
    """
    주어진 쿼터니언 q에 오프셋을 적용하여 새로운 쿼터니언을 계산합니다.
    offset은 x, y, z축 기준 회전 각도 (도 단위)를 나타내는 리스트입니다.
    """
    # 각 축에 대한 오프셋 회전 쿼터니언 생성
    offset_qx = euler_to_quaternion(offset[0], 0, 0)  # x축 회전
    offset_qy = euler_to_quaternion(0, offset[1], 0)  # y축 회전
    offset_qz = euler_to_quaternion(0, 0, offset[2])  # z축 회전

    # 오프셋 회전 쿼터니언 계산
    offset_q = np.array([1, 0, 0, 0])  # 단위 쿼터니언 (회전 없음)
    offset_q = quaternion_multiply(offset_q, offset_qx)
    offset_q = quaternion_multiply(offset_q, offset_qy)
    offset_q = quaternion_multiply(offset_q, offset_qz)

    # 원본 쿼터니언과 오프셋 쿼터니언을 곱하여 새로운 쿼터니언 계산
    new_q = quaternion_multiply(q, offset_q)

    return new_q

def quaternion_multiply(q1, q2):
    """
    두 쿼터니언을 곱하는 함수입니다.
    """
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x2 * w1 + y1 * z2 - z1 * y2
    y = w1 * y2 + y2 * w1 + z1 * x2 - x1 * z2
    z = w1 * z2 + z2 * w1 + x1 * y2 - y1 * x2
    return np.array([x, y, z, w])

def quaternion_to_rotation_vector(qx, qy, qz, qw):
    # Quaternion을 회전 행렬로 변환
    R = np.array([
        [1 - 2*(qy**2 + qz**2), 2*(qx*qy - qw*qz), 2*(qx*qz + qw*qy)],
        [2*(qx*qy + qw*qz), 1 - 2*(qx**2 + qz**2), 2*(qy*qz - qw*qx)],
        [2*(qx*qz - qw*qy), 2*(qy*qz + qw*qx), 1 - 2*(qx**2 + qy**2)]
    ])
    
    # 회전 행렬을 회전 벡터로 변환
    rotation_vector_2d, _ = cv2.Rodrigues(R)
    rotation_vector_1d = to1D(rotation_vector_2d)

    return rotation_vector_1d

def quaternion_to_euler(q):
    """
    쿼터니언을 오일러 각 (Roll, Pitch, Yaw)으로 변환합니다.
    q: [x, y, z, w] 형태의 쿼터니언
    """
    x, y, z, w = q

    # Roll (x축 회전)
    roll = np.arctan2(2 * (w * x + y * z), 1 - 2 * (x**2 + y**2))

    # Pitch (y축 회전)
    pitch = np.arcsin(2 * (w * y - z * x))

    # Yaw (z축 회전)
    yaw = np.arctan2(2 * (w * z + x * y), 1 - 2 * (y**2 + z**2))

    # 라디안을 도로 변환
    roll_deg = np.rad2deg(roll)
    pitch_deg = np.rad2deg(pitch)
    yaw_deg = np.rad2deg(yaw)

    return roll_deg, pitch_deg, yaw_deg

def to1D(two_d):
    arr = np.array(two_d)
    one_d = arr.flatten()
    return one_d   

def create_transformation_matrix(R, P):
    """
    회전 행렬 R (3x3)과 변환 벡터 P (3x1)를 받아 4x4 변환 행렬을 생성합니다.
    R: 3x3 회전 행렬
    P: 3x1 변환 벡터
    return: 4x4 변환 행렬
    """
    # 회전 행렬과 변환 벡터를 결합하여 3x4 행렬 생성
    T = np.hstack((R, P))
    
    # 마지막 행을 추가하여 4x4 행렬로 변환
    T = np.vstack((T, np.array([0, 0, 0, 1])))
    
    return T

# 실행 테스트
sim.startSimulation()
sim.wait(3)

# 카메라 파라미터
resolutionX = 1920
resolutionY = 1080
perspectiveAngle = 69
perspectiveAngle = np.deg2rad(perspectiveAngle)
d = 0.01
ratio = resolutionX / resolutionY

# 계산된 fx, fy 값
if ratio > 1:
    angleX = perspectiveAngle
    angleY = 2 * np.arctan(np.tan(perspectiveAngle / 2) / ratio)
else:
    angleX = 2 * np.arctan(np.tan(perspectiveAngle / 2) * ratio)
    angleY = perspectiveAngle

fx = d / (2 * np.tan(angleX / 2))
fy = d / (2 * np.tan(angleY / 2))

fx = fx * resolutionX / d
fy = fy * resolutionY / d

# 내부 카메라 행렬
cx = resolutionX / 2
cy = resolutionY / 2
camera_matrix = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]], dtype=np.double)

# Distortion coefficients (초기값은 0)
dist_coeffs = np.zeros((4, 1))

# 3D 객체 좌표 (체커보드 각 코너의 3D 좌표)
objPoints = np.array([
    [sizeofmarker / 2, -sizeofmarker / 2, 0],
    [sizeofmarker / 2, sizeofmarker / 2, 0],
    [-sizeofmarker / 2, sizeofmarker / 2, 0],
    [-sizeofmarker / 2, -sizeofmarker / 2, 0]
], dtype=np.double)

# Hand-Eye Calibration을 위한 변수 초기화
robot_position_list = []
robot_rotation_list = []
camera_position_list = []
camera_rotation_list = []


# 여러 번 촬영을 위한 반복 횟수
num_iterations = 20
initTr = sim.getObjectPose(tip_handle, base_handle)
T_hand_to_base_ori = sim.getObjectMatrix(base_handle, tip_handle)
T_hand_to_base_ori_3X4 = np.array(T_hand_to_base_ori).reshape(3, 4)
T_hand_to_base = np.vstack((T_hand_to_base_ori_3X4, np.array([0, 0, 0, 1])))

print("initTr:", initTr)
cal_pose = []
cal_pose.append((initTr[0] + 0.2, initTr[1], initTr[2] - 0.1))
cal_pose.append((initTr[0] + 0.1, initTr[1] +  0.1, initTr[2]- 0.1))
cal_pose.append((initTr[0] + 0.1, initTr[1] - 0.1, initTr[2]- 0.1))
cal_pose.append((initTr[0] - 0.1, initTr[1] + 0.1, initTr[2] + 0.1))
cal_pose.append((initTr[0] - 0.1, initTr[1] + 0.2, initTr[2]- 0.1))
cal_pose.append((initTr[0] - 0.1, initTr[1], initTr[2]- 0.1))
cal_pose.append((initTr[0] - 0.2, initTr[1] - 0.2 , initTr[2]- 0.1))
cal_pose.append((initTr[0] - 0.3, initTr[1] - 0.2, initTr[2]- 0.1))
cal_pose.append((initTr[0] - 0.2, initTr[1] - 0.2, initTr[2]- 0.1))
cal_pose.append((initTr[0] -0.1, initTr[1] - 0.2, initTr[2]- 0.1))
cal_pose.append((initTr[0] + 0.2, initTr[1], initTr[2] - 0.1))
cal_pose.append((initTr[0] + 0.1, initTr[1] +  0.1, initTr[2]- 0.1))
cal_pose.append((initTr[0] + 0.1, initTr[1] - 0.1, initTr[2]- 0.1))
cal_pose.append((initTr[0] - 0.1, initTr[1] + 0.1, initTr[2] + 0.1))
cal_pose.append((initTr[0] - 0.1, initTr[1] + 0.2, initTr[2]- 0.1))
cal_pose.append((initTr[0] - 0.1, initTr[1], initTr[2]- 0.1))
cal_pose.append((initTr[0] - 0.2, initTr[1] - 0.2 , initTr[2]- 0.1))
cal_pose.append((initTr[0] - 0.3, initTr[1] - 0.2, initTr[2]- 0.1))
cal_pose.append((initTr[0] - 0.2, initTr[1] - 0.2, initTr[2]- 0.1))
cal_pose.append((initTr[0] -0.1, initTr[1] - 0.2, initTr[2]- 0.1))

rx = 0
ry = 0
rz = 0

for i in range(num_iterations):
    # 비전 센서로부터 이미지 받아오기

    image_origin, [resX, resY] = sim.getVisionSensorImg(vision_sensor_handle)
    image_origin = np.frombuffer(image_origin, dtype=np.uint8).reshape(resY, resX, 3)

    # 이미지가 정상적으로 로드되었는지 확인
    gray_image = cv2.cvtColor(image_origin, cv2.COLOR_BGR2GRAY)

    # Adaptive Thresholding
    image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 99, 0)
    # cv2.imshow("Captured Image", image)
    # cv2.waitKey(1)
    contour_img = np.copy(image)
    image_copy = image_origin.copy()
    contours1,_ = cv2.findContours(contour_img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    result = cv2.drawContours(image_copy, contours1, -1, (255,0,255),1)

    # ArUco 마커 인식
    arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[Type])
    detectorParams = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(arucoDict, detectorParams)
    corners, ids, rejected_candidates = detector.detectMarkers(image)
    
    cv2.imwrite('saved_image{}.jpg'.format(i), image)

    try:
        imagePoints = np.array(corners[0], dtype=np.double)
    except IndexError:
        print("Out of FOV, continue")
    else:
           # solvePnP를 사용하여 회전 벡터와 변환 벡터 계산
        _, rvec, tvec = cv2.solvePnP(objPoints, imagePoints, camera_matrix, dist_coeffs)
        
        # 3D 포인트를 카메라 좌표계로 변환
        rot_mat, _ = cv2.Rodrigues(rvec)

        T = np.eye(4)  # 4x4 단위 행렬
        T[0:3, 0:3] = rot_mat  # 상단 3x3 회전 행렬을 설정
        T[0:3, 3] = tvec.flatten()  # 마지막 열에 위치 벡터 설정

        # 변환 행렬의 역행렬 계산
        T_inv = np.linalg.inv(T)

        # 역행렬에서 회전 행렬과 위치 벡터 분리
        rot_mat_inv = T_inv[0:3, 0:3]  # 역행렬에서 회전 행렬 부분
        tvec_inv = T_inv[0:3, 3]  # 역행렬에서 위치 벡터 부분

        # 역행렬에서 회전 행렬을 회전 벡터로 변환
        rvec_inv, _ = cv2.Rodrigues(rot_mat_inv)

        #camera_position = np.matrix(rot_mat).T * np.matrix(tvec)
        print("tvec", tvec)
        print("rot_mat", rot_mat)
        camera_position_vector = to1D(tvec_inv)
        camera_rotation_vector = to1D(rvec_inv)
        
        # 카메라 포즈와 로봇 포즈 저장
        camera_position_list.append(camera_position_vector)
        camera_rotation_list.append(camera_rotation_vector)
        # 로봇 포즈는 시뮬레이션을 통해 수집하거나 별도로 설정 필요 (여기서는 예시로 임의 값을 사용)
        # 실제 로봇 포즈를 수집하려면 별도의 로봇 제어 명령과 데이터를 받아야 합니다
        # 예시로 임의의 로봇 포즈를 추가합니다.
        robot_position = np.array(sim.getObjectPosition(tip_handle, base_handle), dtype=np.double)
        robot_rot_quaternion = sim.getObjectQuaternion(tip_handle, base_handle)

        base_to_target_mat = sim.getObjectMatrix(base_handle, tip_handle) #target->base T
        base_to_target_mat_3X4 = np.array(base_to_target_mat).reshape(3, 4)
        T_base_to_target_mat = np.vstack((base_to_target_mat_3X4, np.array([0, 0, 0, 1])))
        robot_position_inv, robot_orientation_inv = Command.extract_translation_and_rotation(T_base_to_target_mat)
        robot_rot_vec = quaternion_to_rotation_vector(robot_rot_quaternion[0], robot_rot_quaternion[1], robot_rot_quaternion[2], robot_rot_quaternion[3])
        print("robot_position", robot_position_inv)
        print("robot_rot_quaternion", robot_position_inv)

        robot_position_list.append(robot_position_inv)
        robot_rotation_list.append(robot_orientation_inv)
        print("rotvec:", robot_rot_vec)

        print(f"Iteration {i+1}")
        print("Camera Position:", camera_position_vector)
        print("Camera rot:", camera_rotation_vector)
        print("Robot Position:", robot_position)
        print("Robot rot:", robot_rot_vec)

        time.sleep(1)  # 시간 지연
        rx, ry, rz = quaternion_to_euler(robot_rot_quaternion)
        print(cal_pose[i])
        print(rx, ry, rz)
    finally:
        if i % 2 == 0:  
            sign = 1  
        else:  
            sign = -1  

        new_q = euler_to_quaternion(rx + sign * 10, ry + sign * 10, rz * sign * 20)

        Command.move_linear_absolute(sim=sim, tip_handle=tip_handle, target_handle=target_handle, position=cal_pose[i], orientation_quaternion=new_q, base_handle=base_handle)

        
    
# Hand-Eye Calibration 결과 출력
cam_to_hand_r, cam_to_hand_p = cv2.calibrateHandEye(
        robot_rotation_list, robot_position_list,  # 첫 번째 요소는 회전 행렬, 두 번째 요소는 위치 벡터
        camera_rotation_list, camera_position_list,  # 동일하게 첫 번째 요소는 회전 행렬, 두 번째 요소는 위치 벡터
        method=cv2.CALIB_HAND_EYE_TSAI   # Tsai 알고리즘을 사용
    )
#hand_eye_transformation = calibrate_hand_eye(robot_poses, camera_poses)
print("cam_to_hand_r")
print(cam_to_hand_r)
print("cam_to_hand_t")
print(cam_to_hand_p)

# Base-to-Hand 변환 행렬 생성
#T_base_to_hand = create_transformation_matrix(R_base_to_hand, P_base_to_hand)
# Hand-to-Camera 변환 행렬 생성
T_camera_to_hand = create_transformation_matrix(cam_to_hand_r, cam_to_hand_p)

# Base-to-Camera 변환 행렬 계산 (T_base_to_camera = T_base_to_hand * T_hand_to_camera)
T_camera_to_base = np.dot(T_camera_to_hand, T_hand_to_base)
print("T_camera_to_base", T_camera_to_base)

T_cam_to_hand_ori = sim.getObjectMatrix(tip_handle, vision_sensor_handle)
T_cam_to_hand_ori_3X4 = np.array(T_cam_to_hand_ori).reshape(3, 4)
T_camera_to_hand_real = np.vstack((T_cam_to_hand_ori_3X4, np.array([0, 0, 0, 1])))
print("T_camera_to_hand_real", T_camera_to_hand_real)

T_camera_to_base_real = np.dot(T_camera_to_hand_real, T_hand_to_base)
print("T_camera_to_base_real", T_camera_to_base_real)

matrix_list = T_camera_to_base.tolist()

# JSON 파일로 저장
with open('matrix_data.json', 'w') as json_file:
    json.dump(matrix_list, json_file, indent=4)

#camera_point = np.array([[x_c], [y_c], [z_c]])
# 시뮬레이션 종료
sim.stopSimulation()

