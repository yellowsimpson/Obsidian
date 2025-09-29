
- 공부해야 될것들
1. 수학에 대해 알아야함
2. 리눅스
3. 파이썬
	토픽
	리스트
	튜플
	+
	numpy
	class
	생성자
	return 값  어떻게 주는지
	numpy 공부 할것!!
4. 머신러닝 
	회귀 분석
	지도학습
	비지도학습
5. 랠루
6. pid제어

framework
	-> ros(robot os)

과제
1. 리눅스에 대해 배워라
2. urdf
3. ros2에서 어떤게 실시간 제어 일까?
4. 퍼셉트론 공부

로봇을 구성하고 있는 것
1. 조인트(joint)
2. 링크(link)

<ros1과 ros2 차이점>
- ros1
단일 로봇
실시간 제어 지원하지 않음
안정된 네트워크 환경 요구
단일 플랫폼
주로 대학이나 연구소 등의 아케데믹 연구 용도

- ros2
복수대의 로봇
실시간 제어
불안정한 네트워크 환경에서도 동작할 수 있는 유연함
멀티 플랫폼(Linux, Windows, MacOs)
최신 기술 지원(zeroconf, Protocol,...)
상업용 제품 제원


QOS란?
**QoS(Quality of Service, 서비스 품질)** 는 __네트워크에서 특정 트래픽(데이터 흐름)에 대해 우선순위를 주거나 성능을 보장하는 기술/개념__ 을 말합니다.

즉, 네트워크가 모든 데이터를 똑같이 취급하는 것이 아니라, **중요한 데이터는 더 빠르고 안정적으로 전송되도록 관리**하는 거예요.

우분투 노트북에 ros2 설치해놔

ROS(통신 프로토콜!!)
ros 공식 사이트
https://docs.ros.org/en/humble/Installation.html 

ros 구성요소
- 노드: 실행할 수 있는 프로그램 단위
---
- 토픽
- 서비스
- 액션

```c
ros2 node list
	->엔트리 포인터, node에는 main함수가 있음
ros2 topic list
ros2 service list
ros2 action list
	-> 인터페이스
```

Debuab으로 깔아야되
ros2 CLI에 대해서 공부해야되

##  Install ROS 2 packages
Update your apt repository caches after setting up the repositories.
```python
sudo apt update
```

ROS 2 packages are built on frequently updated Ubuntu systems. It is always recommended that you ensure your system is up to date before installing new packages.
```python
sudo apt upgrade
```
Warning

Due to early updates in Ubuntu 22.04 it is important that `systemd` and `udev`-related packages are updated before installing ROS 2. The installation of ROS 2’s dependencies on a freshly installed system without upgrading can trigger the **removal of critical system packages**.

