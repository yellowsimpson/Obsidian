import numpy as np

# 두 링크 길이
L1, L2 = 10, 7

# 목표 위치 (예시로 주어진 위치)
x_target, y_target = 10.472, 11.7615

# 역기구학 계산 함수 (Redundant 해법 포함)
def inverse_kinematics(x, y, L1, L2):
    # 코사인 법칙을 사용하여 theta2 계산
    r = np.sqrt(x**2 + y**2)
    cos_theta2 = (r**2 - L1**2 - L2**2) / (2 * L1 * L2)
    
    # theta2가 가능한지 확인 (코사인 값이 -1과 1 사이여야 함)
    if cos_theta2 < -1 or cos_theta2 > 1:
        return None  # 목표 위치는 도달 불가능
    
    # theta2 계산
    theta2_1 = np.arccos(cos_theta2)  # Elbow up (양의 부호)
    theta2_2 = -np.arccos(cos_theta2) # Elbow down (음의 부호)
    
    # theta1 계산
    k1 = L1 + L2 * np.cos(theta2_1)
    k2 = L2 * np.sin(theta2_1)
    theta1_1 = np.arctan2(y, x) - np.arctan2(k2, k1)
    
    k1 = L1 + L2 * np.cos(theta2_2)
    k2 = L2 * np.sin(theta2_2)
    theta1_2 = np.arctan2(y, x) - np.arctan2(k2, k1)
    
    # 각도를 도 단위로 변환
    theta1_1_deg = np.degrees(theta1_1)
    theta2_1_deg = np.degrees(theta2_1)
    theta1_2_deg = np.degrees(theta1_2)
    theta2_2_deg = np.degrees(theta2_2)
    
    return (theta1_1_deg, theta2_1_deg), (theta1_2_deg, theta2_2_deg)

# 역기구학 호출
joint_angles = inverse_kinematics(x_target, y_target, L1, L2)

if joint_angles:
    (theta1_deg_1, theta2_deg_1), (theta1_deg_2, theta2_deg_2) = joint_angles
    print(f"역기구학 결과 (Redundant 해법):")
    print(f"첫 번째 해법:")
    print(f"theta1: {theta1_deg_1:.2f}°, theta2: {theta2_deg_1:.2f}°")
    print(f"두 번째 해법:")
    print(f"theta1: {theta1_deg_2:.2f}°, theta2: {theta2_deg_2:.2f}°")
else:
    print("목표 위치에 도달할 수 없습니다.")
