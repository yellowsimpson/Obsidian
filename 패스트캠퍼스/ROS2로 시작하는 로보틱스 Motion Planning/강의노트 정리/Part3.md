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





# Chapter 2. 로봇 좌표계의 개념

## 1. 강의 요약
1. 모션 플래닝의 활용 사례
2. 작업
3. 로봇
4. 환경
## 2. 좌표계 개요
로봇의 공통점?
1. Link(동체) - 짝대기
2. Joint(관절) - 원통
3. Actuator(모터)

### Link(링크)
- 길이
- 모양
- 물리적 특성 (생략하기도 함)

## 3. 좌표계 구분

## 4. 로봇 좌표계
- 절대 좌표계

### 로봇의 주요 좌표계
- Base Frame
	- 로봇의 베이스 및 첫 번째 링크
	- 로봇의 전체 기준점
- Joint Frame
	- 각 관절마다 정의되는 프레임
- Sensor Frame
	- 센서의 관찰 기준

좌표 변환의 필요성
	-> 다른 기준에서 물체의 위치를 알고 시을 때 필요
## 5. 변환행렬 개요
좌표계: 회전 + 평행 이동
좌표계 변환: 회전 변환 + 평행이동 변환
-> 이 2개로 좌표변환을 표현할 수 있다.
## 6. 반환행렬
회전변환: 방향을 회전

[[Chapter 2. 로봇 좌표계의 개념.pdf]]

평행이동: 위치를 이동



## 7. 로보틱스구조에서의 변환





# Chapter 3. 로봇 기구학

## 1. 이전 강의 요약
좌표계
- 절대 좌표계
- 상대 좌표계
- 로봇의 좌표계
- 회전변환과 평행이동
## 2. 정기구학

### 로봇 기구학(키네마틱스, Kinematics)
로봇 **기구학(Kinematics)** 은 로봇공학의 기본 중 하나로, **로봇의 움직임(자세와 위치)** 을 수학적으로 해석하는 분야입니다. 
주로 정기구학(forward kienmatics) +역기구학(inverse kienmatics)에 문제를 다룬다.
#### 🧠 1️⃣ 기구학의 기본 개념
기구학은 **힘이나 토크를 고려하지 않고**, **기구의 구조적 관계만으로 위치·자세를 다루는 학문**이에요.  
즉, "이 조인트(관절)를 이렇게 움직이면 로봇 팔 끝은 어디로 가는가?"를 다루는 것이죠.
로봇공학에서는 주로 **매니퓰레이터(로봇 팔)** 을 예로 들며 설명합니다.

### 정기구학 (Forward Kinematics)
__Joint값 *q = [q1, q2, q3 ... ]* -> (forward kinematics) ->position *p = [x, y, z, ...]*__

#### 1. Geometric Method(기하하적 방법)
- 링크와 조인트의 위치를 직접 계산
	->계산이 간단하고 시각적 직관이 강함
	->복잡한 구조에서는 활용이 어려움


베이스부터 조인트 끝단까지 어떻게 구하는지 학습
N개의 조인트가 있을때 x,y,x 로우, 피치, 여값이 어떻게 대응 되는가?
끝단을 계산하는 방법 (엔드팩터 값을 알고싶을 떄)
#### 2. Denavit-Hartenberg Method (DH 파라미터)
- 4개의 파라미터(d, Θ, r, α)로 활용해서 특단의 포워드 매트릭스를 계산한다.
- 결국 끝단을 알아가는 것이 목적
- 각 링크 간 변환을 4 x 4 행렬로 표현
- 표준화된 알고리즘
- 프레임 설정이 까다로움
## 3. 역기구학
### 역기구학 (Inverse Kinematics)
__position *p = [x, y, z, ...]* -> (Inverse kinematics) -> Joint값 *q = [q1, q2, q3 ... ]*__
#### 1. Analytical Method(해석적 방법)
- 링크와 조인트의 위치를 직접 계산
	-> 시각적 지관이 강함
	-> 복잡한 구조에서는 활용이 어려움
