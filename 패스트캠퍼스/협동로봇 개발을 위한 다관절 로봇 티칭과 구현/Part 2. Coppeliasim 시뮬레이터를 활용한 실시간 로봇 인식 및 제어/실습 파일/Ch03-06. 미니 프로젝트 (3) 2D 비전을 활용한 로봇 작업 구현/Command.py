import time
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import cv2

def open_gripper(sim, name):
    sim.setInt32Signal(name, 1)
    time.sleep(1)

def close_gripper(sim, name):
    sim.setInt32Signal(name, 0)
    time.sleep(1)

def move_joint(sim, joint_handles, tip_handle, target_handle, maxVel, maxAccel, maxJerk, targetConf):
    current_pose = sim.getObjectPose(tip_handle)
    sim.setObjectPose(target_handle, current_pose, sim.handle_world)   
    currentConf = []
    for i in range(len(joint_handles)):
        currentConf.append(sim.getJointPosition(joint_handles[i]))
    params = {}
    params['joints'] = joint_handles
    params['targetPos'] = targetConf
    params['maxVel'] = maxVel
    params['maxAccel'] = maxAccel
    params['maxJerk'] = maxJerk
    sim.moveToConfig(params)

    current_pose = sim.getObjectPose(tip_handle)
    sim.setObjectPose(target_handle, current_pose, sim.handle_world)    
    sim.wait(0.1)
    
def move_linear(sim, tip_handle, target_handle, target_pos):
    current_pose = sim.getObjectPose(tip_handle)
    sim.setObjectPose(target_handle, current_pose, sim.handle_world)

    target_pose = current_pose.copy()
    target_pose[0] = target_pos[0]
    target_pose[1] = target_pos[1]
    target_pose[2] = target_pos[2]

    params = {
        "object": target_handle,
        "targetPose": target_pose,
        "maxVel": [0.5, 0.5, 0.5, 1],
        "maxAccel": [0.5, 0.5, 0.5, 1],
        "maxJerk": [0.5, 0.5, 0.5, 1],
    }
    sim.moveToPose(params)

def move_linear(sim, tip_handle, target_handle, base_handle, position, orientation_quaternion):
    current_pose = sim.getObjectPose(tip_handle)
    sim.setObjectPose(target_handle, current_pose, sim.handle_world)

    target_pose = current_pose.copy()
    target_pose[0] = position[0]
    target_pose[1] = position[1]
    target_pose[2] = position[2]
    target_pose[3] = orientation_quaternion[0]
    target_pose[4] = orientation_quaternion[1] 
    target_pose[5] = orientation_quaternion[2] 
    target_pose[6] = orientation_quaternion[3] 

    params = {
        "object": target_handle,
        "targetPose": target_pose,
        "base": base_handle,
        "maxVel": [0.5, 0.5, 0.5, 1],
        "maxAccel": [0.5, 0.5, 0.5, 1],
        "maxJerk": [0.5, 0.5, 0.5, 1],
    }
    sim.moveToPose(params)

def move_linear_absolute(sim, tip_handle, target_handle, position, orientation_quaternion, base_handle = None):
    current_pose = sim.getObjectPose(tip_handle)
    sim.setObjectPose(target_handle, current_pose, sim.handle_world)
    # If relto_position and relto_orientation_quaternion are not provided, use default values (0)
    if base_handle:
        Tworld2base_ori = sim.getObjectMatrix(base_handle)
        Tworld2base_3X4 = np.array(Tworld2base_ori).reshape(3, 4)
        Tworld2base = np.vstack((Tworld2base_3X4, np.array([0, 0, 0, 1])))
        ori_mat = quaternion_to_rotation_matrix(orientation_quaternion)
        position_arr = np.array(position)[:, np.newaxis]
        target_pose_mat = create_transformation_matrix(ori_mat, position_arr)
        target_pose_mat_world = np.dot(Tworld2base, target_pose_mat)     
        target_position = extract_position_from_transformation_matrix(target_pose_mat_world)
        rotation_matrix = extract_rotation_from_transformation_matrix(target_pose_mat_world)
        target_quaternion = rotation_matrix_to_quaternion(rotation_matrix)
    target_pose = current_pose.copy()
    target_pose[0] = target_position[0]
    target_pose[1] = target_position[1]
    target_pose[2] = target_position[2]
    target_pose[3] = target_quaternion[0]
    target_pose[4] = target_quaternion[1] 
    target_pose[5] = target_quaternion[2] 
    target_pose[6] = target_quaternion[3] 

    # Set the parameters for motion
    params = {
        "object": target_handle,
        "targetPose": target_pose,
        "maxVel": [0.5, 0.5, 0.5, 1],
        "maxAccel": [0.5, 0.5, 0.5, 1],
        "maxJerk": [0.5, 0.5, 0.5, 1],
    }
    # Move the robot to the target pose
    sim.moveToPose(params)

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

