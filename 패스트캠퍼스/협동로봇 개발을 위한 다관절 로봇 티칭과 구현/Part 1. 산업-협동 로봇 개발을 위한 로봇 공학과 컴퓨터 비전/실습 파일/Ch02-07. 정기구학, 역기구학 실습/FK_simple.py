import numpy as np

# DH 변환 행렬 함수
def DH(a, alpha, d, theta):
    # 라디안으로 각도를 변환
    theta = np.radians(theta)
    alpha = np.radians(alpha)
    
    return np.array([
        [np.cos(theta), -np.sin(theta) * np.cos(alpha), np.sin(theta) * np.sin(alpha), a * np.cos(theta)],
        [np.sin(theta), np.cos(theta) * np.cos(alpha), -np.cos(theta) * np.sin(alpha), a * np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

# 링크 길이 설정
L1, L2 = 10, 7  # 링크 길이

# 관절 각도 (라디안)
theta1, theta2 = 30, 45  # 각도 입력 (도 단위)

# 첫 번째 링크의 DH 파라미터
T1 = DH(L1, 0, 0, theta1)

# 두 번째 링크의 DH 파라미터
T2 = DH(L2, 0, 0, theta2)

# 최종 변환 행렬
T_final = np.dot(T1, T2)

# 끝단 위치 (최종 변환 행렬에서 위치 부분 추출)
end_effector = T_final[:3, 3]

# 출력
print("끝단 위치 (기호식):")
print(end_effector)

# 수치 대입 (theta1 = 30도, theta2 = 45도)
theta1_rad = np.radians(30)
theta2_rad = np.radians(45)

# 수치 계산 결과
end_effector_numeric = np.array([
    np.cos(theta1_rad) * L1 + np.cos(theta1_rad + theta2_rad) * L2,
    np.sin(theta1_rad) * L1 + np.sin(theta1_rad + theta2_rad) * L2,
    0  # Z축은 변하지 않음
])

print("\n끝단 위치 (수치 계산 결과):")
print(end_effector_numeric)