#### 2. Numerical Method(수치적 방법)
- 반복적으로 수치적 근사(approximate)(오차가 작아질 때까지 반복해서 오차가 0으로 갈때까지 계산을 하는 근사값을 찾아서 계산하는 방법) = > __Jacobian__
- Jacobian을 활용한 문제해결
	- 핵심키워드는 변화량. 변화량이 굉장히 중요함
	    - 변화량이 얼마나 되는지 궁금함
	    - 끝단이 얼마큼 변화되는 건지 궁금함
	    - A값(조인트 값)이 변할때 얼마나 변화하는가(변화량)
	    - 포지션의 변화(x,y,,감마)가 궁금하다.
	    - Q값이 변할때 x,y,감마값이 얼마나 변할지 궁금함
	- 얼마큼 영향을 주는지 궁금함
	    - 행으로 볼때 어떤 영향을 주는지
	    - 열로 볼때 어떤 영향을 주는지
	- 델타 p를 알게되면 q를 알 수 있음
	    - 역으로 추산하면 자코비언을 알면 p를 알 수 있음
	    - 관절값이 완벽하게 원하는 값이 되지 않을 수 있다.

<수치적 방법 순서>
1. 초기 추정값 설정
2. 현재 위치 계산
3. 오차 벡터 계싼
4. 자코비안을 통해 보정값 계산
5. 관절값 업데이트
6. 오차가 작아질 때까지 반복
	-> 2번에서 5번 계속 반복

## 4. 강의 요약

- Forward Kinematics
	- 기하하적 기법
	- DH 파라미터 기법
- Inverse Kinematics
	- 해석적 기법
	- 수치적 기법
- jacobian
	- 변화량이 중요!!
- pick & place
	- IK를 활용하여 pick & place 문제의 goal state로 정의

# Chapter 4. 로봇 동역학

## 1. 동역학 개요
- **동역학(Dynamics)** 이란,  
	물체의 **운동(motion)** 과 그 운동을 **일으키는 힘(force)** 의 관계를 다루는 **역학(mechanics)** 의 한 분야입니다.
	
	- 정역학(Statics): **힘은 존재하지만 물체는 정지**하거나 **등속운동**을 하는 경우를 다룸.    
	- **동역학(Dynamics):** **힘에 의해 운동 상태가 변하는 경우**, 즉 **가속도(acceleration)** 가 생기는 운동을 다룸.
	- 기구학: 위치, 속도, 가속도만 고려
	- 동역학: 힘, 토크까지 고려 -> 물리법칙 포함
## 2. 동역학
### 로봇 동역학
제약 조건(Constraints):
1. 로봇의 특성에 따라 __최대속도__ , __최대 조향각__ 
2. 작업의 특성에 따라 __안전거리__ , __안전 속도__

- 위치와 관련된 것 뿐만아니라 링크들의 물리 법칙 특성들을 모두 파악해서 힘을 포함함
- 조인트들의 무게에 따라서 모터가 얼마나 세게 움직여야 되는건지 파악해야 함
    - 그러기 위해서 로봇의 상태를 정의하는 것이 굉장히 중요함
    - 로봇이 빠르게 움직이는지, 느리게 움직이는지 포하매야지 로봇을 완전히 정의할 수 있음
    - 인풋에 따라서 시스템의 변화량이 중요함
        - X = f(x,u)
- 모터가 얼만큼의 힘이 나오는지 조건, 즉 Plant dynamics들이 제공되었다는 가정하에
- 로봇 청소기 상태 정의
    - X,y값
    - 로봇이 얼마나 회전했는지, 세타
    - 로봇이 실제로 얼마나 빠르게 움직이는지 선형적인 값 v
    - 각의 각도로 얼마나 빠르게 회전하고 있는지 각속도 값
    - 왼쪽 바퀴, 오른쪽 바퀴 힘(컨트롤 인풋)
- 상태와 힘과의 관계를 파악하는 것이 중요함
    - F=ma 와 T(힘) = I(가속도) ⇒ 가속도 를 활용
- 이전 링크가 다음 링크의 상태를 결정함(연쇄 작용) 이 있는 조금 더 복잡한 형태의 로봇 동역학
- 토크들의 힘에 따라 로봇의 상태가 정의할 수 있음
    - Mass: 관절을 가속시키는 토크=힘
    - C: 회전 관성 및 원심력에 맞서는 토크
    - g: 중력에 맞서는 토크
- 링크들의 연쇄작용을 알 수 있게 하는게 Urdf임
- 동역학적인 식은 시뮬레이션으로 볼 수 있는 것을 urdf로 확인할 수 있음

## 3. 동역학 요약
### 기구학/동역학 요약
- 기구학은 단순히 속도, 가속도, 포지션
- 동역학은 힘과 관련된 것까지 파악
- 로봇상태는 동영상처럼 현재 로봇이 얼마큼 빠르게 움직이는지 파악하는 것이 중요하고 이를 바탕으로 로봇의 상태를 정의할 수 있음

