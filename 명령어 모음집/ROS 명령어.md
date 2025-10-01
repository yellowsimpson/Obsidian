
__ROS 버전__
- 20.04: foxy
- 22.04: humble
- 24.04: Jazzy Jalisco

__Ubuntu 버전__
- 20.04: Focal Fossa -> focal
- 22.04: Jammy Jellyfish -> jammy
- 24.04: Noble Numbat -> noble
 
__초기 업데이트 명령어__ 
$sudo apt update
$sudo apt upgrade

__ros 설치 명령어__
$sudo apt install ros-humble-desktop
$sudo apt install ros-humble-ros-base
$sudo apt install ros-dev-tools

__setup.bash 여는 명령어__
$source /opt/ros/humble/setup.bash
:터미널 처음 열때 치는 명령어
*-> 귀찮으면 .bashrc에 내용 포함해!*

__ROS2 여는 명령어__
$ros2 run <패키지 이름> <노드 이름>
$ros2 launch <패키지 이름> <런치파일 이름>
$ros2 run rmw_zenoh_cpp rmw_zenohd
:rmw_zenohd노드 실행 명령어
$source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker
: talker 실행
$source /opt/ros/humble/setup.bash
ros2 run demo_nodes_py listener
: listener 실행

__rqt__
$rqt_graph
:현재 통신 상태 보여주는 명령어

__Turtlesim__
$sudo apt update
sudo apt install ros-humble-turtlesim
: Turtlesim 설치 명령어

$ros2 run turtlesim turtlesim_node
$ros2 run turtlesim turtle_teleop_key
:동작 확인

$ros2 pkg executables turtlesim
turtlesim draw_square
turtlesim mimic

__각각의 터미널에서 아래 두개 틀어줘__
$turtlesim turtlesim_node
: 거북이 있는 화면 나옴
$turtlesim turtle_teleop_key
: 키로 거북이를 조절 할 수 있음

__새로운 터미널에서 아래 명령어로 거북이 조절 가능!!__
$ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 0.0}}" -1
: x(거리)와 z(각도)값을 조절하여 거북이 조절

__node__
$ros2 node list
:실행 중인 노드 이름 표시
$ros2 node info
:실행중인 노드 정보 표시

__Topic__
$ros2 topic list
:실행중인 토픽 이름 표시
$ros2 topic info
:실행중인 토픽 정보 표시
$ros3 topic type
:실행중인 토픽 타입 표시
$ros2 topic echo
:특정 토픽을 터미널에 표시
$ros2 topic pub
:특정 토픽 값을 발행
$ros2 topic bw
:지정 토픽의 대역폭 측정
$ros2 topic delay
:지정 토픽의 지연시간 측정
$ros2 topic find
:지정 타입을 사용하는 토픽 이름 출력
$ros2 topic hz
:지정 토픽의 주기 측정

__Serivce__
$ros2 service list
:실행중인 서비스 이름 표시
$ros2 service type
:실행중인 서비스 타입 표시
$ros2 service call
:특정 서비스 호출
$ros2 service find
:지정 서비스 타입의 서비스 출력

__Action__
$ros2 action list
:실행중인 액션의 이름 표시
$ros2 action info
:실행중인 액션의 정보 표시
$ros2 action goal
:액션의 목표 지정

__Parameter__
$rps2 param list
:파라미터 목록 확인
$rps2 param describe
	*ros2 param describe <노드 이름> <파라미터 이름>*
:파라미터 내용 확인
$rps2 param lget
	*ros2 param get <노드 이름> <파라이머터 이름>*
:파라미터 읽기
$rps2 param set
	*ros2 param set <노드 이름> <파라이머터 이름> <값>*
:파라미터 쓰기
$rps2 param dump
	*ros2 param dump <노드 이름>*
:파라미터 저장
$rps2 param delete
	*ros2 param delete <노드 이름> <파라이머터 이름>*
:파라미터 삭제



__dd
$ros2 llaunch <패키지 이름> <노드 이름>