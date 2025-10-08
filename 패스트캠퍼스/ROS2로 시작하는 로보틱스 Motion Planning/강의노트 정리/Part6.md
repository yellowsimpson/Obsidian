
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
ros2 설치 사이트 : https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html

터미널 1 : talker
$ ros2 run demo_nodes_py talker

터미널 2 : lisener
$ ros2 run demo_nodes_py listener

$ gedit ~/.bashrc : bashrc 여는 명령어

여기에 source /opt/humble/setup.bash 넣어주면 터미널 틀때마다 칠 필요X

## 3. turtlesim 설치
- [[ROS 명령어]]
$sudo apt install ros-humble-turtlesim
: turtlesim 설치 명령어
## 4. node
[[ROS 명령어]]

$ ros2 pkg executables turtlesim
: 현재 사용할 수 있는 turtlesim 패키지  안에 executables  보기
ex)
turtlesim draw_square
turtlesim mimic
turtlesim turtle_teleop_key
turtlesim turtlesim_node
	->총 4개의 executables가 있음

$ ros2 node list
: 지금 현재 어떤 node가 실행되어 있는 지 확인하는 명령어
/turtlesim

$ ros2 run turtlesim turtlesim_node 
: turtlesim 실행 명령어
$ ros2 run turtlesim turtle_teleop_key 
: 거북이 제어 명령어(방향키 누르면 제어 가능)

$ ros2 node info /turtlesim
:  turtlesim 안에 있는 노드 정보 확인

```
/turtlesim
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/color_sensor: turtlesim/msg/Color
    /turtle1/pose: turtlesim/msg/Pose
  Service Servers:
    /clear: std_srvs/srv/Empty
    /kill: turtlesim/srv/Kill
    /reset: std_srvs/srv/Empty
    /spawn: turtlesim/srv/Spawn
    /turtle1/set_pen: turtlesim/srv/SetPen
    /turtle1/teleport_absolute: turtlesim/srv/TeleportAbsolute
    /turtle1/teleport_relative: turtlesim/srv/TeleportRelative
    /turtlesim/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /turtlesim/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /turtlesim/get_parameters: rcl_interfaces/srv/GetParameters
    /turtlesim/list_parameters: rcl_interfaces/srv/ListParameters
    /turtlesim/set_parameters: rcl_interfaces/srv/SetParameters
    /turtlesim/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
  Action Clients:
```
## 5. rqt
$rqt_graph
: 현재 노드들이 어떻게 연결되어 있는지 확인하는 명령어
## 6. topic
$ ros2 topic list
: 현재 실행 중인 모든 토픽(topic)의 이름을 목록으로 보여주는 명령어
	/parameter_events
	/rosout
	/turtle1/cmd_vel
	/turtle1/color_sensor
	/turtle1/pose

$ ros2 topic  echo
: ROS 2에서 특정 토픽(topic)에 퍼블리시되는 메시지를 실시간으로 화면에 출력
```
usage: ros2 topic echo [-h] [--spin-time SPIN_TIME] [-s]
                       [--no-daemon]
                       [--qos-profile {unknown,system_default,sensor_data,services_default,parameters,parameter_events,action_status_default}]
                       [--qos-depth N]
                       [--qos-history {system_default,keep_last,keep_all,unknown}]
                       [--qos-reliability {system_default,reliable,best_effort,unknown}]
                       [--qos-durability {system_default,transient_local,volatile,unknown}]
                       [--csv] [--field FIELD] [--full-length]
                       [--truncate-length TRUNCATE_LENGTH]
                       [--no-arr] [--no-str] [--flow-style]
                       [--lost-messages] [--no-lost-messages]
                       [--raw] [--filter FILTER_EXPR] [--once]
                       topic_name [message_type]
ros2 topic echo: error: the following arguments are required: topic_name
```

$ ros2 topic info
: topic 정보 알려주는 명령어
usage: ros2 topic info [-h] [--spin-time SPIN_TIME] [-s]
                       [--no-daemon] [--verbose]
                       topic_name
ros2 topic info: error: the following arguments are required: topic_name