Please refer to [ros2/ros2#1272](https://github.com/ros2/ros2/issues/1272) and [Launchpad #1974196](https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1974196) for more information.
Desktop Install (Recommended): ROS, RViz, demos, tutorials.
```python
sudo apt install ros-humble-desktop
```
ROS-Base Install (Bare Bones): Communication libraries, message packages, command line tools. No GUI tools.
```python
sudo apt install ros-humble-ros-base
```
Development tools: Compilers and other tools to build ROS packages
```python
sudo apt install ros-dev-tools
```
## Environment setup
### Sourcing the setup script
Set up your environment by sourcing the following file.
```python
source /opt/ros/humble/setup.bash
```
```
Note

Replace `.bash` with your shell if you’re not using bash. Possible values are: `setup.bash`, `setup.sh`, `setup.zsh`.
```

## Try some examples(ros2 listener / talker 실습)

### Talker-listener
If you installed `ros-humble-desktop` above you can try some examples.
First, if you use `Zenoh` as the RMW implementation, you will require a router for node discovery and communication.
In one terminal, start the Zenoh router daemon:
```python
source /opt/ros/humble/setup.bash
ros2 run rmw_zenoh_cpp rmw_zenohd
```
In another terminal, source the setup file and then run a C++ `talker`:
```python
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker
```
In a third terminal source the setup file and then run a Python `listener`:
```python
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_py listener
```
You should see the `talker` saying that it’s `Publishing` messages and the `listener` saying `I heard` those messages. This verifies both the C++ and Python APIs are working properly. Hooray!

# Task 
### 1 Install turtlesim
As always, start by sourcing your setup files in a new terminal, as described in the [previous tutorial](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html).

Install the turtlesim package for your ROS 2 distro:
```python
sudo apt update
sudo apt install ros-humble-turtlesim
```
To check if the package is installed, run the following command, which should return a list of turtlesim’s executables:

```python
ros2 pkg executables turtlesim
turtlesim draw_square
turtlesim mimic
turtlesim turtle_teleop_key
turtlesim turtlesim_node
```

### 2 Start turtlesim
To start turtlesim, enter the following command in your terminal:
```python
ros2 run turtlesim turtlesim_node

[INFO] [turtlesim]: Starting turtlesim with node name /turtlesim
[INFO] [turtlesim]: Spawning turtle [turtle1] at x=[5.544445], y=[5.544445], theta=[0.000000]
```

__ros2 프로그램을 어떻게 실행시킵니까?
	-> ros2 run 패키지이름 노드 이름


Under the command, you will see messages from the node. There you can see the default turtle’s name and the coordinates where it spawns.

The simulator window should appear, with a random turtle in the center.

![../../../_images/turtlesim.png](https://docs.ros.org/en/humble/_images/turtlesim.png)


###  3 Use turtlesim
Open a new terminal and source ROS 2 again.
Now you will run a new node to control the turtle in the first node:
ros2 run turtlesim turtle_teleop_key

At this point you should have three windows open: a terminal running `turtlesim_node`, a terminal running `turtle_teleop_key` and the turtlesim window. Arrange these windows so that you can see the turtlesim window, but also have the terminal running `turtle_teleop_key` active so that you can control the turtle in turtlesim.

Use the arrow keys on your keyboard to control the turtle. It will move around the screen, using its attached “pen” to draw the path it followed so far.

Note
```
Pressing an arrow key will only cause the turtle to move a short distance and then stop. This is because, realistically, you wouldn’t want a robot to continue carrying on an instruction if, for example, the operator lost the connection to the robot.

You can see the nodes, and their associated topics, services, and actions, using the `list` subcommands of the respective commands:
```
```python
ros2 node list
ros2 topic list
ros2 service list
ros2 action list
```
You will learn more about these concepts in the coming tutorials. Since the goal of this tutorial is only to get a general overview of turtlesim, you will use rqt to call some of the turtlesim services and interact with `turtlesim_node`.

### 4 Install rqt
Open a new terminal to install `rqt` and its plugins:

Ubuntu LinuxmacOSWindows
```python
sudo apt update
sudo apt install '~nros-humble-rqt*'
```
To run rqt:
```python
rqt
```
### 5 Use rqt
When running rqt for the first time, the window will be blank. No worries; just select **Plugins** > **Services** > **Service Caller** from the menu bar at the top.

Note
```
It may take some time for rqt to locate all the plugins. If you click on **Plugins** but don’t see **Services** or any other options, you should close rqt and enter the command `rqt --force-discover` in your terminal.
```

Type: integer8, 16 ... , float boolean: 기본 타입
list, array, buffer

![../../../_images/rqt.png](https://docs.ros.org/en/humble/_images/rqt.png)

-> clear 라는 serivce를 요청해줘(caller) 그리고 response 된거 보여줘

__여기서 외워야 할것!!
-> service => call을 통해서 호출__


Use the refresh button to the left of the **Service** dropdown list to ensure all the services of your turtlesim node are available.
Click on the **Service** dropdown list to see turtlesim’s services, and select the `/spawn` service.

#### 5.1 Try the spawn service (spawn 무언가를 만들어 내는것)
__-> 어떤 로봇을 하나더 만들어라!! 할때 사용__
Let’s use rqt to call the `/spawn` service. You can guess from its name that `/spawn` will create another turtle in the turtlesim window.
Give the new turtle a unique name, like `turtle2`, by double-clicking between the empty single quotes in the **Expression** column. You can see that this expression corresponds to the value of **name** and is of type **string**.
Next enter some valid coordinates at which to spawn the new turtle, like `x = 1.0` and `y = 1.0`.

![../../../_images/spawn.png](https://docs.ros.org/en/humble/_images/spawn.png)

-> request 할때 topic 이름이 있어야되 serive 실행 시킬려면 call 해야되 
지금 service 안에 x, y, theta, name 이라는 내용이 들어가 있음!

x, y, 는 위치
1.0, 0.0은 각도

보통 로봇을 다룰 때 6가지의 요소가 있음
x,y,z, row, pitch, low

Note
```
If you try to spawn a new turtle with the same name as an existing turtle, like the default `turtle1`, you will get an error message in the terminal running `turtlesim_node`:
[ERROR] [turtlesim]: A turtle named [turtle1] already exists
To spawn `turtle2`, you then need to call the service by clicking the **Call** button on the upper right side of the rqt window.
If the service call was successful, you should see a new turtle (again with a random design) spawn at the coordinates you input for **x** and **y**.
If you refresh the service list in rqt, you will also see that now there are services related to the new turtle, `/turtle2/...`, in addition to `/turtle1/...`.
```
#### 5.2 Try the set_pen service
Now let’s give `turtle1` a unique pen using the `/set_pen` service:

![../../../_images/set_pen.png](https://docs.ros.org/en/humble/_images/set_pen.png)

The values for **r**, **g** and **b**, which are between 0 and 255, set the color of the pen `turtle1` draws with, and **width** sets the thickness of the line.

To have `turtle1` draw with a distinct red line, change the value of **r** to 255, and the value of **width** to 5. Don’t forget to call the service after updating the values.

If you return to the terminal where `turtle_teleop_key` is running and press the arrow keys, you will see `turtle1`’s pen has changed.

![../../../_images/new_pen.png](https://docs.ros.org/en/humble/_images/new_pen.png)

You’ve probably also noticed that there’s no way to move `turtle2`. That’s because there is no teleop node for `turtle2`.

### 6 Remapping
You need a second teleop node in order to control `turtle2`. However, if you try to run the same command as before, you will notice that this one also controls `turtle1`. The way to change this behavior is by remapping the `cmd_vel` topic.

In a new terminal, source ROS 2, and run:
```python
ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=turtle2/cmd_vel
```
Now, you can move `turtle2` when this terminal is active, and `turtle1` when the other terminal running `turtle_teleop_key` is active.

![../../../_images/remap.png](https://docs.ros.org/en/humble/_images/remap.png)

### 7 Close turtlesim
To stop the simulation, you can enter `Ctrl + C` in the `turtlesim_node` terminal, and `q` in the `turtle_teleop_key` terminals.

## Summary
Using turtlesim and rqt is a great way to learn the core concepts of ROS 2.



[[ROS2_기초강의_첫날(0929).pdf]]

ros2 안에 DDS가 있다!!