## **환경 구성요소**

**장애물** Obstacle

로봇의 움직임을 방해하는 모든 물체나 제약조건. 

**Broad Phase** - 절대 충돌할 리 없는 쌍을 빠르게 걸러내는 단계. 복잡한 물체를 단순한 경계 볼륨으로 감싸고, 이 볼륨끼리 겹치는지 먼저 확인함. 볼륨이 겹치지 않으면 세부 검사를 생략함. 

**Narrow Phase** - Broad Phase에서 걸러지지 않은 쌍들에 대해 실제로 충돌하는지 정밀하게 판단하는 단계. 물체를 수많은 작은 블록의 집합으로 보고, 이 블록 쌍들이 서로 닿는지 일일이 검사함. 계산량이 많지만 정확함. 

**공간 해상도** Spatial Resolution

로봇이 움직이는 공간을 얼마나 잘게 쪼개서 볼 것인가를 나타내는 척도.

높 - 더 정확한 경로를 찾을 수 있지만 계산량이 증가함.

낮 - 계산은 빠르지만 경로 정확도가 떨어지거나 충돌 가능성이 생김.

**시간 해상도** Time Resolution

로봇의 움직임을 시간적으로 얼마나 잘게 쪼개서 계산할 것인가를 나타내는 척도.

높 - 더 정확한 경로를 찾을 수 있지만 계산량이 증가함.

낮 - 계산은 빠르지만 경로 정확도가 떨어지거나 충돌 가능성이 생김.

## **환경 해석 방법**

**Offline**

로봇이 움직이기 전에 이미 알고 있는 정보를 바탕으로 경로를 계획함. 환경 전체를 미리 알고 있어 최적의 경로를 찾기 쉽고 실시간 계산 부담이 적지만, 실시간 대응이 어려움. 

**Online**

카메라, 라이다 등 센서 정보를 이용해 실시간으로 주변 환경을 파악하며 경로를 계획함. 동적인 환경에서도 충돌을 회피하며 움직일 수 있지만, 전체 최적 경로를 찾기 어렵고 실시간 계산 비용이 큼.
# Chapter 5. URDF 와 미니 실습

## 1. 개요

기본 점검 사항 
- Ubuntu 24.04
- Visual Code
- Git

## 2. 깃클론

여기 저장소 깃클론
https://github.com/Daniella1/urdf_files_dataset 
## 3. urdf  분석
### URDF(Universal Robot Description Format)

• 로봇의 구조를 컴퓨터가 이해할 수 있게 XML 형태로 기술한 설계도임.  
• 온라인에서 시각화해서 바로 볼 수 있음

- Robot urdf viewer: 로봇이 어떻게 생겼는지 확인하는데 유용함

#### 주요 구성요소

• link: 물리적 부품 정의  
• joint: 링크 간의 연결과 자유도 정의  
• transmission: 구동계(모터, 기어비 등) 정보  
• 시뮬레이션(RViz, Gazebo) 및 물리 엔진에서 로봇 모델링의 기본이 됨.