$ros2 topic pub 1.토픽이름    2.메시지타입    3.어떤 데이터를 담을 껀지 
예시
$ ros2 interface show geometry_msgs/msg/Twist
```
# This expresses velocity in free space broken into its linear and angular parts.

Vector3  linear
	float64 x
	float64 y
	float64 z
Vector3  angular
	float64 x
	float64 y
	float64 z

```
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

    Main author of the migration to yaml configs: Ludovic Delval.

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

  <!-- xacro: macro => 로봇의 base를 구성하는 부분을 ur_robot으로 정의 -->
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
      force_abs_paths:=false">

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
        <origin xyz="0 0 0" rpy="0 0 0"/>
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
          izz="${shoulder_inertia_izz}"/>
      </inertial>
    </link>

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
          izz="${upper_arm_inertia_izz}"/>
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
          izz="${forearm_inertia_izz}"/>
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
          izz="${wrist_1_inertia_izz}"/>
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
          izz="${wrist_2_inertia_izz}"/>
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
          izz="${wrist_3_inertia_izz}"/>
      </inertial>
    </link>

    <!-- base_joint fixes base_link to the environment -->
    <joint name="${tf_prefix}base_joint" type="fixed">
      <xacro:insert_block name="origin"/>
      <parent link="${parent}"/>
      <child link="${tf_prefix}base_link"/>
    </joint>

    <!-- joints - main serial chain -->
    <joint name="${tf_prefix}base_link-base_link_inertia" type="fixed">
      <parent link="${tf_prefix}base_link"/>
      <child link="${tf_prefix}base_link_inertia"/>
      <!-- 'base_link' is REP-103 aligned (X+ forward), while the internal
           frames of the robot/controller have X+ pointing backwards.
           Use this joint to introduce the necessary rotation over Z (pi rad). -->
      <origin xyz="0 0 0" rpy="0 0 ${pi}"/>
    </joint>

    <joint name="${tf_prefix}shoulder_pan_joint" type="revolute">
      <parent link="${tf_prefix}base_link_inertia"/>
      <child link="${tf_prefix}shoulder_link"/>
      <origin xyz="${shoulder_x} ${shoulder_y} ${shoulder_z}" rpy="${shoulder_roll} ${shoulder_pitch} ${shoulder_yaw}"/>
      <axis xyz="0 0 1"/>
      <limit lower="${shoulder_pan_lower_limit}" upper="${shoulder_pan_upper_limit}"
             effort="${shoulder_pan_effort_limit}" velocity="${shoulder_pan_velocity_limit}"/>
      <xacro:if value="${safety_limits}">
        <safety_controller soft_lower_limit="${shoulder_pan_lower_limit + safety_pos_margin}"
                           soft_upper_limit="${shoulder_pan_upper_limit - safety_pos_margin}"
                           k_position="${safety_k_position}" k_velocity="0.0"/>
      </xacro:if>
      <dynamics damping="0" friction="0"/>
    </joint>

    <joint name="${tf_prefix}shoulder_lift_joint" type="revolute">
      <parent link="${tf_prefix}shoulder_link"/>
      <child link="${tf_prefix}upper_arm_link"/>
      <origin xyz="${upper_arm_x} ${upper_arm_y} ${upper_arm_z}" rpy="${upper_arm_roll} ${upper_arm_pitch} ${upper_arm_yaw}"/>
      <axis xyz="0 0 1"/>
      <limit lower="${shoulder_lift_lower_limit}" upper="${shoulder_lift_upper_limit}"
             effort="${shoulder_lift_effort_limit}" velocity="${shoulder_lift_velocity_limit}"/>
      <xacro:if value="${safety_limits}">
        <safety_controller soft_lower_limit="${shoulder_lift_lower_limit + safety_pos_margin}"
                           soft_upper_limit="${shoulder_lift_upper_limit - safety_pos_margin}"
                           k_position="${safety_k_position}" k_velocity="0.0"/>
      </xacro:if>
      <dynamics damping="0" friction="0"/>
    </joint>

    <joint name="${tf_prefix}elbow_joint" type="revolute">
      <parent link="${tf_prefix}upper_arm_link"/>
      <child link="${tf_prefix}forearm_link"/>
      <origin xyz="${forearm_x} ${forearm_y} ${forearm_z}" rpy="${forearm_roll} ${forearm_pitch} ${forearm_yaw}"/>
      <axis xyz="0 0 1"/>
      <limit lower="${elbow_joint_lower_limit}" upper="${elbow_joint_upper_limit}"
             effort="${elbow_joint_effort_limit}" velocity="${elbow_joint_velocity_limit}"/>
      <xacro:if value="${safety_limits}">
        <safety_controller soft_lower_limit="${elbow_joint_lower_limit + safety_pos_margin}"
                           soft_upper_limit="${elbow_joint_upper_limit - safety_pos_margin}"
                           k_position="${safety_k_position}" k_velocity="0.0"/>
      </xacro:if>
      <dynamics damping="0" friction="0"/>
    </joint>

    <joint name="${tf_prefix}wrist_1_joint" type="revolute">
      <parent link="${tf_prefix}forearm_link"/>
      <child link="${tf_prefix}wrist_1_link"/>
      <origin xyz="${wrist_1_x} ${wrist_1_y} ${wrist_1_z}" rpy="${wrist_1_roll} ${wrist_1_pitch} ${wrist_1_yaw}"/>
      <axis xyz="0 0 1"/>
      <limit lower="${wrist_1_lower_limit}" upper="${wrist_1_upper_limit}"
             effort="${wrist_1_effort_limit}" velocity="${wrist_1_velocity_limit}"/>
      <xacro:if value="${safety_limits}">
        <safety_controller soft_lower_limit="${wrist_1_lower_limit + safety_pos_margin}"
                           soft_upper_limit="${wrist_1_upper_limit - safety_pos_margin}"
                           k_position="${safety_k_position}" k_velocity="0.0"/>
      </xacro:if>
      <dynamics damping="0" friction="0"/>
    </joint>

    <joint name="${tf_prefix}wrist_2_joint" type="revolute">
      <parent link="${tf_prefix}wrist_1_link"/>
      <child link="${tf_prefix}wrist_2_link"/>
      <origin xyz="${wrist_2_x} ${wrist_2_y} ${wrist_2_z}" rpy="${wrist_2_roll} ${wrist_2_pitch} ${wrist_2_yaw}"/>
      <axis xyz="0 0 1"/>
      <limit lower="${wrist_2_lower_limit}" upper="${wrist_2_upper_limit}"
             effort="${wrist_2_effort_limit}" velocity="${wrist_2_velocity_limit}"/>
      <xacro:if value="${safety_limits}">
        <safety_controller soft_lower_limit="${wrist_2_lower_limit + safety_pos_margin}"
                           soft_upper_limit="${wrist_2_upper_limit - safety_pos_margin}"
                           k_position="${safety_k_position}" k_velocity="0.0"/>
      </xacro:if>
      <dynamics damping="0" friction="0"/>
    </joint>

    <joint name="${tf_prefix}wrist_3_joint" type="${wrist_3_joint_type}">
      <parent link="${tf_prefix}wrist_2_link"/>
      <child link="${tf_prefix}wrist_3_link"/>
      <origin xyz="${wrist_3_x} ${wrist_3_y} ${wrist_3_z}" rpy="${wrist_3_roll} ${wrist_3_pitch} ${wrist_3_yaw}"/>
      <axis xyz="0 0 1"/>

      <xacro:if value="${wrist_3_joint_type != 'continuous'}">
        <limit lower="${wrist_3_lower_limit}" upper="${wrist_3_upper_limit}"
               effort="${wrist_3_effort_limit}" velocity="${wrist_3_velocity_limit}"/>
        <xacro:if value="${safety_limits}">
          <safety_controller soft_lower_limit="${wrist_3_lower_limit + safety_pos_margin}"
                             soft_upper_limit="${wrist_3_upper_limit - safety_pos_margin}"
                             k_position="${safety_k_position}" k_velocity="0.0"/>
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
      <!-- Note the rotation over Z of pi radians: base_link is REP-103 aligned (X+ forward, Y+ left, Z+ up),
           rotate to align with the UR controller 'Base' coordinates. -->
      <origin xyz="0 0 0" rpy="0 0 ${pi}"/>
      <parent link="${tf_prefix}base_link"/>
      <child link="${tf_prefix}base"/>
    </joint>

    <!-- ROS-Industrial 'flange' frame - attachment point for EEF models -->
    <link name="${tf_prefix}flange"/>
    <joint name="${tf_prefix}wrist_3-flange" type="fixed">
      <parent link="${tf_prefix}wrist_3_link"/>
      <child link="${tf_prefix}flange"/>
      <origin xyz="0 0 0" rpy="0 ${-pi/2.0} ${-pi/2.0}"/>
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

  <!-- 
    possible 'ur_type' values: ur3, ur3e, ur5, ur5e, ur10, ur10e, ur16e, ur20, ur30
    the default value should raise an error in case this was called without defining the type 
  -->
  <xacro:arg name="ur_type" default="ur5x"/>

  <!-- parameters -->
  <xacro:arg name="tf_prefix" default="" />
  <xacro:arg name="joint_limit_params"  default="$(find ur_description)/config/$(arg ur_type)/joint_limits.yaml"/>
  <xacro:arg name="kinematics_params"   default="$(find ur_description)/config/$(arg ur_type)/default_kinematics.yaml"/>
  <xacro:arg name="physical_params"     default="$(find ur_description)/config/$(arg ur_type)/physical_parameters.yaml"/>
  <xacro:arg name="visual_params"       default="$(find ur_description)/config/$(arg ur_type)/visual_parameters.yaml"/>
  <xacro:arg name="transmission_hw_interface" default=""/>
  <xacro:arg name="safety_limits"      default="false"/>
  <xacro:arg name="safety_pos_margin"  default="0.15"/>
  <xacro:arg name="safety_k_position"  default="20"/>

  <!-- When using gazebo simulations absolute paths are necessary. -->
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
      force_abs_paths="$(arg force_abs_paths)">
      
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
Moveit2 를 활용한 pick and place 실습
- UR Moveit Package Test
- Gripper Package Test
- 로봇 구성
- 환경 구성
- 실행 코드 구성
## 2. MoveIt 패키지 설치
https://github.com/UniversalRobots/Universal_Robots_ROS2_Driver
위의 저장소 중 config 폴더

