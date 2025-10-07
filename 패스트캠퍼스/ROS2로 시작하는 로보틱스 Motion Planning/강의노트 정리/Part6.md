
# Chapter 1. ROS2 개요

## 1. ROS2개요
- *AGV(바퀴 4개 달린 자동차)*
1. Task Description
	- 네비게이션
2. Perception
	- 카메라, 라이다
	- Encoder
	- IMU
3. Planning
	- 경로 계획
4. Control
	- 로봇 구동
	- 외란(미끄럼)의 작용

- *다리 4개 달린 강아지 로봇*
1. Task Description
	- 네비게이션
	- 걷기, 뛰기
2. Perception
	- 카메라, 라이다
	- Encoder
	- IMU
3. Planning
	- 경로 계획(dynamics & kinematics)
4. Control
	- 로봇 구동
	- 외란(미끄럼)의 작용

- *3축 로봇암*
1. Task Description
	- 네비게이션
	- 걷기, 뛰기
	- 물체를 집어 올리기
2. Perception
	- 카메라 -> 외부 카메라를 통해 상황 파악하는 경우가 많음
	- Encoder
3. Planning
	- 경로 계획(dynamics & kinematics)
	- 모션 플래닝
4. Control
	- 로봇 구동
	- 외란(미끄럼)의 작용

- *휴머노이드 로봇*
1. Task Description
	- 네비게이션
	- 걷기, 뛰기
	- 물체를 집어 올리기
2. Perception
	- 카메라, 라이다
	- Encoder
	- 촉각 센서
	- IMU
3. Planning
	- 경로 계획(dynamics & kinematics)
	- 모션 플래닝
4. Control
	- 로봇 구동
	- 외란(미끄럼)의 작용
	- 사람과의 상호작용

## 2. ROS2의 필요성
1. Task Description
	- 네비게이션
	- 걷기, 뛰기
	- 물체를 집어 올리기
__-> 외부에서 주어짐__

2. Perception
	- 카메라, 라이다
	- Encoder
	- 촉각 센서
	- IMU
3. Planning
	- 경로 계획(dynamics & kinematics)
	- 모션 플래닝
4. Control -> PID 제어를 많이 사용
	- 로봇 구동
	- 외란(미끄럼)의 작용
	- 사람과의 상호작용
__-> 상황에 맞게 변형
- 센서의 종류, 알고리즘의 종류, 컨트롤러의 종류
- 고려할 사항이 매우 많고 구현이 어려움



## 3. ROS2의 필요성2
1. 센서
	- 카메라 패키지
	- 라이다 패키지
	- IMU 패키지
2. 플래닝 알고리즘
	- 서치 알고리즘
	- 모션 프래닝 알고리즘
	- 경로 계획 알고리즘
	- 네비게이션 알고리즘
3. 필터링 알고리즘
	- 몬테 카를로
	- 칼만 필터

__-> ROS가 여러 패키지를 한번에 모아서 사용할 수 있게 해준다.__


- 하드웨어와 소프트웨어를 모듈화하고 연결하는 미들웨어
- 복잡한 로봇 제어 시스템을 구성 가능하게 해주는 프레임워크
- 기업(개인)과의 협업
- 패키지 확장성

1. 제조사 제공 드라이버
	- 복잡한 low-level 소프트웨어
2. ROS 플랫 폼
	- movite2, nav2, driver
3. 사용이 편리한 high-level 소프트웨어
4. Head

## 4. ROS2 특징

### ROS1 ROS2 차이점
- ROS1
	-  중앙 집중형: 병령 처리의 한계 존재
	- 신시간성 부족: 제어 주기를 맞추기 어려움(TCPROS)
	- 다양한 로봇을 위한 환경 구성의 어려움: IP 설정, 로봇 ID 수작업 등
	- XML 기반 실행

- ROS2
	-  중앙 집중형: 병령 처리의 한계 존재 -> __병렬 구조__
	- 신시간성 부족: 제어 주기를 맞추기 어려움(TCPROS)->  __우선순위 기반, 시간 제약 고려한 통신(RTOS)
	- 다양한 로봇을 위한 환경 구성의 어려움: IP 설정, 로봇 ID 수작업 등 -> __로봇 ID 작업 자동화__
	- XML 기반 실행 -> __Python 기반 실행__

## 5. 마무리
1. ROS의 특징 및 필요성
	- 하드웨어와 소프트웨어 모듈화 및 연결
	- 기업과의 협업