```xml
<?xml version="1.0" ?>

<!-- =================================================================================== -->

<!-- | This document was autogenerated by xacro from ur5e.xacro | -->

<!-- | EDITING THIS FILE BY HAND IS NOT RECOMMENDED | -->

<!-- =================================================================================== -->

<robot name="ur5e_robot">

<!--

Base UR robot series xacro macro.

  

NOTE: this is NOT a URDF. It cannot directly be loaded by consumers

expecting a flattened '.urdf' file. See the top-level '.xacro' for that

(but note: that .xacro must still be processed by the xacro command).

  

For use in '.launch' files: use one of the 'load_urX.launch' convenience

launch files.

  

This file models the base kinematic chain of a UR robot, which then gets

parameterised by various configuration files to convert it into a UR3(e),

UR5(e), UR10(e) or UR16e.

  

NOTE: the default kinematic parameters (ie: link lengths, frame locations,

offets, etc) do not correspond to any particular robot. They are defaults

only. There WILL be non-zero offsets between the Forward Kinematics results

in TF (ie: robot_state_publisher) and the values reported by the Teach

Pendant.

  

For accurate (and robot-specific) transforms, the 'kinematics_parameters_file'

parameter MUST point to a .yaml file containing the appropriate values for

the targetted robot.

  

If using the UniversalRobots/Universal_Robots_ROS_Driver, follow the steps

described in the readme of that repository to extract the kinematic

calibration from the controller and generate the required .yaml file.

  

Main author of the migration to yaml configs: Ludovic Delval.

  

Contributors to previous versions (in no particular order):

  

- Felix Messmer

- Kelsey Hawkins

- Wim Meeussen

- Shaun Edwards

- Nadia Hammoudeh Garcia

- Dave Hershberger

- G. vd. Hoorn

- Philip Long

- Dave Coleman

- Miguel Prada

- Mathias Luedtke

- Marcel Schnirring

- Felix von Drigalski

- Felix Exner

- Jimmy Da Silva

- Ajit Krisshna N L

- Muhammad Asif Rana

-->

<!--

NOTE: the macro defined in this file is NOT part of the public API of this

package. Users CANNOT rely on this file being available, or stored in

this location. Nor can they rely on the existence of the macro.

-->

<transmission name="shoulder_pan_trans">

<type>transmission_interface/SimpleTransmission</type>

<joint name="shoulder_pan_joint">

<hardwareInterface>hardware_interface/PositionJointInterface</hardwareInterface>

</joint>

<actuator name="shoulder_pan_motor">

<mechanicalReduction>1</mechanicalReduction>

</actuator>

</transmission>

<transmission name="shoulder_lift_trans">

<type>transmission_interface/SimpleTransmission</type>

<joint name="shoulder_lift_joint">

<hardwareInterface>hardware_interface/PositionJointInterface</hardwareInterface>

</joint>

<actuator name="shoulder_lift_motor">

<mechanicalReduction>1</mechanicalReduction>

</actuator>

</transmission>

<transmission name="elbow_trans">

<type>transmission_interface/SimpleTransmission</type>

<joint name="elbow_joint">

<hardwareInterface>hardware_interface/PositionJointInterface</hardwareInterface>

</joint>

<actuator name="elbow_motor">

<mechanicalReduction>1</mechanicalReduction>

</actuator>

</transmission>

<transmission name="wrist_1_trans">

<type>transmission_interface/SimpleTransmission</type>

<joint name="wrist_1_joint">

<hardwareInterface>hardware_interface/PositionJointInterface</hardwareInterface>

</joint>

<actuator name="wrist_1_motor">

<mechanicalReduction>1</mechanicalReduction>

</actuator>

</transmission>

<transmission name="wrist_2_trans">

<type>transmission_interface/SimpleTransmission</type>

<joint name="wrist_2_joint">

<hardwareInterface>hardware_interface/PositionJointInterface</hardwareInterface>

</joint>

<actuator name="wrist_2_motor">

<mechanicalReduction>1</mechanicalReduction>

</actuator>

</transmission>

<transmission name="wrist_3_trans">

<type>transmission_interface/SimpleTransmission</type>

<joint name="wrist_3_joint">

<hardwareInterface>hardware_interface/PositionJointInterface</hardwareInterface>

</joint>

<actuator name="wrist_3_motor">

<mechanicalReduction>1</mechanicalReduction>

</actuator>

</transmission>

---------------------------------------------------
#link의 첫 시작

<!-- links: main serial chain -->

<link name="base_link"/>

<link name="base_link_inertia">

<visual>

<origin rpy="0 0 3.141592653589793" xyz="0 0 0"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/visual/base.dae"/>

</geometry>

<material name="LightGrey">

<color rgba="0.7 0.7 0.7 1.0"/>

</material>

</visual>

<collision>

<origin rpy="0 0 3.141592653589793" xyz="0 0 0"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/collision/base.stl"/>

</geometry>

</collision>

<inertial>

<mass value="4.0"/>

<origin rpy="0 0 0" xyz="0 0 0"/>

<inertia ixx="0.00443333156" ixy="0.0" ixz="0.0" iyy="0.00443333156" iyz="0.0" izz="0.0072"/>

</inertial>

</link>

<link name="shoulder_link">

<visual>

<origin rpy="0 0 3.141592653589793" xyz="0 0 0"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/visual/shoulder.dae"/>

</geometry>

<material name="LightGrey">

<color rgba="0.7 0.7 0.7 1.0"/>

</material>

</visual>

<collision>

<origin rpy="0 0 3.141592653589793" xyz="0 0 0"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/collision/shoulder.stl"/>

</geometry>

</collision>

<inertial>

<mass value="3.7"/>

<origin rpy="0 0 0" xyz="0 0 0"/>

<inertia ixx="0.010267495893" ixy="0.0" ixz="0.0" iyy="0.010267495893" iyz="0.0" izz="0.00666"/>

</inertial>

</link>

<link name="upper_arm_link">

<visual>

<origin rpy="1.5707963267948966 0 -1.5707963267948966" xyz="0 0 0.138"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/visual/upperarm.dae"/>

</geometry>

<material name="LightGrey">

<color rgba="0.7 0.7 0.7 1.0"/>

</material>

</visual>

<collision>

<origin rpy="1.5707963267948966 0 -1.5707963267948966" xyz="0 0 0.138"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/collision/upperarm.stl"/>

</geometry>

</collision>

<inertial>

<mass value="8.393"/>

<origin rpy="0 1.5707963267948966 0" xyz="-0.2125 0.0 0.138"/>

<inertia ixx="0.1338857818623325" ixy="0.0" ixz="0.0" iyy="0.1338857818623325" iyz="0.0" izz="0.0151074"/>

</inertial>

</link>

<link name="forearm_link">

<visual>

<origin rpy="1.5707963267948966 0 -1.5707963267948966" xyz="0 0 0.007"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/visual/forearm.dae"/>

</geometry>

<material name="LightGrey">

<color rgba="0.7 0.7 0.7 1.0"/>

</material>

</visual>

<collision>

<origin rpy="1.5707963267948966 0 -1.5707963267948966" xyz="0 0 0.007"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/collision/forearm.stl"/>

</geometry>

</collision>

<inertial>

<mass value="2.275"/>

<origin rpy="0 1.5707963267948966 0" xyz="-0.1961 0.0 0.007"/>

<inertia ixx="0.031209355099586295" ixy="0.0" ixz="0.0" iyy="0.031209355099586295" iyz="0.0" izz="0.004095"/>

</inertial>

</link>

<link name="wrist_1_link">

<visual>

<!-- TODO: Move this to a parameter -->

<origin rpy="1.5707963267948966 0 0" xyz="0 0 -0.127"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/visual/wrist1.dae"/>

</geometry>

<material name="LightGrey">

<color rgba="0.7 0.7 0.7 1.0"/>

</material>

</visual>

<collision>

<origin rpy="1.5707963267948966 0 0" xyz="0 0 -0.127"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/collision/wrist1.stl"/>

</geometry>

</collision>

<inertial>

<mass value="1.219"/>

<origin rpy="0 0 0" xyz="0 0 0"/>

<inertia ixx="0.0025598989760400002" ixy="0.0" ixz="0.0" iyy="0.0025598989760400002" iyz="0.0" izz="0.0021942"/>

</inertial>

</link>

<link name="wrist_2_link">

<visual>

<origin rpy="0 0 0" xyz="0 0 -0.0997"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/visual/wrist2.dae"/>

</geometry>

<material name="LightGrey">

<color rgba="0.7 0.7 0.7 1.0"/>

</material>

</visual>

<collision>

<origin rpy="0 0 0" xyz="0 0 -0.0997"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/collision/wrist2.stl"/>

</geometry>

</collision>

<inertial>

<mass value="1.219"/>

<origin rpy="0 0 0" xyz="0 0 0"/>

<inertia ixx="0.0025598989760400002" ixy="0.0" ixz="0.0" iyy="0.0025598989760400002" iyz="0.0" izz="0.0021942"/>

</inertial>

</link>

<link name="wrist_3_link">

<visual>

<origin rpy="1.5707963267948966 0 0" xyz="0 0 -0.0989"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/visual/wrist3.dae"/>

</geometry>

<material name="LightGrey">

<color rgba="0.7 0.7 0.7 1.0"/>

</material>

</visual>

<collision>

<origin rpy="1.5707963267948966 0 0" xyz="0 0 -0.0989"/>

<geometry>

<mesh filename="package://ur_description/meshes/ur5e/collision/wrist3.stl"/>

</geometry>

</collision>

<inertial>

<mass value="0.1879"/>

<origin rpy="0 0 0" xyz="0.0 0.0 -0.0229"/>

<inertia ixx="9.890410052167731e-05" ixy="0.0" ixz="0.0" iyy="9.890410052167731e-05" iyz="0.0" izz="0.0001321171875"/>

</inertial>

</link>

<!-- joints: main serial chain -->

<joint name="base_link-base_link_inertia" type="fixed">

<parent link="base_link"/>

<child link="base_link_inertia"/>

<!-- 'base_link' is REP-103 aligned (so X+ forward), while the internal

frames of the robot/controller have X+ pointing backwards.

Use the joint between 'base_link' and 'base_link_inertia' (a dummy

link/frame) to introduce the necessary rotation over Z (of pi rad).

-->

<origin rpy="0 0 3.141592653589793" xyz="0 0 0"/>

</joint>

<joint name="shoulder_pan_joint" type="revolute">

<parent link="base_link_inertia"/>

<child link="shoulder_link"/>

<origin rpy="0 0 0" xyz="0 0 0.1625"/>

<axis xyz="0 0 1"/>

<limit effort="150.0" lower="-6.283185307179586" upper="6.283185307179586" velocity="3.141592653589793"/>

<dynamics damping="0" friction="0"/>

</joint>

<joint name="shoulder_lift_joint" type="revolute">

<parent link="shoulder_link"/>

<child link="upper_arm_link"/>

<origin rpy="1.570796327 0 0" xyz="0 0 0"/>

<axis xyz="0 0 1"/>

<limit effort="150.0" lower="-6.283185307179586" upper="6.283185307179586" velocity="3.141592653589793"/>

<dynamics damping="0" friction="0"/>

</joint>

<joint name="elbow_joint" type="revolute">

<parent link="upper_arm_link"/>

<child link="forearm_link"/>

<origin rpy="0 0 0" xyz="-0.425 0 0"/>

<axis xyz="0 0 1"/>

<limit effort="150.0" lower="-3.141592653589793" upper="3.141592653589793" velocity="3.141592653589793"/>

<dynamics damping="0" friction="0"/>

</joint>

<joint name="wrist_1_joint" type="revolute">

<parent link="forearm_link"/>

<child link="wrist_1_link"/>

<origin rpy="0 0 0" xyz="-0.3922 0 0.1333"/>

<axis xyz="0 0 1"/>

<limit effort="28.0" lower="-6.283185307179586" upper="6.283185307179586" velocity="3.141592653589793"/>

<dynamics damping="0" friction="0"/>

</joint>

<joint name="wrist_2_joint" type="revolute">

<parent link="wrist_1_link"/>

<child link="wrist_2_link"/>

<origin rpy="1.570796327 0 0" xyz="0 -0.0997 -2.044881182297852e-11"/>

<axis xyz="0 0 1"/>

<limit effort="28.0" lower="-6.283185307179586" upper="6.283185307179586" velocity="3.141592653589793"/>

<dynamics damping="0" friction="0"/>

</joint>

<joint name="wrist_3_joint" type="revolute">

<parent link="wrist_2_link"/>

<child link="wrist_3_link"/>

<origin rpy="1.570796326589793 3.141592653589793 3.141592653589793" xyz="0 0.0996 -2.042830148012698e-11"/>

<axis xyz="0 0 1"/>

<limit effort="28.0" lower="-6.283185307179586" upper="6.283185307179586" velocity="3.141592653589793"/>

<dynamics damping="0" friction="0"/>

</joint>

<!-- ROS-Industrial 'base' frame: base_link to UR 'Base' Coordinates transform -->

<link name="base"/>

<joint name="base_link-base_fixed_joint" type="fixed">

<!-- Note the rotation over Z of pi radians: as base_link is REP-103

aligned (ie: has X+ forward, Y+ left and Z+ up), this is needed

to correctly align 'base' with the 'Base' coordinate system of

the UR controller.

-->

<origin rpy="0 0 3.141592653589793" xyz="0 0 0"/>

<parent link="base_link"/>

<child link="base"/>

</joint>

<!-- ROS-Industrial 'flange' frame: attachment point for EEF models -->

<link name="flange"/>

<joint name="wrist_3-flange" type="fixed">

<parent link="wrist_3_link"/>

<child link="flange"/>

<origin rpy="0 -1.5707963267948966 -1.5707963267948966" xyz="0 0 0"/>

</joint>

<!-- ROS-Industrial 'tool0' frame: all-zeros tool frame -->

<link name="tool0"/>

<joint name="flange-tool0" type="fixed">

<!-- default toolframe: X+ left, Y+ up, Z+ front -->

<origin rpy="1.5707963267948966 0 1.5707963267948966" xyz="0 0 0"/>

<parent link="flange"/>

<child link="tool0"/>

</joint>

</robot>
```
## 4. 매쉬

## 5. 온라인툴 소개

## 6. 시각화툴 활용

## 7. 로봇팔 시각화

# Chapter 6.  환경 - 격자도와 로드 맵

## 1. 이전 강의 요약

## 2. 장애물과 충돌검출

## 3. 브로드내로페이즈

## 4. 공간해상도

## 5. 시간해상도

## 6. 예시

## 7. 온라인 오프라인

## 8. 그리드로드맵

## 9. 강의 요약





