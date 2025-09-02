from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, RegisterEventHandler
from launch.event_handlers import OnProcessExit, OnProcessStart
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import os
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable, TimerAction
from pathlib import Path


from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
)
import subprocess

def generate_launch_description():
    # Declare arguments
    declared_arguments = []

   
    declared_arguments.append(
        DeclareLaunchArgument(
            'runtime_config_package',
            default_value='ur_robotiq_moveit_config',
            description='Package with the controller\'s configuration in "config" folder. \
                         Usually the argument is not set, it enables use of a custom setup.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'controllers_file',
            default_value='controllers.yaml',
            description='YAML file with the controllers configuration.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'description_package',
            default_value='ur_robotiq_moveit_config',
            description='Description package with robot URDF/xacro files. Usually the argument \
                         is not set, it enables use of a custom description.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'description_file',
            default_value='ur_robotiq.urdf.xacro',
            description='URDF/XACRO description file with the robot.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'gazebo_world_file',
            default_value="workstation.sdf",
            description='gazebo world file with the robot',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'prefix',
            default_value='""',
            description='Prefix of the joint names, useful for multi-robot setup. \
                         If changed than also joint names in the controllers \
                         configuration have to be updated. Expected format "<prefix>/"',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'namespace',
            default_value='',
            description='Namespace of launched nodes, useful for multi-robot setup. \
                         If changed than also the namespace in the controllers \
                         configuration needs to be updated. Expected format "<ns>/".',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'sim_gazebo',
            default_value='true',
            description='Start robot in Gazebo simulation.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'use_fake_hardware',
            default_value='false',
            description='Start robot with fake hardware mirroring command to its states.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'use_planning',
            default_value='true',
            description='Start robot with Moveit2 `move_group` planning \
                         config for Pilz and OMPL.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'arm_controller',
            default_value='ur_arm_controller',
            description='arm controller to start.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'gripper_controller',
            default_value='gripper_controller',
            description='gripper controller to start.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'start_rviz',
            default_value='true',
            description='Start RViz2 automatically with this launch file.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'rviz_config_file', 
            default_value='ur_robotiq.rviz',
            description='Rviz file'
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'initial_positions_file',
            default_value='initial_positions.yaml',
            description='Configuration file of robot initial positions for simulation.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'base_frame_file',
            default_value='base_frame.yaml',
            description='Configuration file of robot base frame wrt World.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'description_package',
            default_value='ur_robotiq_moveit_config',
            description='Description package with robot URDF/xacro files. Usually the argument \
                         is not set, it enables use of a custom description.',
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Description package with robot URDF/xacro files. Usually the argument \
                         is not set, it enables use of a custom description.',
        )
    )


    # Initialize Arguments
    runtime_config_package = LaunchConfiguration('runtime_config_package')
    controllers_file = LaunchConfiguration('controllers_file')
    description_package = LaunchConfiguration('description_package')
    description_file = LaunchConfiguration('description_file')
    gazebo_world_file = LaunchConfiguration('gazebo_world_file')
    prefix = LaunchConfiguration('prefix')
    namespace = LaunchConfiguration('namespace')
    sim_gazebo = LaunchConfiguration('sim_gazebo')
    use_planning = LaunchConfiguration('use_planning')
    arm_controller = LaunchConfiguration('arm_controller')
    gripper_controller = LaunchConfiguration('gripper_controller')
    start_rviz = LaunchConfiguration('start_rviz')
    rviz_config_file = LaunchConfiguration('rviz_config_file')
    initial_positions_file = LaunchConfiguration('initial_positions_file')
    base_frame_file = LaunchConfiguration('base_frame_file')
    use_sim_time = LaunchConfiguration('use_sim_time')

    # File path
    controllers_file_path = PathJoinSubstitution(
        [FindPackageShare(description_package), 'config', controllers_file,]
    )
    initial_positions_file_path = PathJoinSubstitution(
        [FindPackageShare(runtime_config_package), 'config', initial_positions_file,]
    )
    rviz_config_file_path = PathJoinSubstitution(
        [FindPackageShare(runtime_config_package), 'rviz', rviz_config_file]
    )
    base_frame_file_path = PathJoinSubstitution(
        [FindPackageShare(runtime_config_package), 'config', base_frame_file]
    )


    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name='xacro')]),
            ' ',
            PathJoinSubstitution(
                [FindPackageShare(description_package), 'urdf', description_file]
            ), 
            ' ',
            'ur_type:=',
            'ur5e',
            ' ',
            'sim_gazebo:=', 
            sim_gazebo, 
            ' ', 
            'simulation_controllers:=',
            controllers_file_path,
            ' ',
            'initial_positions_file:=', 
            initial_positions_file_path,
            ' ', 
            'base_frame_file:=',
            base_frame_file_path,
        ]
    )
    robot_description = {'robot_description': robot_description_content}


    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[{"use_sim_time": use_sim_time}, robot_description],
    )

    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster', '--controller-manager',
                   [namespace, 'controller_manager']],
    )
    


    arm_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[arm_controller, '--controller-manager', [namespace, 'controller_manager']],
    )

    gripper_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[gripper_controller, '--controller-manager', [namespace, 'controller_manager']],
    )


    # Delay start of robot controllers after `joint_state_broadcaster`
    delay_robot_controller_spawner_after_joint_state_broadcaster_spawner = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[arm_controller_spawner, gripper_controller_spawner],
        )
    )

    arm_robot_sim_path = os.path.join(
        get_package_share_directory('ur_robotiq_moveit_config'))

    gazebo_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=[
            os.path.join(arm_robot_sim_path, 'worlds'), ':' +
            str(Path(arm_robot_sim_path).parent.resolve())
            ]
    )

    spawn_entity = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=[
            "-string",
            robot_description_content,
            # "-name",
            # "ur",
            # "-allow_renaming",
            # "true",
        ],
    )


    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [FindPackageShare("ros_gz_sim"), "/launch/gz_sim.launch.py"]
        ),
        launch_arguments=[
            ("gz_args", [PathJoinSubstitution([FindPackageShare(description_package), 'worlds', gazebo_world_file]),
                                 ' -v 4',
                                 ' -r',
                                 ' --physics-engine gz-physics-bullet-featherstone-plugin'],
            )
        ]
    )

    # Make the /clock topic available in ROS
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