2. ROS1 vs ROS2
	- 구조
	- 실시간성
	- 로봇 ID
	- PYTHON 기반

# Chapter 2. ROS2 기본 개념
## 1, 2, 3. ROS2 개념
![](https://miro.medium.com/v2/resize:fit:1400/0*aNw-2q1Azw5QpAuN.gif)

- 노드 (Node)
    - ROS2에서 실행되는 프로그램의 최소 단위
    - 노드끼리는 서로 통신하면서 협업
    - 메시지를 주고 받으면서 상호작용을 함
        
- 토픽 (Topic)
    - 노드끼리 데이터를 주고받는 __채널__ 같은 것
    - __서비스와 다르게 계속해서 신호를 보냄__
        
- 메시지 (Message)
    - 통신의 기본 단위
    - 토픽에 실려 나르는 데이터의 형식 -> Structure 정의
    - Publish–Subscribe 방식
        - 퍼블리셔 노드(Publisher node) : 데이터를 보냄.
			->방송국에 정보를 보냄!
        - 서브스크라이버 노드(Subscriber node) : 데이터를 받음.
			->방송국에서 정보를 받고 있음!
        
- 서비스 (Service)
    - 정보 요청(Request) - 응답 구조(Response)
    - Server와  Client가 있음
    - __필요할 때만 보내는 단발성 통신__ , 짧고 즉각적인 통신에 적합
    - 진행상황을 알 수 없고 취소 불가능

- 파라미터(Parameter)
    - ROS2 노드 내부에서 사용하는 전역적인 설정 값
    - 토픽 메시지처럼 계속 주고받는 데이터가 아니라 한 번 설정해두고 노드 실행 중에 참조
    - 각 노드들에 필요한 중요 정보
        
- 액션(Action)
    - 서비스와 비슷하지만 시간이 오래 걸리는 작업에 특화
    - Server와 Client가 있음
    - __진행상황을 알 수 있고 취소 가능__
    - 흐름 : Goal -> Feedback -> Result

![](https://docs.ros.org/en/rolling/_images/Action-SingleActionClient.gif)


## 4. ROS2 패키지 및 워크스페이스
- 패키지(Package)
    - 기능별 프로젝트를 관리하는 폴더
    - 기능 통합, 분리 등 단위에 제약이 없음
        
	- Package (Python)
		![[스크린샷 2025-10-04 오후 9.17.18.png]]
	        - package.xml : 패키지 정보
	        - setup.py : Python 모듈로 설정하기 위한 스크립트
	        - setup.cfg : setup.py 보조파일
	        - resource/my_robot_pkg : 패키지 리소스 관리
	        - my_robot_pkg/_init_.py : Python 패키지로 인식하기 위한 설정 파일
	        - launch : 패키지 실행 파일
	            
	- Package (C++)
		![[스크린샷 2025-10-04 오후 9.17.26.png]]
	        - CMakeLists.txt : C++ 핵심 빌드 설정 파일
	        - package.xml : 패키지 정보
	        - include : C++ 헤더파일
	        - src : 사용자가 작성한 실행코드
	        - launch : 패키지 실행 파일

		- 워크 스페이스 (Workspace)
		![[스크린샷 2025-10-04 오후 9.17.37.png]]
		    - ROS2 전체 프로젝트 구조
		        - ros2_ws : 워크스페이스 최상단
		        - src : 패키지를 포함하는 폴더
		        - 패키지
		        - install : 빌드된 실행 파일(빌드 결과물)
		        - build : 중간 빌드 결과물


[[ROS 명령어]]


# Chapter 3. ROS2 기본 개념 학습

## 1. 강의 개요
- turtle Sim을 활용해서 실습시작!
## 2. ROS2 설치
- [[ROS 명령어]]
## 3. turtlesim 설치
- [[ROS 명령어]]
## 4. node

## 5. rqt

## 6. topic

## 7. publish

## 8. 중간점검

## 9. service

## 10. parameter 도입부

## 11. parameter

## 12. action

## 13. 중간점검2

##  14. 마무리


# Chapter 4. ROS2 패키지 분석2

## 1. 패키지 개요

## 2. Robot Description
#### **my_robot_description**

로봇의 외형과 구조를 정의하는 패키지. 

**URDF** - 로봇의 기구학적 구조를 정의하는 파일

**Mesh** - 로봇의 3D 모델링 파일

**Launch** - URDF를 ROS2 시스템에 로드하는 **robot_state_publisher** 노드를 실행함


## 3. driver
#### **my_robot_driver**

ROS2 시스템과 실제 로봇 하드웨어를 연결하는 역할. 

**ROS2 명령어 -> 하드웨어 제어** - 표준 명령어를 받아서 모터 제어기가 알아들을 수 있는 저수준 신호로 변환

**하드웨어 센서값 -> ROS2 메시지** - 바퀴 엔코더 값이나 IMU 센서 데이터를 읽어서 표준 메시지로 변환하고 발행

#### **my_robot_bringup**

로봇을 구동하는 데 필요한 모든 노드를 한 번에 실행하는 역할. 대부분 launch 파일로만 이루어져 있음.

## 4. driver Repository

## 5. 추가 패키지
## **확장 패키지**

**gazebo_ros** - 시뮬레이션

**moveit2** - 모션 플래닝 / 로봇팔의 경로를 계획하고 충돌을 회피하는 기능을 제공함

**nav2** - 자율주행 / SLAM으로 지도를 만들고, 목적지까지 스스로 경로를 탐색하여 이동하는 기능을 제공함

**rviz2** - 3D 시각화 / 현재 상태, 센서 데이터, 경로 계획 등을 3D 환경에서 직관적으로 보여줌


## 6. Gitub Respository

## 7. Gitub Respository2

## 8. Build 예시

## 9. Build 예시2

## 10. 마무리






# Chapter 5. Xacro 개요
## 1. Xacro  개요
URDF
- 로봇의 정보를 모두 담고 있는 파일 형식
- Rviz2 에서 시각화 및 Gazebo 에서 시뮬레이션에 활용
- 대표 구성요소
	-  Link
	- Joint
	- Inertial
	- Collision
	- Transmission
	- Material

Xacro
- 로봇의 확장성을 위해 만들어진 파일 형식
- 기본적으로 URDF형식을 따름
- URD를 하나의 함수로 설정하는 것과 유사
	- 변수 사용, 반복문, 조건문, 매크로 함수 정의 등이 가능

로봇1에 다른 로봇2를 추가하고 싶을 때 
파이썬 처럼 함수를 불러온 후 파라미터를 변경해주는 식으로 합쳐준다.


## 2. 예시
### <ur_macro.xacro>
```xml
<?xml version="1.0"?>

<robot xmlns:xacro="http://wiki.ros.org/xacro">

<!--

Base UR robot series xacro macro.

  

NOTE this is NOT a URDF. It cannot directly be loaded by consumers

expecting a flattened '.urdf' file. See the top-level '.xacro' for that

(but note that .xacro must still be processed by the xacro command).

  

This file models the base kinematic chain of a UR robot, which then gets

parameterised by various configuration files to convert it into a UR3(e),

UR5(e), UR10(e) or UR16e.

  

NOTE the default kinematic parameters (i.e., link lengths, frame locations,

offsets, etc) do not correspond to any particular robot. They are defaults

only. There WILL be non-zero offsets between the Forward Kinematics results

in TF (i.e., robot_state_publisher) and the values reported by the Teach

Pendant.

  

For accurate (and robot-specific) transforms, the 'kinematics_parameters_file'

parameter MUST point to a .yaml file containing the appropriate values for

the targeted robot.

  

If using the UniversalRobots/Universal_Robots_ROS_Driver, follow the steps

described in the readme of that repository to extract the kinematic

calibration from the controller and generate the required .yaml file.

  

Main author of the migration to yaml configs Ludovic Delval.

  

Contributors to previous versions (in no particular order)

  

- Denis Stogl

- Lovro Ivanov

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

  

<xacro:include filename="$(find ur_description)/urdf/inc/ur_common.xacro" />

  
<!-- xacro: macro => 앞에서 로봇의 base 구성하는 부분을 ur_robot으로 불러옴 -->
<xacro:macro name="ur_robot" params="

name
tf_prefix
parent
*origin
joint_limits_parameters_file
kinematics_parameters_file
physical_parameters_file
visual_parameters_file
safety_limits:=false
safety_pos_margin:=0.15
safety_k_position:=20
force_abs_paths:=false
">

  

<!-- Load configuration data from the provided .yaml files -->

<xacro:read_model_data

joint_limits_parameters_file="${joint_limits_parameters_file}"

kinematics_parameters_file="${kinematics_parameters_file}"

physical_parameters_file="${physical_parameters_file}"

visual_parameters_file="${visual_parameters_file}"

force_abs_paths="${force_abs_paths}"/>

  

<!-- links - main serial chain -->

<link name="${tf_prefix}base_link"/>

<link name="${tf_prefix}base_link_inertia">

<visual>

<origin xyz="0 0 0" rpy="0 0 ${pi}"/>

<geometry>

<xacro:get_mesh name="base" type="visual"/>

</geometry>

</visual>

<collision>

<origin xyz="0 0 0" rpy="0 0 ${pi}"/>

<geometry>

<xacro:get_mesh name="base" type="collision"/>

</geometry>

</collision>

<xacro:cylinder_inertial radius="${base_inertia_radius}" length="${base_inertia_length}" mass="${base_mass}">

<origin xyz="0 0 0" rpy="0 0 0" />

</xacro:cylinder_inertial>

</link>

<link name="${tf_prefix}shoulder_link">

<visual>

<origin xyz="0 0 0" rpy="0 0 ${pi}"/>

<geometry>

<xacro:get_mesh name="shoulder" type="visual"/>

</geometry>

</visual>

<collision>

<origin xyz="0 0 0" rpy="0 0 ${pi}"/>

<geometry>

<xacro:get_mesh name="shoulder" type="collision"/>

</geometry>

</collision>

<inertial>

<mass value="${shoulder_mass}"/>

<origin rpy="${shoulder_inertia_rotation}" xyz="${shoulder_cog}"/>

<inertia

ixx="${shoulder_inertia_ixx}"

ixy="${shoulder_inertia_ixy}"

ixz="${shoulder_inertia_ixz}"

iyy="${shoulder_inertia_iyy}"

iyz="${shoulder_inertia_iyz}"

izz="${shoulder_inertia_izz}"

/>

</inertial> </link>

<link name="${tf_prefix}upper_arm_link">

<visual>

<origin xyz="0 0 ${shoulder_offset}" rpy="${pi/2} 0 ${-pi/2}"/>

<geometry>

<xacro:get_mesh name="upper_arm" type="visual"/>

</geometry>

</visual>

<collision>

<origin xyz="0 0 ${shoulder_offset}" rpy="${pi/2} 0 ${-pi/2}"/>

<geometry>

<xacro:get_mesh name="upper_arm" type="collision"/>

</geometry>

</collision>

<inertial>

<mass value="${upper_arm_mass}"/>

<origin rpy="${upper_arm_inertia_rotation}" xyz="${upper_arm_cog}"/>

<inertia

ixx="${upper_arm_inertia_ixx}"

ixy="${upper_arm_inertia_ixy}"

ixz="${upper_arm_inertia_ixz}"

iyy="${upper_arm_inertia_iyy}"

iyz="${upper_arm_inertia_iyz}"

izz="${upper_arm_inertia_izz}"

/>

</inertial>

</link>

<link name="${tf_prefix}forearm_link">

<visual>

<origin xyz="0 0 ${elbow_offset}" rpy="${pi/2} 0 ${-pi/2}"/>

<geometry>

<xacro:get_mesh name="forearm" type="visual"/>

</geometry>

</visual>

<collision>

<origin xyz="0 0 ${elbow_offset}" rpy="${pi/2} 0 ${-pi/2}"/>

<geometry>

<xacro:get_mesh name="forearm" type="collision"/>

</geometry>

</collision>

<inertial>

<mass value="${forearm_mass}"/>

<origin rpy="${forearm_inertia_rotation}" xyz="${forearm_cog}"/>

<inertia

ixx="${forearm_inertia_ixx}"

ixy="${forearm_inertia_ixy}"

ixz="${forearm_inertia_ixz}"

iyy="${forearm_inertia_iyy}"

iyz="${forearm_inertia_iyz}"

izz="${forearm_inertia_izz}"

/>

</inertial>

</link>

<link name="${tf_prefix}wrist_1_link">

<xacro:get_visual_params name="wrist_1" type="visual_offset"/>

<visual>

<origin xyz="0 0 ${visual_params}" rpy="${pi/2} 0 0"/>

<geometry>

<xacro:get_mesh name="wrist_1" type="visual"/>

</geometry>

</visual>

<collision>

<origin xyz="0 0 ${visual_params}" rpy="${pi/2} 0 0"/>

<geometry>

<xacro:get_mesh name="wrist_1" type="collision"/>

</geometry>

</collision>

<inertial>

<mass value="${wrist_1_mass}"/>

<origin rpy="${wrist_1_inertia_rotation}" xyz="${wrist_1_cog}"/>

<inertia

ixx="${wrist_1_inertia_ixx}"

ixy="${wrist_1_inertia_ixy}"

ixz="${wrist_1_inertia_ixz}"

iyy="${wrist_1_inertia_iyy}"

iyz="${wrist_1_inertia_iyz}"

izz="${wrist_1_inertia_izz}"

/>

</inertial>

</link>

<link name="${tf_prefix}wrist_2_link">

<xacro:get_visual_params name="wrist_2" type="visual_offset"/>

<visual>

<origin xyz="0 0 ${visual_params}" rpy="0 0 0"/>

<geometry>

<xacro:get_mesh name="wrist_2" type="visual"/>

</geometry>

</visual>

<collision>

<origin xyz="0 0 ${visual_params}" rpy="0 0 0"/>

<geometry>

<xacro:get_mesh name="wrist_2" type="collision"/>

</geometry>

</collision>

<inertial>

<mass value="${wrist_2_mass}"/>

<origin rpy="${wrist_2_inertia_rotation}" xyz="${wrist_2_cog}"/>

<inertia

ixx="${wrist_2_inertia_ixx}"

ixy="${wrist_2_inertia_ixy}"

ixz="${wrist_2_inertia_ixz}"

iyy="${wrist_2_inertia_iyy}"

iyz="${wrist_2_inertia_iyz}"

izz="${wrist_2_inertia_izz}"

/>

</inertial>

</link>

<link name="${tf_prefix}wrist_3_link">

<!-- TODO: remove this once all wrist_3 meshes have the visual_offset_xyz tag -->

<xacro:get_visual_params name="wrist_3" type="visual_offset_xyz"/>

<xacro:property name="mesh_offset" value="${visual_params}" scope="parent"/>

  

<xacro:if value="${visual_params == ''}">

<xacro:get_visual_params name="wrist_3" type="visual_offset"/>

<xacro:property name="mesh_offset" value="0 0 ${visual_params}" scope="parent"/>

</xacro:if>

<visual>

<origin xyz="${mesh_offset}" rpy="${pi/2} 0 0"/>

<geometry>

<xacro:get_mesh name="wrist_3" type="visual"/>

</geometry>

</visual>

<collision>

<origin xyz="${mesh_offset}" rpy="${pi/2} 0 0"/>

<geometry>

<xacro:get_mesh name="wrist_3" type="collision"/>

</geometry>

</collision>

<inertial>

<mass value="${wrist_3_mass}"/>

<origin rpy="${wrist_3_inertia_rotation}" xyz="${wrist_3_cog}"/>

<inertia

ixx="${wrist_3_inertia_ixx}"

ixy="${wrist_3_inertia_ixy}"

ixz="${wrist_3_inertia_ixz}"

iyy="${wrist_3_inertia_iyy}"

iyz="${wrist_3_inertia_iyz}"

izz="${wrist_3_inertia_izz}"

/>

</inertial>

</link>

  

<!-- base_joint fixes base_link to the environment -->

<joint name="${tf_prefix}base_joint" type="fixed">

<xacro:insert_block name="origin" />

<parent link="${parent}" />

<child link="${tf_prefix}base_link" />

</joint>

  

<!-- joints - main serial chain -->

<joint name="${tf_prefix}base_link-base_link_inertia" type="fixed">

<parent link="${tf_prefix}base_link" />

<child link="${tf_prefix}base_link_inertia" />

<!-- 'base_link' is REP-103 aligned (so X+ forward), while the internal

frames of the robot/controller have X+ pointing backwards.

Use the joint between 'base_link' and 'base_link_inertia' (a dummy

link/frame) to introduce the necessary rotation over Z (of pi rad).

-->

<origin xyz="0 0 0" rpy="0 0 ${pi}" />

</joint>

<joint name="${tf_prefix}shoulder_pan_joint" type="revolute">

<parent link="${tf_prefix}base_link_inertia" />

<child link="${tf_prefix}shoulder_link" />

<origin xyz="${shoulder_x} ${shoulder_y} ${shoulder_z}" rpy="${shoulder_roll} ${shoulder_pitch} ${shoulder_yaw}" />

<axis xyz="0 0 1" />

<limit lower="${shoulder_pan_lower_limit}" upper="${shoulder_pan_upper_limit}"

effort="${shoulder_pan_effort_limit}" velocity="${shoulder_pan_velocity_limit}"/>

<xacro:if value="${safety_limits}">

<safety_controller soft_lower_limit="${shoulder_pan_lower_limit + safety_pos_margin}" soft_upper_limit="${shoulder_pan_upper_limit - safety_pos_margin}" k_position="${safety_k_position}" k_velocity="0.0"/>

</xacro:if>

<dynamics damping="0" friction="0"/>

</joint>

<joint name="${tf_prefix}shoulder_lift_joint" type="revolute">

<parent link="${tf_prefix}shoulder_link" />

<child link="${tf_prefix}upper_arm_link" />

<origin xyz="${upper_arm_x} ${upper_arm_y} ${upper_arm_z}" rpy="${upper_arm_roll} ${upper_arm_pitch} ${upper_arm_yaw}" />

<axis xyz="0 0 1" />

<limit lower="${shoulder_lift_lower_limit}" upper="${shoulder_lift_upper_limit}"

effort="${shoulder_lift_effort_limit}" velocity="${shoulder_lift_velocity_limit}"/>

<xacro:if value="${safety_limits}">

<safety_controller soft_lower_limit="${shoulder_lift_lower_limit + safety_pos_margin}" soft_upper_limit="${shoulder_lift_upper_limit - safety_pos_margin}" k_position="${safety_k_position}" k_velocity="0.0"/>

</xacro:if>

<dynamics damping="0" friction="0"/>

</joint>

<joint name="${tf_prefix}elbow_joint" type="revolute">

<parent link="${tf_prefix}upper_arm_link" />

<child link="${tf_prefix}forearm_link" />

<origin xyz="${forearm_x} ${forearm_y} ${forearm_z}" rpy="${forearm_roll} ${forearm_pitch} ${forearm_yaw}" />

<axis xyz="0 0 1" />

<limit lower="${elbow_joint_lower_limit}" upper="${elbow_joint_upper_limit}"

effort="${elbow_joint_effort_limit}" velocity="${elbow_joint_velocity_limit}"/>

<xacro:if value="${safety_limits}">

<safety_controller soft_lower_limit="${elbow_joint_lower_limit + safety_pos_margin}" soft_upper_limit="${elbow_joint_upper_limit - safety_pos_margin}" k_position="${safety_k_position}" k_velocity="0.0"/>

</xacro:if>

<dynamics damping="0" friction="0"/>

</joint>

<joint name="${tf_prefix}wrist_1_joint" type="revolute">

<parent link="${tf_prefix}forearm_link" />

<child link="${tf_prefix}wrist_1_link" />

<origin xyz="${wrist_1_x} ${wrist_1_y} ${wrist_1_z}" rpy="${wrist_1_roll} ${wrist_1_pitch} ${wrist_1_yaw}" />

<axis xyz="0 0 1" />

<limit lower="${wrist_1_lower_limit}" upper="${wrist_1_upper_limit}"

effort="${wrist_1_effort_limit}" velocity="${wrist_1_velocity_limit}"/>

<xacro:if value="${safety_limits}">

<safety_controller soft_lower_limit="${wrist_1_lower_limit + safety_pos_margin}" soft_upper_limit="${wrist_1_upper_limit - safety_pos_margin}" k_position="${safety_k_position}" k_velocity="0.0"/>

</xacro:if>

<dynamics damping="0" friction="0"/>

</joint>

<joint name="${tf_prefix}wrist_2_joint" type="revolute">

<parent link="${tf_prefix}wrist_1_link" />

<child link="${tf_prefix}wrist_2_link" />

<origin xyz="${wrist_2_x} ${wrist_2_y} ${wrist_2_z}" rpy="${wrist_2_roll} ${wrist_2_pitch} ${wrist_2_yaw}" />

<axis xyz="0 0 1" />

<limit lower="${wrist_2_lower_limit}" upper="${wrist_2_upper_limit}"

effort="${wrist_2_effort_limit}" velocity="${wrist_2_velocity_limit}"/>

<xacro:if value="${safety_limits}">

<safety_controller soft_lower_limit="${wrist_2_lower_limit + safety_pos_margin}" soft_upper_limit="${wrist_2_upper_limit - safety_pos_margin}" k_position="${safety_k_position}" k_velocity="0.0"/>

</xacro:if>

<dynamics damping="0" friction="0"/>

</joint>

<joint name="${tf_prefix}wrist_3_joint" type="${wrist_3_joint_type}">

<parent link="${tf_prefix}wrist_2_link" />

<child link="${tf_prefix}wrist_3_link" />

<origin xyz="${wrist_3_x} ${wrist_3_y} ${wrist_3_z}" rpy="${wrist_3_roll} ${wrist_3_pitch} ${wrist_3_yaw}" />

<axis xyz="0 0 1" />

<xacro:if value="${wrist_3_joint_type != 'continuous'}">

<limit lower="${wrist_3_lower_limit}" upper="${wrist_3_upper_limit}"

effort="${wrist_3_effort_limit}" velocity="${wrist_3_velocity_limit}"/>

<xacro:if value="${safety_limits}">

<safety_controller soft_lower_limit="${wrist_3_lower_limit + safety_pos_margin}" soft_upper_limit="${wrist_3_upper_limit - safety_pos_margin}" k_position="${safety_k_position}" k_velocity="0.0"/>

</xacro:if>

</xacro:if>

<xacro:unless value="${wrist_3_joint_type != 'continuous'}">

<limit effort="${wrist_3_effort_limit}" velocity="${wrist_3_velocity_limit}"/>

<xacro:if value="${safety_limits}">

<safety_controller k_position="${safety_k_position}" k_velocity="0.0"/>

</xacro:if>

</xacro:unless>

<dynamics damping="0" friction="0"/>

</joint>

  

<link name="${tf_prefix}ft_frame"/>

<joint name="${tf_prefix}wrist_3_link-ft_frame" type="fixed">

<parent link="${tf_prefix}wrist_3_link"/>

<child link="${tf_prefix}ft_frame"/>

<origin xyz="0 0 0" rpy="${pi} 0 0"/>

</joint>

  

<!-- ROS-Industrial 'base' frame - base_link to UR 'Base' Coordinates transform -->

<link name="${tf_prefix}base"/>

<joint name="${tf_prefix}base_link-base_fixed_joint" type="fixed">

<!-- Note the rotation over Z of pi radians - as base_link is REP-103

aligned (i.e., has X+ forward, Y+ left and Z+ up), this is needed

to correctly align 'base' with the 'Base' coordinate system of

the UR controller.

-->

<origin xyz="0 0 0" rpy="0 0 ${pi}"/>

<parent link="${tf_prefix}base_link"/>

<child link="${tf_prefix}base"/>

</joint>

  

<!-- ROS-Industrial 'flange' frame - attachment point for EEF models -->

<link name="${tf_prefix}flange" />

<joint name="${tf_prefix}wrist_3-flange" type="fixed">

<parent link="${tf_prefix}wrist_3_link" />

<child link="${tf_prefix}flange" />

<origin xyz="0 0 0" rpy="0 ${-pi/2.0} ${-pi/2.0}" />

</joint>

  

<!-- ROS-Industrial 'tool0' frame - all-zeros tool frame -->

<link name="${tf_prefix}tool0"/>

<joint name="${tf_prefix}flange-tool0" type="fixed">

<!-- default toolframe - X+ left, Y+ up, Z+ front -->

<origin xyz="0 0 0" rpy="${pi/2.0} 0 ${pi/2.0}"/>

<parent link="${tf_prefix}flange"/>

<child link="${tf_prefix}tool0"/>

</joint>

  

</xacro:macro>

</robot>
```

### <ur.urdf.xacro>
```xml
<?xml version="1.0"?>

<robot xmlns:xacro="http://wiki.ros.org/xacro" name="$(arg name)">

<!-- robot name parameter -->

<xacro:arg name="name" default="ur"/>

<!-- import main macro -->

<xacro:include filename="$(find ur_description)/urdf/ur_macro.xacro"/>

  

<!-- possible 'ur_type' values: ur3, ur3e, ur5, ur5e, ur10, ur10e, ur16e, ur20, ur30 -->

<!-- the default value should raise an error in case this was called without defining the type -->

<xacro:arg name="ur_type" default="ur5x"/>

  

<!-- parameters -->

<xacro:arg name="tf_prefix" default="" />

<xacro:arg name="joint_limit_params" default="$(find ur_description)/config/$(arg ur_type)/joint_limits.yaml"/>

<xacro:arg name="kinematics_params" default="$(find ur_description)/config/$(arg ur_type)/default_kinematics.yaml"/>

<xacro:arg name="physical_params" default="$(find ur_description)/config/$(arg ur_type)/physical_parameters.yaml"/>

<xacro:arg name="visual_params" default="$(find ur_description)/config/$(arg ur_type)/visual_parameters.yaml"/>

<xacro:arg name="transmission_hw_interface" default=""/>

<xacro:arg name="safety_limits" default="false"/>

<xacro:arg name="safety_pos_margin" default="0.15"/>

<xacro:arg name="safety_k_position" default="20"/>

  

<!--When using gazebo simulations absolute paths are necessary.-->

<xacro:arg name="force_abs_paths" default="false" />

  

<!-- create link fixed to the "world" -->

<link name="world" />

  

<!-- arm -->
<!-- ur_macro.xacro파일에서 설정한 ur_robot을 include를 통해 불러옴 -->
<xacro:ur_robot

name="$(arg name)"

tf_prefix="$(arg tf_prefix)"

parent="world"

joint_limits_parameters_file="$(arg joint_limit_params)"

kinematics_parameters_file="$(arg kinematics_params)"

physical_parameters_file="$(arg physical_params)"

visual_parameters_file="$(arg visual_params)"

safety_limits="$(arg safety_limits)"

safety_pos_margin="$(arg safety_pos_margin)"

safety_k_position="$(arg safety_k_position)"

force_abs_paths="$(arg force_abs_paths)"

>

<origin xyz="0 0 0" rpy="0 0 0" /> <!-- position robot in the world -->
<!-- 그래서 여기서 ur_robot을 활용할 수 있음 -->
</xacro:ur_robot>

</robot>
```
## 3. 마무리

| URDF                                                                                            | Xacro                                                    |
| ----------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| - 확장성이 떨어짐<br>                                                                                  | - include을 통해 Xacro, macro 서로 정보 공유할 수 있는 시스템을 만들어 놓음    |
| 대표 구성요소<br>-link<br>-joint<br>-Inertial<br>-visual<br>-collisiion<br>-transmission<br>-material | - urdf 의 확장성을 위한 형식<br>- 병합 및 분할에 용이<br>- include, param |


# Chapter 6. Manipulator (MoveIt2)

## 1. MoveIt2 개요
- 서치 알고리즘
- 모션 플래닝 알고리즘
을 결합한 motion planning에 특화된  Moveit2 패키지를 사용 

- motion planning에 특화된  ROS2 패키지의 일종
	-  Sampling-based
	- Optimization-based
- 알고리즘 제공
- 로봇 제조사와 협업 및 연동
	- cobot arms: universal robots, panda
	- industrial arms: kuka, abb
- 사용자는 용도에 맞게 파라미터 조절
- Rviz2, Gazebo와 연동
	- Rviz2: 데이터 시각화 및  UI  제공
	- Gazebo: 물리 엔진 시뮬레이션

## 2. 패키지 구조
- moveit2 는 특정한 패키지 구조가 있고 그 구조에 따라 패키지가 실행, 빌드가 되기 때문에 가각의 폴더 어떤 역할을 하는지 아는것이 중요
## 3. 패키지 구조2
https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver 

이름 뒤에 moveit_config라고 적혀있는거 찾으면됨!!

패키지 필수 파일
- config
- launch
- srdf
	->이 3개는 필수로 있어야됨 (doc 파일은 필수 X)

ur_moveit_config/config/joint_limits.yaml : joint가 몇도까지 돌아가는지 설정해 놓은 파일
ur_moveit_config/config/kinematics.yaml : 어떤 kinematics활용할건지
ur_moveit_config/config/ompl_planning.yaml : 어떠한 파라미터 활용할건지
ur_moveit_config/config/chomp_planning.yaml : chomp을 활용할때 사용하는 파라미터
## 4. 패키지구조 마무리
 패키지구조를 아는것이 중요!
## 5. MoveIt 2  설치
moveit 설치 사이트: https://moveit.ai/install-moveit2/binary/ 

moveit 설치 명령어
```
sudo apt install ros-humble-moveit
```
## 6. 강의 요약

Moveit2
- Motion Planning에 특화된 ROS2  패키지의 일종
- 알고리즘 제공
- 로봇 제조사와 협업 및 연동

패키지 구조
- config
- launch
- srdf



# Chatper 7. Manipulator (MoveIt2) 실습

## 1. 강의 개요

## 2. MoveIt 패키지 설치

## 3. 커맨드 실행

## 4. MoveIt 실행

## 5. gripper Test

## 6. ur+gripper

## 7. world

## 8. moveitConfig

## 9. launch 0

## 10. launch 1

## 11. laucnh 2
## 12. build And Run

## 13. pickNplace

## 14. 원리 설명

## 15. 마무리



# Chapter 8. Mobile Robot(Nav2)

## 1. Nav2 개요

## 2. Nav2 미니 실습 개요

## 3. Nav2 설명

## 4. 2D Pose

## 5. 마무리