1.  **Install the driver**
    ```shell
    sudo apt-get install ros-rolling-ur
    ```
    
    See the [installation instructions](https://docs.universal-robots.com/Universal_Robots_ROS2_Documentation/doc/ur_robot_driver/ur_robot_driver/doc/installation/installation.html) for more details and source-build instructions.


## 3. 커맨드 실행
2. 실행 명령어
```shell
ros2 launch ur_moveit_config  ur_moveit.launch.py ur_type:=ur5e
```
-> ros2 launch  <패키지 이름>  <실행할 launch 파일 이름>  <런치 인자(launch argument) 설정(불러올 urdf 파일 )>                                                                         

## 4. MoveIt 실행
urdf -> robot_description(토픽)을 moveit2에 보냄

1. 하드웨어를 구동(driver안에 launch 파일 안에 로봇 description을 실행하는  launch file이 )
2. Rviz2->  robotdescription

rivz2에 띄운 모델을 옆에 motion planning 설정 창에 옆에 
![[moveit2.png]]

![[rosgraph_1.png]]

## 5. gripper Test
그리퍼 예제 깃허브 링크: https://github.com/PickNikRobotics/ros2_robotiq_gripper

1. 새로운 ws와 그 안에 src 폴더를 만든다.
2. 그 안에  위 깃허브 링크를 git clone  해준다.
3. 새로운 ws 에서 $ colcon build --symlink-install 을 해주면 에러가 생긴다!! why??

<ros2_robotiq_gripper-not-released.rolling.repos> 이 폴더 안에 
``` repos
repositories:
  serial:
    type: git
    url: https://github.com/tylerjw/serial.git
    version: ros2
```
https://github.com/tylerjw/serial.git  이 저장소로 같이 git clone 해줘야되

https://github.com/RoverRobotics-forks/serial-ros2 난 이걸로  git clone 한 후 


### <motion_planning_ws/src/serial/CMakeLists.txt>

```txt
cmake_minimum_required(VERSION 3.5)
project(serial)

# PIC 전역 활성화 (보험용)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

find_package(ament_cmake REQUIRED)

# 라이브러리 본체: 우선 공통 소스만 넣고, OS별 소스는 target_sources로 추가
add_library(${PROJECT_NAME}
  src/serial.cc
)

# 헤더 공개
target_include_directories(${PROJECT_NAME}
  PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

# 타깃에 PIC 확실히 적용 (add_library 다음 줄에서!)
set_property(TARGET ${PROJECT_NAME} PROPERTY POSITION_INDEPENDENT_CODE ON)

# OS별 소스/링크
if(APPLE) # macOS
  find_library(IOKIT_LIBRARY IOKit)
  find_library(FOUNDATION_LIBRARY Foundation)
  target_sources(${PROJECT_NAME} PRIVATE
    src/impl/unix.cc
    src/impl/list_ports/list_ports_osx.cc
  )
  target_link_libraries(${PROJECT_NAME} ${FOUNDATION_LIBRARY} ${IOKIT_LIBRARY})

elseif(UNIX) # Linux 등
  target_sources(${PROJECT_NAME} PRIVATE
    src/impl/unix.cc
    src/impl/list_ports/list_ports_linux.cc
  )
  target_link_libraries(${PROJECT_NAME} rt pthread)

elseif(WIN32) # Windows
  target_sources(${PROJECT_NAME} PRIVATE
    src/impl/win.cc
    src/impl/list_ports/list_ports_win.cc
  )
  target_link_libraries(${PROJECT_NAME} setupapi)
  ament_export_libraries(setupapi)
endif()

# ament 내보내기 정보
ament_export_include_directories(include)
ament_export_libraries(${PROJECT_NAME})

# 설치
install(TARGETS ${PROJECT_NAME}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)
install(DIRECTORY include/ DESTINATION include)

ament_package()
```
이렇게 수정한 후 $ colcon build --symlink-install 해줌


그 후 rivz2실행
$ ros2 launch robotiq_description view_gripper.launch.py 

![[gripper.png]]

motion_planning_ws/src/ros2_robotiq_gripper/robotiq_description/urdf/2f_85.ros2_control.xacro
2f_85.ros2_control.xacro
2f_140.ros2_control.xacro
-> 2개의 파일 중 85가 조금 더 작은 모델

## 6. ur+gripper
<motion_planning_ws/src/ur_robotiq_moveit_config/urdf>
### <ur_robotiq_macro.urdf.xacro>
```xml
<?xml version="1.0"?>
<robot xmlns:xacro="http://wiki.ros.org/xacro">

  <xacro:macro name="ur_robotiq" params="
    ur_name:=ur
    ur_type:=ur5x
    tf_prefix
    parent
    *origin
    use_fake_hardware:=false
    fake_sensor_commands:=false
    sim_gazebo:=false
    sim_ignition:=false
    headless_mode:=false
    initial_positions
    simulation_controllers"
    >

    <!-- import main macro -->
    <xacro:include filename="$(find ur_description)/urdf/ur_macro.xacro"/>
    <xacro:include filename="$(find robotiq_description)/urdf/robotiq_2f_85_macro.urdf.xacro" />
    <xacro:include filename="$(find robotiq_description)/urdf/ur_to_robotiq_adapter.urdf.xacro" />
    <!-- <xacro:include filename="$(find ur_robotiq_moveit_config)/urdf/realsense_d435.urdf.xacro"/> -->
    
    <!-- property -->
    <xacro:property name="joint_limits_parameters_file" value="$(find ur_description)/config/${ur_type}/joint_limits.yaml"/>
    <xacro:property name="kinematics_parameters_file" value="$(find ur_description)/config/${ur_type}/default_kinematics.yaml"/>
    <xacro:property name="physical_parameters_file" value="$(find ur_description)/config/${ur_type}/physical_parameters.yaml"/>
    <xacro:property name="visual_parameters_file" value="$(find ur_description)/config/${ur_type}/visual_parameters.yaml"/>
    <xacro:property name="transmission_hw_interface" value=""/>
    <xacro:property name="safety_limits" value="false"/>
    <xacro:property name="safety_pos_margin" value="0.15"/>
    <xacro:property name="safety_k_position" value="20"/>

    <!-- ros2_control related parameters -->
    <xacro:property name="headless_mode" value="false" />
    <xacro:property name="robot_ip" value="0.0.0.0" />
    <xacro:property name="script_filename" value=""/>
    <xacro:property name="output_recipe_filename" value=""/>
    <xacro:property name="input_recipe_filename" value=""/>
    <xacro:property name="reverse_ip" value="0.0.0.0"/>
    <xacro:property name="script_command_port" value="50004"/>
    <xacro:property name="reverse_port" value="50001"/>
    <xacro:property name="script_sender_port" value="50002"/>
    <xacro:property name="trajectory_port" value="50003"/>

    <!-- tool communication related parameters -->
    <xacro:property name="use_tool_communication" value="false" />
    <xacro:property name="tool_voltage" value="0" />
    <xacro:property name="tool_parity" value="0" />
    <xacro:property name="tool_baud_rate" value="115200" />
    <xacro:property name="tool_stop_bits" value="1" />
    <xacro:property name="tool_rx_idle_chars" value="1.5" />
    <xacro:property name="tool_tx_idle_chars" value="3.5" />
    <xacro:property name="tool_device_name" value="/tmp/ttyUR" />
    <xacro:property name="tool_tcp_port" value="54321" />

    <!-- arm -->
    <xacro:ur_robot
      name="${ur_name}"
      tf_prefix="${tf_prefix}"
      parent="${parent}" 
      joint_limits_parameters_file="${joint_limits_parameters_file}"
      kinematics_parameters_file="${kinematics_parameters_file}"
      physical_parameters_file="${physical_parameters_file}"
      visual_parameters_file="${visual_parameters_file}"
      safety_limits="${safety_limits}"
      safety_pos_margin="${safety_pos_margin}"
      safety_k_position="${safety_k_position}"
      >
      <xacro:insert_block name="origin" /> <!-- position robot in the parent link -->
    </xacro:ur_robot>

    <!-- adapter -->
    <xacro:ur_to_robotiq
      prefix="${tf_prefix}"
      parent="${tf_prefix}tool0"
      child="${tf_prefix}gripper_mount_link"
      rotation="0."
      />

    <!-- gripper -->
    <xacro:robotiq_gripper 
        name="${ur_name}gripper" 
        prefix="${tf_prefix}"
        parent="${tf_prefix}gripper_mount_link" 
        use_fake_hardware="${use_fake_hardware}"
        sim_gazebo="$(arg sim_gazebo)">
        <origin xyz="0 0 0" rpy="0 0 0" />
    </xacro:robotiq_gripper>

    <!-- grasp point for planning -->
    <link name="${tf_prefix}grasp_point"/>
    <joint name="${tf_prefix}grasp_point_joint" type="fixed">
      <parent link="${tf_prefix}tool0"/>
      <child link="${tf_prefix}grasp_point"/>
      <origin xyz="0 0 0.15" rpy="0 0 0"/>
    </joint>

    <!-- realsense camera -->
    <!-- Use the nominal extrinsics between camera frames if the calibrated extrinsics aren't being published. e.g. running the device in simulation -->
    <!--
    <xacro:sensor_d435 parent="${tf_prefix}tool0"
      name="${tf_prefix}camera"
      use_nominal_extrinsics="true" 
      add_plug="false" 
      use_mesh="true">
      <origin xyz="0 -0.1 0" rpy="0 -1.5707 1.5707"/>
    </xacro:sensor_d435>
    -->

  </xacro:macro>
</robot>

```

### <ur_robotiq.urdf.xacro>
```xml
<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="ur_robotiq">

    <!-- ========================= -->
    <!--   Argument definitions    -->
    <!-- ========================= -->
    <xacro:arg name="tf_prefix" default=""/>
    <xacro:arg name="ur_type" default="ur5e"/>
    <xacro:arg name="sim_gazebo" default="true" />
    <xacro:arg name="parent" default="world" />
    <xacro:arg name="simulation_controllers" default="$(find ur_robotiq_moveit_config)/config/controllers.yaml" />
    <xacro:arg name="initial_positions_file" default="$(find ur_robotiq_moveit_config)/config/initial_positions.yaml"/>
    <xacro:arg name="base_frame_file" default="$(find ur_robotiq_moveit_config)/config/base_frame.yaml" />
    <xacro:arg name="transmission_hw_interface" default=""/>

    <!-- ========================= -->
    <!--   Property setup          -->
    <!-- ========================= -->
    <xacro:property name="base_frame_file" value="$(arg base_frame_file)"/>
    <xacro:property name="base_frame" value="${xacro.load_yaml(base_frame_file)['base_frame']}"/>

    <!-- ========================= -->
    <!--   Include main macros     -->
    <!-- ========================= -->
    <xacro:include filename="$(find ur_robotiq_moveit_config)/urdf/ur_robotiq_macro.urdf.xacro"/>
    <xacro:include filename="$(find ur_robotiq_moveit_config)/urdf/ur_gz.ros2_control.xacro"/>

    <!-- ========================= -->
    <!--   World Link              -->
    <!-- ========================= -->
    <link name="world"/>

    <!-- ========================= -->
    <!--   Robot: UR + Robotiq     -->
    <!-- ========================= -->
    <xacro:ur_robotiq 
        ur_name="ur"
        ur_type="$(arg ur_type)" 
        tf_prefix="$(arg tf_prefix)" 
        parent="$(arg parent)"
        sim_gazebo="$(arg sim_gazebo)"
        initial_positions="$(arg initial_positions_file)"
        simulation_controllers="$(arg simulation_controllers)">
        <origin xyz="${base_frame['x']} ${base_frame['y']} ${base_frame['z']}"
                rpy="${base_frame['roll']} ${base_frame['pitch']} ${base_frame['yaw']}" />
    </xacro:ur_robotiq>

    <!-- ========================= -->
    <!--   Gazebo / ROS2 Control   -->
    <!-- ========================= -->
    <xacro:if value="$(arg sim_gazebo)">
        <!-- World reference for Gazebo -->
        <gazebo reference="world">
        </gazebo>

        <!-- Gazebo ROS2 Control Plugin -->
        <gazebo>
            <plugin filename="libgz_ros2_control-system.so" name="gz_ros2_control::GazeboSimROS2ControlPlugin">
                <parameters>$(arg simulation_controllers)</parameters>
            </plugin>
        </gazebo>

        <!-- ROS2 Control Interface Instance -->
        <xacro:ur_ros2_control
            name="ur"
            tf_prefix="$(arg tf_prefix)"
            transmission_hw_interface="$(arg transmission_hw_interface)"
        />
    </xacro:if>

</robot>

```
## 7. world
### <workstation.sdf>
```xml
<?xml version="1.0" ?>
<sdf version="1.6">
  <world name="workstation">

    <!-- ========== Scene Settings ========== -->
    <scene>
      <shadows>0</shadows>
    </scene>

    <!-- ========== GUI Camera View ========== -->
    <gui>
      <camera name="user_camera">
        <!-- pose: x y z roll pitch yaw -->
        <pose>0.75 -0.75 1.4 0 0.29 2.21</pose>
      </camera>
    </gui>
    <!-- GUI 카메라 시점 설정 -->

    <!-- ========== Lighting ========== -->
    <include>
    <!-- include 는 동일 폴더 안에 있는 내용을 불러옴 -->
      <uri>model://sun</uri>
    </include>
    <!-- 태양광 조명 추가 -->

    <!-- ========== Tables ========== -->
    <!-- table은 는 동일 폴더 안에 있는 내용을 불러옴 -->
    <model name="table1">
      <static>true</static>
      <include>
        <uri>model://table</uri>
      </include>
      <pose>-0.8 0.5 0 0 0 1.5708</pose>
    </model>

    <model name="table2">
      <static>true</static>
      <include>
        <uri>model://table</uri>
      </include>
      <pose>0 0.5 0 0 0 1.5708</pose>
    </model>

    <model name="table3">
      <static>true</static>
      <include>
        <uri>model://table</uri>
      </include>
      <pose>0.8 0.5 0 0 0 1.5708</pose>
    </model>

    <!-- ========== Cube Object ========== -->
    <model name="cube">
      <!-- Positioned on table2 -->
      <pose>0 0.5 1.0 0 0 0</pose>

      <link name="link">
        <inertial>
          <mass>0.5</mass>
          <inertia>
            <ixx>0.0005</ixx>
            <iyy>0.0005</iyy>
            <izz>0.0005</izz>
            <ixy>0.0</ixy>
            <ixz>0.0</ixz>
            <iyz>0.0</iyz>
          </inertia>
        </inertial>

        <collision name="collision">
          <geometry>
            <box>
              <size>0.03 0.03 0.03</size>
            </box>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>0.03 0.03 0.03</size>
            </box>
          </geometry>
          <material>
            <ambient>0.8 0.2 0.2 1</ambient>
            <!--    (x, y, z, row, pith, low) -->
            <diffuse>0.8 0.2 0.2 1</diffuse>
            <specular>0.8 0.2 0.2 1</specular>
          </material>
        </visual>
      </link>
    </model>

    <!-- ========== Ground Plane ========== -->
    <model name="ground_plane">
	<!-- 동일 선상 ground 모델 불러옴-->
      <static>true</static>
      <include>
        <uri>model://ground_plane</uri>
      </include>
    </model>

  </world>
</sdf>

```

### <model.sdf>
-> 이 파일 같은 경우 웹상에서 구할 수 있는 파일이다
```xml
<?xml version="1.0" ?>
<sdf version="1.6">
  <world name="workstation">

    <!-- ========== Scene Settings ========== -->
    <scene>
      <shadows>0</shadows>
    </scene>

    <!-- ========== GUI Camera View ========== -->
    <gui>
      <camera name="user_camera">
        <!-- pose: x y z roll pitch yaw -->
        <pose>0.75 -0.75 1.4 0 0.29 2.21</pose>
      </camera>
    </gui>

    <!-- ========== Lighting ========== -->
    <include>
      <uri>model://sun</uri>
    </include>

    <!-- ========== Table Models ========== -->
    <model name="table1">
      <static>true</static>
      <include>
        <uri>model://table</uri>
      </include>
      <pose>-0.8 0.5 0 0 0 1.5708</pose>
    </model>

    <model name="table2">
      <static>true</static>
      <include>
        <uri>model://table</uri>
      </include>
      <pose>0 0.5 0 0 0 1.5708</pose>
    </model>

    <model name="table3">
      <static>true</static>
      <include>
        <uri>model://table</uri>
      </include>
      <pose>0.8 0.5 0 0 0 1.5708</pose>
    </model>

    <!-- ========== Cube Object ========== -->
    <model name="cube">
      <!-- Positioned on table2 -->
      <pose>0 0.5 1.0 0 0 0</pose>

      <link name="link">
        <inertial>
          <mass>0.5</mass>
          <inertia>
            <ixx>0.0005</ixx>
            <iyy>0.0005</iyy>
            <izz>0.0005</izz>
            <ixy>0.0</ixy>
            <ixz>0.0</ixz>
            <iyz>0.0</iyz>
          </inertia>
        </inertial>

        <collision name="collision">
          <geometry>
            <box>
              <size>0.03 0.03 0.03</size>
            </box>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name="visual">
          <geometry>
            <box>
              <size>0.03 0.03 0.03</size>
            </box>
          </geometry>
          <material>
            <ambient>0.8 0.2 0.2 1</ambient>
            <diffuse>0.8 0.2 0.2 1</diffuse>
            <specular>0.8 0.2 0.2 1</specular>
          </material>
        </visual>
      </link>
    </model>

    <!-- ========== Ground Plane ========== -->
    <model name="ground_plane">
      <static>true</static>
      <include>
        <uri>model://ground_plane</uri>
      </include>
    </model>

  </world>
</sdf>
```
## 8. moveitConfig
- launch 파일: 어떤걸 launch 한다는 의미 (ur과 관련된 정보 포함)
- script: 어떤한 task를 수행하도록 하는 파일
- srdf:  moveit2에서 collision의 관계 나타내는 파일

### <ur_macro.srdf.xacro>
```xml
<?xml version="1.0" encoding="UTF-8"?>
<robot xmlns:xacro="http://wiki.ros.org/xacro">

  <!--
    =============================================
      Semantic Robot Description Format (SRDF)
    =============================================

    ⚙️ 개요:
    - URDF를 대체하거나 확장하는 것이 아니라,
      로봇의 "의미적 구성 요소" (그룹, 상태, 충돌 무시 등)를 기술하는 파일.
    - MoveIt! 등에서 로봇의 동작 그룹, 상태, 충돌 제외 링크 등을 정의할 때 사용됨.
    - 반드시 대응하는 URDF가 존재해야 함 (여기서 정의된 링크/조인트는 URDF에 이미 있어야 함)
  -->

  <xacro:macro name="ur_srdf" params="name prefix">

    <!-- ============================= -->
    <!--     GROUP 정의 (Manipulator) -->
    <!-- ============================= -->
    <!--
      - group: 로봇의 관절/링크 집합 (예: arm, gripper)
      - chain: base_link → tool0 까지의 모든 링크 및 조인트 포함
    -->
    <group name="${prefix}${name}_manipulator">
      <chain base_link="${prefix}base_link" tip_link="${prefix}tool0" />
    </group>

    <!-- ============================= -->
    <!--     GROUP STATES 정의         -->
    <!-- ============================= -->
    <!--
      - 특정 그룹의 조인트 구성을 이름으로 저장
      - MoveIt에서 “home”, “up” 등으로 호출 가능
    -->

    <!-- 기본 Home 자세 -->
    <group_state name="${prefix}home" group="${prefix}${name}_manipulator">
      <joint name="${prefix}elbow_joint" value="0" />
      <joint name="${prefix}shoulder_lift_joint" value="-1.5707" />
      <joint name="${prefix}shoulder_pan_joint" value="0" />
      <joint name="${prefix}wrist_1_joint" value="0" />
      <joint name="${prefix}wrist_2_joint" value="0" />
      <joint name="${prefix}wrist_3_joint" value="0" />
    </group_state>

    <!-- Up 자세 -->
    <group_state name="${prefix}up" group="${prefix}${name}_manipulator">
      <joint name="${prefix}elbow_joint" value="0" />
      <joint name="${prefix}shoulder_lift_joint" value="-1.5707" />
      <joint name="${prefix}shoulder_pan_joint" value="0" />
      <joint name="${prefix}wrist_1_joint" value="-1.5707" />
      <joint name="${prefix}wrist_2_joint" value="0" />
      <joint name="${prefix}wrist_3_joint" value="0" />
    </group_state>

    <!-- 테스트 자세 -->
    <group_state name="${prefix}test_configuration" group="${prefix}${name}_manipulator">
      <joint name="${prefix}elbow_joint" value="1.4" />
      <joint name="${prefix}shoulder_lift_joint" value="-1.62" />
      <joint name="${prefix}shoulder_pan_joint" value="1.54" />
      <joint name="${prefix}wrist_1_joint" value="-1.2" />
      <joint name="${prefix}wrist_2_joint" value="-1.6" />
      <joint name="${prefix}wrist_3_joint" value="-0.11" />
    </group_state>

    <!-- ============================= -->
    <!--     COLLISION 제외 설정       -->
    <!-- ============================= -->
    <!--
      - 인접하거나 실제로 충돌 불가능한 링크 간 충돌 체크를 비활성화
      - MoveIt의 Planning 속도를 높임
    -->
    <disable_collisions link1="${prefix}base_link" link2="${prefix}base_link_inertia" reason="Adjacent" />
    <disable_collisions link1="${prefix}base_link_inertia" link2="${prefix}shoulder_link" reason="Adjacent" />
    <disable_collisions link1="${prefix}tool0" link2="${prefix}wrist_1_link" reason="Never" />
    <disable_collisions link1="${prefix}tool0" link2="${prefix}wrist_2_link" reason="Never" />
    <disable_collisions link1="${prefix}tool0" link2="${prefix}wrist_3_link" reason="Adjacent" />
    <disable_collisions link1="${prefix}forearm_link" link2="${prefix}upper_arm_link" reason="Adjacent" />
    <disable_collisions link1="${prefix}forearm_link" link2="${prefix}wrist_1_link" reason="Adjacent" />
    <disable_collisions link1="${prefix}shoulder_link" link2="${prefix}upper_arm_link" reason="Adjacent" />
    <disable_collisions link1="${prefix}wrist_1_link" link2="${prefix}wrist_2_link" reason="Adjacent" />
    <disable_collisions link1="${prefix}wrist_1_link" link2="${prefix}wrist_3_link" reason="Never" />
    <disable_collisions link1="${prefix}wrist_2_link" link2="${prefix}wrist_3_link" reason="Adjacent" />

  </xacro:macro>
</robot>
```

### <ur_robotiq_macro.srdf.xacro>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<robot xmlns:xacro="http://wiki.ros.org/xacro">

  <!-- ===================================================== -->
  <!--   UR + Robotiq 2F-85 통합 SRDF (MoveIt용) 매크로      -->
  <!--   파일명: ur_robotiq_srdf.xacro                      -->
  <!-- ===================================================== -->

  <xacro:macro name="ur_robotiq_srdf" params="prefix">

    <!-- ============================= -->
    <!--  Include 서브 매크로 정의들   -->
    <!-- ============================= -->
    <xacro:include filename="$(find ur_robotiq_moveit_config)/srdf/ur_macro.srdf.xacro" />
    <xacro:include filename="$(find robotiq_description)/srdf/robotiq_2f_85_macro.srdf.xacro"/>

    <!-- ============================= -->
    <!--  UR 로봇 (팔) 구성            -->
    <!-- ============================= -->
    <xacro:ur_srdf name="ur" prefix="${prefix}" />

    <!-- ============================= -->
    <!--  Robotiq 2F-85 그리퍼 구성     -->
    <!-- ============================= -->
    <xacro:robotiq_2f_85_srdf prefix="${prefix}"/>

    <!-- ============================= -->
    <!--  전체 조합 그룹 정의           -->
    <!-- ============================= -->
    <!-- UR 매니퓰레이터 + Robotiq 그리퍼 통합 -->
    <group name="${prefix}ur_robotiq">
      <group name="${prefix}ur_manipulator"/>
      <group name="${prefix}robotiq_2f_85_gripper"/>
    </group>

    <!-- ============================= -->
    <!--  준비 자세 (Ready Pose) 정의   -->
    <!-- ============================= -->
    <group_state name="${prefix}ready" group="${prefix}ur_manipulator">
      <joint name="${prefix}elbow_joint" value="1.5707" />
      <joint name="${prefix}shoulder_lift_joint" value="-1.5707" />
      <joint name="${prefix}shoulder_pan_joint" value="0" />
      <joint name="${prefix}wrist_1_joint" value="-1.5707" />
      <joint name="${prefix}wrist_2_joint" value="-1.5707" />
      <joint name="${prefix}wrist_3_joint" value="0" />
    </group_state>

    <!-- ============================= -->
    <!--  End Effector 설정             -->
    <!-- ============================= -->
    <end_effector
      name="${prefix}robotiq_2f_85_gripper_ee"
      parent_link="${prefix}tool0"
      group="${prefix}robotiq_2f_85_gripper"
      parent_group="${prefix}ur_manipulator"/>

    <!-- ============================= -->
    <!--  Collision Disable 설정        -->
    <!-- ============================= -->
    <!-- 인접하거나 연결된 링크들 간의 불필요한 충돌 검사 비활성화 -->
    <!-- 무시해도 되는 링크들 적어놓은거 -->
    <disable_collisions link1="${prefix}robotiq_85_base_link" link2="${prefix}ur_to_robotiq_link" reason="Adjacent"/>
    <disable_collisions link1="${prefix}robotiq_85_left_finger_link" link2="${prefix}ur_to_robotiq_link" reason="Never"/>
    <disable_collisions link1="${prefix}robotiq_85_left_finger_tip_link" link2="${prefix}ur_to_robotiq_link" reason="Never"/>
    <disable_collisions link1="${prefix}robotiq_85_left_inner_knuckle_link" link2="${prefix}ur_to_robotiq_link" reason="Never"/>
    <disable_collisions link1="${prefix}robotiq_85_left_knuckle_link" link2="${prefix}ur_to_robotiq_link" reason="Never"/>
    <disable_collisions link1="${prefix}robotiq_85_right_finger_link" link2="${prefix}ur_to_robotiq_link" reason="Never"/>
    <disable_collisions link1="${prefix}robotiq_85_right_finger_tip_link" link2="${prefix}ur_to_robotiq_link" reason="Never"/>
    <disable_collisions link1="${prefix}robotiq_85_right_inner_knuckle_link" link2="${prefix}ur_to_robotiq_link" reason="Never"/>
    <disable_collisions link1="${prefix}robotiq_85_right_knuckle_link" link2="${prefix}ur_to_robotiq_link" reason="Never"/>
    <disable_collisions link1="${prefix}ur_to_robotiq_link" link2="${prefix}wrist_1_link" reason="Never"/>
    <disable_collisions link1="${prefix}ur_to_robotiq_link" link2="${prefix}wrist_2_link" reason="Never"/>
    <disable_collisions link1="${prefix}ur_to_robotiq_link" link2="${prefix}wrist_3_link" reason="Adjacent"/>

  </xacro:macro>
</robot>
```

<ur_robotiq.srdf.xacro>
```xml
<?xml version="1.0" encoding="UTF-8"?>
<robot xmlns:xacro="http://wiki.ros.org/xacro" name="ur_robotiq">

	<xacro:arg name="prefix" default="" />
	
	<xacro:include filename="$(find ur_robotiq_moveit_config)/srdf/ur_robotiq_macro.srdf.xacro"/>
<xacro:ur_robotiq_srdf prefix="$(arg prefix)"/>

</robot>
```

config 폴더 안에 파일
- base_frame.yaml : 어디에 고정 시켜 놓을지에 대한 정보
- controllers.yaml : 
- initial_positions.yaml :  joint 의 초기값이 적혀있음
- joint_limits.yaml : 로봇의 최대값 최솟값에 대한 정보
- kinematics.yaml : 내가 뭘 이용할 것이가?에 대한 정보
- moveit_controllers.yaml : moveit과 관련된 파일, moveit에서 실제 사용하는 컨트롤러
- moveit_cpp.yaml : 어떤한 알고리즘을 사용할지에 대한 정보
- ompl_planning.yaml : ompl(open motion palnning library) planning 과 관련된 파일
- pilz_cartesian_limits.yaml : 어떤 회사 알고리즘
- planning_pipelines_config.yaml
- servo.yaml : moveit과 gazebo사용할때 필요한 파라미터
- visual_parameters.yaml : gazebo나 rviz2에 올릴 때 어떤 걸쓸지에 대한 정보


### <controllers.yaml >
```yaml
# ros2_control uses this configuration for controller management
# This file is only for simulation

controller_manager:
  ros__parameters:
    update_rate: 100  # Hz

    joint_state_broadcaster:
      type: joint_state_broadcaster/JointStateBroadcaster

    ur_arm_controller:
      type: joint_trajectory_controller/JointTrajectoryController

    forward_velocity_controller:
      type: velocity_controllers/JointGroupVelocityController

    forward_position_controller:
      type: position_controllers/JointGroupPositionController

    gripper_controller:
      type: position_controllers/GripperActionController


# -----------------------------------------------------------------
# Arm controller configuration
ur_arm_controller:
  ros__parameters:
    joints:
    #아래 6개의 joint대로 움직이겠다
      - shoulder_pan_joint
      - shoulder_lift_joint
      - elbow_joint
      - wrist_1_joint
      - wrist_2_joint
      - wrist_3_joint
    command_interfaces:
    #내가 이 joint 가 어디로 갔으면 좋겠는지 정보를 적어 넣은 것
      - position
    state_interfaces:
    #로봇이 움직이는 동안 어떤한 정보를 붙이고 있을지에 대한 내용
      - position
      - velocity
    state_publish_rate: 100.0
    action_monitor_rate: 20.0
    allow_partial_joints_goal: false
    constraints:
      stopped_velocity_tolerance: 0.2
      goal_time: 0.0
      shoulder_pan_joint:   { trajectory: 0.2, goal: 0.1 }
      shoulder_lift_joint:  { trajectory: 0.2, goal: 0.1 }
      elbow_joint:          { trajectory: 0.2, goal: 0.1 }
      wrist_1_joint:        { trajectory: 0.2, goal: 0.1 }
      wrist_2_joint:        { trajectory: 0.2, goal: 0.1 }
      wrist_3_joint:        { trajectory: 0.2, goal: 0.1 }


# -----------------------------------------------------------------
# Velocity controller for teleoperation / testing
forward_velocity_controller:
  ros__parameters:
    joints:
      - shoulder_pan_joint
      - shoulder_lift_joint
      - elbow_joint
      - wrist_1_joint
      - wrist_2_joint
      - wrist_3_joint
    interface_name: velocity


# -----------------------------------------------------------------
# Position controller for direct joint position commands
forward_position_controller:
  ros__parameters:
    joints:
      - shoulder_pan_joint
      - shoulder_lift_joint
      - elbow_joint
      - wrist_1_joint
      - wrist_2_joint
      - wrist_3_joint


# -----------------------------------------------------------------
# Robotiq 2F-85 gripper controller
gripper_controller:
  ros__parameters:
    joint: robotiq_85_left_knuckle_joint
```


## 9, 10, 11. launch 0, 1, 2
launch 폴더 안에 파일 
-  ur_robotiq_control.launch.py
- ur_robotiq_moveit.launch.py
- ur_robotiq.launch.py

### <ur_robotiq.launch.py>
```python
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    OpaqueFunction,
)
from launch.conditions import IfCondition, UnlessCondition
from launch.event_handlers import OnProcessExit, OnProcessStart
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import (
    Command,
    FindExecutable,
    FindPackageShare,
    LaunchConfiguration,
    PathJoinSubstitution,
    IfElseSubstitution,
)
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
from moveit_configs_utils import MoveItConfigsBuilder
import os


