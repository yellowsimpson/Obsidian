import sympy

#Rotation Matrix - X축 회전
def Rot_X(angle_rad):
    rot_martix = sympy.Matrix([[1,0,0,0],
                               [0,sympy.cos(angle_rad),-sympy.sin(angle_rad),0],
                               [0,sympy.sin(angle_rad),sympy.cos(angle_rad),0],
                               [0,0,0,1]]);
    return rot_martix
#Rotation Matrix - Y축 회전
def Rot_Y(angle_rad):
    rot_martix = sympy.Matrix([[sympy.cos(angle_rad),0,sympy.sin(angle_rad),0],
                               [0,1,0,0],
                               [-sympy.sin(angle_rad),0,sympy.cos(angle_rad),0],
                               [0,0,0,1]]);
    return rot_martix
#Rotation Matrix- Z축 회전
def Rot_Z(angle_rad):
    rot_martix = sympy.Matrix([[sympy.cos(angle_rad),-sympy.sin(angle_rad),0,0],
                               [sympy.sin(angle_rad),sympy.cos(angle_rad),0,0],
                               [0,0,1,0],
                               [0,0,0,1]]);
    return rot_martix

#Translation Matrix - 이동동
def Transl(x,y,z):
    transl_martix = sympy.Matrix([[1,0,0,x],
                                  [0,1,0,y],
                                  [0,0,1,z],
                                  [0,0,0,1]]);
    return transl_martix

# A 좌표계 기준 B 좌표계의 변환 행렬 생성 (회전 + 이동)
T_A_to_B = Transl(0, 20, 10) @ Rot_Y(-sympy.pi/2) @ Rot_X(sympy.pi/2)
T_A_to_B_2 = Transl(0, 20, 10) @ Rot_X(sympy.pi/2) @ Rot_Z(sympy.pi/2)

# B 좌표계의 점 P_B = (10, 0, 0) (열 벡터로 표현)
P_B = sympy.Matrix([10, 0, 0, 1])

# A 좌표계 기준으로 변환
P_A = T_A_to_B @ P_B
P_A_2 = T_A_to_B_2 @ P_B

# 결과 출력
print(P_A)
print(P_A_2)