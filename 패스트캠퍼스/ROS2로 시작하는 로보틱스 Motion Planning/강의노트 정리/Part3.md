# Chapter 1. 로봇의 정의와 구성요소
## 1. 강의 요약
1. 모션 플래닝의 활용 사례
2. 작업
3. 로봇
4. 환경
## 2. 로봇 공통점+링크
로봇의 공통점?
1. Link(동체) - 짝대기
2. Joint(관절) - 원통
3. Actuator(모터)

### Link(링크)
- 길이
- 모양
- 물리적 특성 (생략하기도 함)

## 3. 조인트 기본 설명
### Joint(조인트)
![[스크린샷 2025-10-04 오후 2.54.51.png]]
대표적인 조인트 6개
- Revolute
- Prismatic
- Helical
- Cylindrical
- Universal
- Spherical (우리 관절)

## 4. 조인트 예시1
__Dof(Degree of Freedom, 자유도)란?
	-> 박스의 상태를 정의하기 위해서 필요한 정보의 개수

ex) 박스의 상태를 정의하기 위해서 필요한 정보의 개수는?
-> x,y,z : 위치 정보
-> roll, pitch, yaw :각도 정보
총 6개의 정보 필요

조인트 별로 필요한 자유도 갯수
- Revolute -> Dof: 1
- Prismatic -> Dof: 1
- Helical -> Dof: 1
- Cylindrical -> Dof: 2
- Universal -> Dof: 2
- Spherical (우리 관절) -> Dof: 3

Joint(조인트) - Grubler's Formula
```
dof = m(N−1−J)+∑ (i = 1 to J) fᵢ
```
![[스크린샷 2025-10-04 오후 5.46.32.png]]
[[Chapter 1. 로봇의 정의와 구성요소.pdf]]
## 5. 조인트 예시2와 3

## 6. 엑추에이터와 URDF
Actuator(액추에이터)
- Mechanical(가장 많이 사용)
	- Electric motors
	- Linear actuators
- Pneumatic(공기, 유체)
- Hydraulic(유압)

URDF(Universal Robot Description Format)
-  실제 로봇의 물리적 구조를 표현하는 설계도
- 시뮬레이션에서 로봇 시각화 및 역학 계산

URDF를 구성하는 대표 구성 요소
1. __Link__
2. __Joint__
3. Inertial
4. Visual
5. Collisioni
6. __Transmission__
7. Material

- urdf 파일 예시
```xml
<robot name="two_link_arm">

  <link name="base_link">
    <visual>
      <geometry>
        <box size="0.2 0.2 0.05"/>
      </geometry>
    </visual>
  </link>

  <link name="link1">
    <inertial>
      <mass value="1.0"/>
      <inertia ixx="0.01" ixy="0" ixz="0" iyy="0.01" iyz="0" izz="0.01"/>
    </inertial>
    <visual>
      <geometry>
        <cylinder length="1.0" radius="0.05"/>
      </geometry>
    </visual>
  </link>

  <joint name="joint1" type="revolute">
    <parent link="base_link"/>
    <child link="link1"/>
    <origin xyz="0 0 0.05" rpy="0 0 0"/>
    <axis xyz="0 0 1"/>
    <limit effort="10" velocity="1.0" lower="-1.57" upper="1.57"/>
  </joint>

</robot>
```