def generate_launch_description():
    """Launch file to bring up UR + Robotiq robot simulation with MoveIt and Gazebo."""
    declared_arguments = []

    # --------------------------------------------------------------------------
    # Simulation and configuration arguments
    # --------------------------------------------------------------------------
    declared_arguments.append(
        DeclareLaunchArgument(
            "runtime_config_package",
            default_value="ur_robotiq_moveit_config",
            description=(
                "Package with the controller's configuration in 'config' folder. "
                "Usually the argument is not set; it enables the use of a custom setup."
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "controllers_file",
            default_value="controllers.yaml",
            description="YAML file with the controllers configuration.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "description_package",
            default_value="ur_robotiq_moveit_config",
            description=(
                "Description package with robot URDF/Xacro files. Usually the argument "
                "is not set, it enables use of a custom description."
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "description_file",
            default_value="ur_robotiq.urdf.xacro",
            description="URDF/Xacro description file with the robot.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "gazebo_world_file_path",
            default_value=os.path.join(
                get_package_share_directory("ur_robotiq_moveit_config"),
                "gazebo",
                "workstation.world",
            ),
            description="Gazebo world file with the robot.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "prefix",
            default_value='""',
            description=(
                "Prefix of the joint names, useful for multi-robot setup. "
                'Expected format "<prefix>/".'
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "namespace",
            default_value="",
            description=(
                "Namespace of launched nodes, useful for multi-robot setup. "
                'Expected format "<ns>/".'
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "sim_gazebo",
            default_value="true",
            description="Start robot in Gazebo simulation.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "use_fake_hardware",
            default_value="false",
            description="Start robot with fake hardware mirroring commands to its states.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "use_planning",
            default_value="true",
            description="Start robot with MoveIt2 `move_group` planning config (Pilz and OMPL).",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "arm_controller",
            default_value="ur_arm_controller",
            description="Arm controller to start.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "gripper_controller",
            default_value="gripper_controller",
            description="Gripper controller to start.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "start_rviz",
            default_value="true",
            description="Start RViz2 automatically with this launch file.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "rviz_config_file",
            default_value="ur_robotiq.rviz",
            description="Rviz2 configuration file.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "initial_positions_file",
            default_value="initial_positions.yaml",
            description="Configuration file for robot initial positions in simulation.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "base_frame_file",
            default_value="base_frame.yaml",
            description="Configuration file for robot base frame wrt world.",
        )
    )

    # Duplicate (safe to include for completeness)
    declared_arguments.append(
        DeclareLaunchArgument(
            "description_package",
            default_value="ur_robotiq_moveit_config",
            description=(
                "Description package with robot URDF/Xacro files. Usually the argument "
                "is not set, it enables use of a custom description."
            ),
        )
    )

    return LaunchDescription(declared_arguments + [OpaqueFunction(function=launch_setup)])


def launch_setup(context, *args, **kwargs):
    """Launch Gazebo control and MoveIt configuration for UR + Robotiq."""
    
    # --------------------------------------------------------------------------
    # UR control (ros2_control + Gazebo)
    # --------------------------------------------------------------------------
    ur_control_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("ur_robotiq_moveit_config"),
                "launch",
                "ur_robotiq_control.launch.py"
                #여기서 파일 1개
            ])
        ),
        launch_arguments={
            "use_sim_time": "true",
            "launch_rviz": "false",
        }.items(),
    )

    # --------------------------------------------------------------------------
    # MoveIt configuration (planning + RViz)
    # --------------------------------------------------------------------------
    ur_moveit_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("ur_robotiq_moveit_config"),
                "launch",
                "ur_robotiq_moveit.launch.py"
                #여기서 파일 또 다른 1개 실행
            ])
        ),
        launch_arguments={
            "use_sim_time": "true",
            "launch_rviz": "true",
        }.items(),
    )

    # --------------------------------------------------------------------------
    # Final nodes to launch
    # --------------------------------------------------------------------------
    nodes_to_launch = [
        ur_control_launch,
        ur_moveit_launch,
    ]

    return nodes_to_launch