def quaternion_to_euler(q):
    """
    쿼터니언을 오일러 각 (Roll, Pitch, Yaw)으로 변환합니다.
    q: [x, y, z, w] 형태의 쿼터니언
    """
    x, y, z, w = q

    # Roll (x축 회전)
    roll = np.arctan2(2 * (w * x + y * z), 1 - 2 * (x**2 + y**2))

    # Pitch (y축 회전)
    pitch_value = 2 * (w * y - z * x)
    # 피치를 -1과 1 사이로 클리핑
    pitch_value = np.clip(pitch_value, -1.0, 1.0)
    pitch = np.arcsin(pitch_value)

    # Yaw (z축 회전)
    yaw = np.arctan2(2 * (w * z + x * y), 1 - 2 * (y**2 + z**2))

    # 라디안을 도로 변환
    roll_deg = np.rad2deg(roll)
    pitch_deg = np.rad2deg(pitch)
    yaw_deg = np.rad2deg(yaw)

    return roll_deg, pitch_deg, yaw_deg

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

def quaternion_to_rotation_matrix(q):
    """
    주어진 쿼터니언을 3x3 회전 매트릭스로 변환합니다.
    q: [qx, qy, qz, qw] 형태의 쿼터니언
    """
    qx, qy, qz, qw = q
    norm = np.sqrt(qx**2 + qy**2 + qz**2 + qw**2)
    qx, qy, qz, qw = qx / norm, qy / norm, qz / norm, qw / norm
    # 회전 매트릭스 계산
    R = np.array([
        [1 - 2 * (qy**2 + qz**2), 2 * (qx * qy - qz * qw), 2 * (qx * qz + qy * qw)],
        [2 * (qx * qy + qz * qw), 1 - 2 * (qx**2 + qz**2), 2 * (qy * qz - qx * qw)],
        [2 * (qx * qz - qy * qw), 2 * (qy * qz + qx * qw), 1 - 2 * (qx**2 + qy**2)]
    ])
    
    return R

def extract_position_from_transformation_matrix(transformation_matrix):
    """
    트랜스포메이션 매트릭스에서 위치(position)을 추출합니다.
    transformation_matrix: 4x4 트랜스포메이션 매트릭스
    """
    position = transformation_matrix[:3, 3]  # 3x1 벡터로 위치 추출
    return position

def extract_rotation_from_transformation_matrix(transformation_matrix):
    """
    트랜스포메이션 매트릭스에서 회전(rotation)을 추출하여 3x3 회전 매트릭스로 반환합니다.
    transformation_matrix: 4x4 트랜스포메이션 매트릭스
    """
    rotation_matrix = transformation_matrix[:3, :3]  # 3x3 회전 매트릭스 추출
    return rotation_matrix

def rotation_matrix_to_quaternion(m):
    """
    3x3 회전 매트릭스를 쿼터니언으로 변환합니다.
    rotation_matrix: 3x3 회전 매트릭스
    """
    t = np.matrix.trace(m)
    q = np.asarray([0.0, 0.0, 0.0, 0.0], dtype=np.float64)

    if(t > 0):
        t = np.sqrt(t + 1)
        q[3] = 0.5 * t
        t = 0.5/t
        q[0] = (m[2,1] - m[1,2]) * t
        q[1] = (m[0,2] - m[2,0]) * t
        q[2] = (m[1,0] - m[0,1]) * t

    else:
        i = 0
        if (m[1,1] > m[0,0]):
            i = 1
        if (m[2,2] > m[i,i]):
            i = 2
        j = (i+1)%3
        k = (j+1)%3

        t = np.sqrt(m[i,i] - m[j,j] - m[k,k] + 1)
        q[i] = 0.5 * t
        t = 0.5 / t
        q[3] = (m[k,j] - m[j,k]) * t
        q[j] = (m[j,i] + m[i,j]) * t
        q[k] = (m[k,i] + m[i,k]) * t
    return q

def rotation_matrix_to_vector(rotation_matrix):
    """회전 행렬을 회전 벡터로 변환하는 함수"""
    theta = np.arccos((np.trace(rotation_matrix) - 1) / 2)
    
    if theta == 0:
        return np.array([0, 0, 0])  # 회전이 없으면 회전 벡터는 0
    
    r = np.array([
        [rotation_matrix[2, 1] - rotation_matrix[1, 2]],
        [rotation_matrix[0, 2] - rotation_matrix[2, 0]],
        [rotation_matrix[1, 0] - rotation_matrix[0, 1]]
    ]) / (2 * np.sin(theta))

    return r * theta  # 회전 벡터

def extract_translation_and_rotation(T):
    """4x4 변환 행렬에서 위치 벡터와 회전 벡터를 추출하는 함수"""
    # 3x1 위치 벡터 (마지막 열에서 추출)
    translation = T[0:3, 3]
    
    # 3x3 회전 행렬 (상단 왼쪽 3x3에서 추출)
    rotation_matrix = T[0:3, 0:3]
    
    # 회전 행렬을 회전 벡터로 변환
    rotation_vector = rotation_matrix_to_vector(rotation_matrix)
    
    return translation, rotation_vector