```

### <ur_robotiq_control.launch.py>
```python
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    RegisterEventHandler,
    SetEnvironmentVariable,
    TimerAction,
    OpaqueFunction,
)
from launch.event_handlers import OnProcessExit, OnProcessStart
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory

from pathlib import Path
import os
import subprocess


def generate_launch_description():
    # Declare arguments
    declared_arguments = []

    declared_arguments.append(
        DeclareLaunchArgument(
            "runtime_config_package",
            default_value="ur_robotiq_moveit_config",
            description=(
                "Package with the controller's configuration in 'config' folder. "
                "Usually the argument is not set, it enables use of a custom setup."
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "controllers_file",
            default_value="controllers.yaml",
            description="YAML file with the controllers configuration.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "description_package",
            default_value="ur_robotiq_moveit_config",
            description=(
                "Description package with robot URDF/xacro files. Usually the argument "
                "is not set, it enables use of a custom description."
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "description_file",
            default_value="ur_robotiq.urdf.xacro",
            description="URDF/XACRO description file with the robot.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "gazebo_world_file",
            default_value="workstation.sdf",
            description="gazebo world file with the robot",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "prefix",
            default_value='""',
            description=(
                "Prefix of the joint names, useful for multi-robot setup. "
                'If changed then also joint names in the controllers configuration have to be updated. '
                'Expected format "<prefix>/"'
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "namespace",
            default_value="",
            description=(
                "Namespace of launched nodes, useful for multi-robot setup. "
                'If changed then also the namespace in the controllers configuration needs to be updated. '
                'Expected format "<ns>/".'
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "sim_gazebo",
            default_value="true",
            description="Start robot in Gazebo simulation.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "use_fake_hardware",
            default_value="false",
            description="Start robot with fake hardware mirroring command to its states.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "use_planning",
            default_value="true",
            description=(
                "Start robot with Moveit2 `move_group` planning "
                "config for Pilz and OMPL."
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "arm_controller",
            default_value="ur_arm_controller",
            description="arm controller to start.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "gripper_controller",
            default_value="gripper_controller",
            description="gripper controller to start.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "start_rviz",
            default_value="true",
            description="Start RViz2 automatically with this launch file.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "rviz_config_file",
            default_value="ur_robotiq.rviz",
            description="Rviz file",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "initial_positions_file",
            default_value="initial_positions.yaml",
            description="Configuration file of robot initial positions for simulation.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "base_frame_file",
            default_value="base_frame.yaml",
            description="Configuration file of robot base frame wrt World.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "description_package",
            default_value="ur_robotiq_moveit_config",
            description=(
                "Description package with robot URDF/xacro files. Usually the argument "
                "is not set, it enables use of a custom description."
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "use_sim_time",
            default_value="true",
            description=(
                "Use simulated time from Gazebo/IGN for ROS nodes."
            ),
        )
    )

    # Initialize Arguments
    runtime_config_package = LaunchConfiguration("runtime_config_package")
    controllers_file = LaunchConfiguration("controllers_file")
    description_package = LaunchConfiguration("description_package")
    description_file = LaunchConfiguration("description_file")
    gazebo_world_file = LaunchConfiguration("gazebo_world_file")
    prefix = LaunchConfiguration("prefix")
    namespace = LaunchConfiguration("namespace")
    sim_gazebo = LaunchConfiguration("sim_gazebo")
    use_planning = LaunchConfiguration("use_planning")
    arm_controller = LaunchConfiguration("arm_controller")
    gripper_controller = LaunchConfiguration("gripper_controller")
    start_rviz = LaunchConfiguration("start_rviz")
    rviz_config_file = LaunchConfiguration("rviz_config_file")
    initial_positions_file = LaunchConfiguration("initial_positions_file")
    base_frame_file = LaunchConfiguration("base_frame_file")
    use_sim_time = LaunchConfiguration("use_sim_time")

    # File paths
    controllers_file_path = PathJoinSubstitution(
        [FindPackageShare(description_package), "config", controllers_file]
    )
    initial_positions_file_path = PathJoinSubstitution(
        [FindPackageShare(runtime_config_package), "config", initial_positions_file]
    )
    rviz_config_file_path = PathJoinSubstitution(
        [FindPackageShare(runtime_config_package), "rviz", rviz_config_file]
    )
    base_frame_file_path = PathJoinSubstitution(
        [FindPackageShare(runtime_config_package), "config", base_frame_file]
    )

    # Build robot_description by processing xacro
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution([FindPackageShare(description_package), "urdf", description_file]),
            " ",
            "ur_type:=",
            "ur5e",
            " ",
            "sim_gazebo:=",
            sim_gazebo,
            " ",
            "simulation_controllers:=",
            controllers_file_path,
            " ",
            "initial_positions_file:=",
            initial_positions_file_path,
            " ",
            "base_frame_file:=",
            base_frame_file_path,
        ]
    )
    robot_description = {"robot_description": robot_description_content}

    # Nodes
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[{"use_sim_time": use_sim_time}, robot_description],
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            [namespace, "controller_manager"],
        ],
    )

    arm_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[arm_controller, "--controller-manager", [namespace, "controller_manager"]],
    )

    gripper_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[gripper_controller, "--controller-manager", [namespace, "controller_manager"]],
    )

    # Delay start of robot controllers after joint_state_broadcaster
    # joint_state_broadcaster_spawner이 시작 되어야지(먼저!!) arm_controller_spawner, gripper_controller_spawner이 실행(나중!!)이 됨
    delay_robot_controller_spawner_after_joint_state_broadcaster_spawner = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[arm_controller_spawner, gripper_controller_spawner],
        )
    )

    arm_robot_sim_path = os.path.join(get_package_share_directory("ur_robotiq_moveit_config"))

    gazebo_resource_path = SetEnvironmentVariable(
        name="GZ_SIM_RESOURCE_PATH",
        value=[
            os.path.join(arm_robot_sim_path, "worlds"),
            ":" + str(Path(arm_robot_sim_path).parent.resolve()),
        ],
    )

    spawn_entity = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=[
            "-string",
            robot_description_content,
            # "-name", "ur",
            # "-allow_renaming", "true",
        ],
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [FindPackageShare("ros_gz_sim"), "/launch/gz_sim.launch.py"]
        ),
        launch_arguments=[
            (
                "gz_args",
                [
                    PathJoinSubstitution([FindPackageShare(description_package), "worlds", gazebo_world_file]),
                    " -v 4",
                    " -r",
                    " --physics-engine gz-physics-bullet-featherstone-plugin",
                ],
            )
        ],
    )

    # Make the /clock topic available in ROS
    # time과 관련된내용이랑 반드시 넣어줘야함
    gz_sim_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock",
        ],
        output="screen",
    )

    nodes = [
        gazebo_resource_path,
        robot_state_publisher_node,
        joint_state_broadcaster_spawner,
        delay_robot_controller_spawner_after_joint_state_broadcaster_spawner,
        spawn_entity,
        gazebo,
        gz_sim_bridge,
    ]

    return LaunchDescription(declared_arguments + nodes)

```

### <ur_robotiq_moveit.launch.py>
```python
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    RegisterEventHandler,
    OpaqueFunction,
)
from launch.conditions import IfCondition
from launch.event_handlers import OnProcessExit, OnProcessStart
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
from moveit_configs_utils import MoveItConfigsBuilder
from pathlib import Path
import os
import yaml


# ---------------------------------------------------------------------------- #
# Helper function: Load YAML configuration files
# ---------------------------------------------------------------------------- #
def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)

    try:
        with open(absolute_file_path) as file:
            return yaml.safe_load(file)
    except OSError:
        return None


# ---------------------------------------------------------------------------- #
# Main Launch Description
# ---------------------------------------------------------------------------- #
def generate_launch_description():
    # ---------------------------
    # Declare Launch Arguments
    # ---------------------------
    declared_arguments = []

    declared_arguments.append(
        DeclareLaunchArgument(
            "runtime_config_package",
            default_value="ur_robotiq_moveit_config",
            description=(
                "Package with the controller's configuration in 'config' folder. "
                "Usually the argument is not set, it enables use of a custom setup."
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "description_package",
            default_value="ur_robotiq_moveit_config",
            description=(
                "Description package with robot URDF/xacro files. "
                "Usually not set, allows for a custom robot description."
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "description_file",
            default_value="ur_robotiq.urdf.xacro",
            description="URDF/Xacro description file for the robot.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "prefix",
            default_value='""',
            description=(
                "Prefix of the joint names, useful for multi-robot setups. "
                'Expected format "<prefix>/".'
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "namespace",
            default_value="",
            description=(
                "Namespace of launched nodes, useful for multi-robot setups. "
                'Expected format "<ns>/".'
            ),
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "start_rviz",
            default_value="true",
            description="Start RViz2 automatically with this launch file.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "rviz_config_file",
            default_value="dual_ur_robotiq.rviz",
            description="RViz configuration file.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "use_sim_time",
            default_value="true",
            description="Use simulated time (from Gazebo or Ignition).",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "base_frame_file",
            default_value="base_frame.yaml",
            description="Configuration file for the robot base frame wrt World.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "warehouse_sqlite_path",
            default_value=os.path.expanduser("~/.ros/warehouse_ros.sqlite"),
            description="Path to MoveIt warehouse SQLite database.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "launch_servo",
            default_value="false",
            description="Launch MoveIt Servo node?",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "test_mode",
            default_value="true",
            description="Run MoveIt Python API tutorial node?",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "test_name",
            default_value="motion_test_arm",
            description="Python API tutorial filename to execute.",
        )
    )

    # ---------------------------
    # Initialize Launch Configs
    # ---------------------------
    runtime_config_package = LaunchConfiguration("runtime_config_package")
    description_package = LaunchConfiguration("description_package")
    description_file = LaunchConfiguration("description_file")
    prefix = LaunchConfiguration("prefix")
    start_rviz = LaunchConfiguration("start_rviz")
    rviz_config_file = LaunchConfiguration("rviz_config_file")
    base_frame_file = LaunchConfiguration("base_frame_file")
    namespace = LaunchConfiguration("namespace")
    use_sim_time = LaunchConfiguration("use_sim_time")
    warehouse_sqlite_path = LaunchConfiguration("warehouse_sqlite_path")
    launch_servo = LaunchConfiguration("launch_servo")
    test_name = LaunchConfiguration("test_name")
    test_mode = LaunchConfiguration("test_mode")

    # ---------------------------
    # Build MoveIt Config
    # ---------------------------
    base_package_name = "ur_robotiq_moveit_config"
#=====================================================================
	#이 부분이 어디론가 들어가야하는데 moveit과 관련된 설정을 다 넣어둠
    moveit_config = (
    
        MoveItConfigsBuilder(robot_name="ur_robotiq")
        #MoveItConfigsBuilder는 ur_robotiq이라는 이름의 패키지를 찾아라!!
        .robot_description(Path("urdf") / "ur_robotiq.urdf.xacro")
        .robot_description_semantic(Path("srdf") / "ur_robotiq.srdf.xacro")
        .moveit_cpp(
            file_path=get_package_share_directory(base_package_name)
            + "/config/moveit_cpp.yaml"
        )
        .to_moveit_configs()
    )

    # ---------------------------
    # MoveIt Python Control Node
    # ---------------------------
    moveit_py_node = Node(
        name="moveit_py",
        package="ur_robotiq_moveit_config",
        executable="ur_robotiq_controller.py",
        output="both",
        parameters=[
            moveit_config.to_dict(),
            {"use_sim_time": use_sim_time},
        ],
        condition=IfCondition(test_mode),
    )

    # ---------------------------
    # MoveIt Warehouse Configuration
    # ---------------------------
    warehouse_ros_config = {
        "warehouse_plugin": "warehouse_ros_sqlite::DatabaseConnection",
        "warehouse_host": warehouse_sqlite_path,
    }

    # ---------------------------
    # Wait for robot_description before move_group
    # ---------------------------
    wait_robot_description = Node(
        package="ur_robot_driver",
        executable="wait_for_robot_description",
        #wait_for_robot_description이게 실행이 안되면 다른 것도 실행시키지 말아라!
        output="screen",
    )

    # ---------------------------
    # Move Group Node
    # ---------------------------
    move_group_node = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",
        parameters=[
            moveit_config.to_dict(),
            warehouse_ros_config,
            {
                "use_sim_time": use_sim_time,
                "publish_robot_description": True,
                "publish_robot_description_semantic": True,
            },
        ],
    )

    # ---------------------------
    # MoveIt Servo Node
    # ---------------------------
    servo_yaml = load_yaml(base_package_name, "config/servo.yaml")
    servo_params = {"moveit_servo": servo_yaml}

    servo_node = Node(
        package="moveit_servo",
        executable="servo_node",
        output="screen",
        condition=IfCondition(launch_servo),
        parameters=[
            moveit_config.to_dict(),
            servo_params,
        ],
    )

    # ---------------------------
    # RViz Node
    # ---------------------------
    rviz_config = PathJoinSubstitution(
        [FindPackageShare(base_package_name), "rviz", "ur_robotiq.rviz"]
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2_moveit",
        output="log",
        arguments=["-d", rviz_config],
        parameters=[
            moveit_config.robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.robot_description_kinematics,
            moveit_config.planning_pipelines,
            moveit_config.joint_limits,
            warehouse_ros_config,
            {"use_sim_time": use_sim_time},
        ],
        condition=IfCondition(start_rviz),
    )

    # ---------------------------
    # Launch Description
    # ---------------------------
    ld = LaunchDescription()
    ld.add_entity(LaunchDescription(declared_arguments))

    # Wait for robot_description before launching MoveIt nodes
    ld.add_action(wait_robot_description)
    ld.add_action(
        RegisterEventHandler(
            OnProcessExit(
                target_action=wait_robot_description,
                on_exit=[move_group_node, rviz_node, servo_node, moveit_py_node],
            )
        ),
    )

    return ld
```
## 12. build And Run
$ colcon build --symlink-install --allow-overriding ur_description

## 13. pickNplace

## 14. 원리 설명

## 15. 마무리



# Chapter 8. Mobile Robot(Nav2)

## 1. Nav2 개요

## 2. Nav2 미니 실습 개요

## 3. Nav2 설명

## 4. 2D Pose

## 5. 마무리


# Chapter 9. Mobile Robot(Nav2) 실습

## 1. 실습 개요

## 2. 코드 구조

## 3. launch

## 4. launch2

## 5. 파일 확인

## 6. 빌드

## 7. SLAM

## 8. 마무리


# Chapter 10. Mobile Manipulator 실습

## 1. MM실습 개요

## 2. 배경지식

## 3. 패키지 분석

## 4. xacro

## 5. 환경

## 6. task

## 7. 실행

## 8. 마무리




