import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_navigation_stack = get_package_share_directory('mobile_manip_moveit_config')
    os.environ["GZ_SIM_RESOURCE_PATH"] += os.pathsep + pkg_navigation_stack + "/gazebo_models/"

    world_arg = DeclareLaunchArgument('world', default_value='warehouse_walk.sdf', description='Name of the Gazebo world file to load')
    model_arg = DeclareLaunchArgument('model', default_value='mobile_manip.urdf.xacro', description='Name of the URDF description to load')
    x_arg = DeclareLaunchArgument('x', default_value='0', description='x coordinate of spawned robot')
    y_arg = DeclareLaunchArgument('y', default_value='0', description='y coordinate of spawned robot')
    yaw_arg = DeclareLaunchArgument('yaw', default_value='-1.5707', description='yaw angle of spawned robot')
    sim_time_arg = DeclareLaunchArgument('use_sim_time', default_value='True', description='Flag to enable use_sim_time')

    urdf_file_path = PathJoinSubstitution([pkg_navigation_stack, "urdf", LaunchConfiguration('model')])
    gz_bridge_params_path = os.path.join(pkg_navigation_stack, 'config', 'gz_bridge.yaml')

    world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_navigation_stack, 'launch', 'world.launch.py')),
        launch_arguments={'world': LaunchConfiguration('world')}.items()
    )

    spawn_urdf_node = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=["-topic", "robot_description", "-x", LaunchConfiguration('x'), "-y", LaunchConfiguration('y'), "-z", "0.5", "-Y", LaunchConfiguration('yaw')],
        output="screen",
        parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}]
    )

    gz_bridge_node = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=['--ros-args', '-p', f'config_file:={gz_bridge_params_path}'],
        output="screen",
        parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}]
    )

    gz_bridge_node_delayed = TimerAction(period=5.0, actions=[gz_bridge_node])

    gz_image_bridge_node = Node(
        package="ros_gz_image",
        executable="image_bridge",
        arguments=["/camera/image"],
        output="screen",
        parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time'), 'camera.image.compressed.jpeg_quality': 75}]
    )

    relay_camera_info_node = Node(
        package='topic_tools',
        executable='relay',
        name='relay_camera_info',
        output='screen',
        arguments=['camera/camera_info', 'camera/image/camera_info'],
        parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}]
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': Command(['xacro', ' ', urdf_file_path]), 'use_sim_time': LaunchConfiguration('use_sim_time')}],
        remappings=[('/tf', 'tf'), ('/tf_static', 'tf_static')]
    )

    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster', '--controller-manager', ['', 'controller_manager']]
    )

    arm_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['ur_arm_controller', '--controller-manager', ['', 'controller_manager']]
    )

    gripper_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['gripper_controller', '--controller-manager', ['', 'controller_manager']]
    )

    ekf_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[os.path.join(pkg_navigation_stack, 'config', 'ekf.yaml'), {'use_sim_time': LaunchConfiguration('use_sim_time')}]
    )

    launchDescriptionObject = LaunchDescription()
    launchDescriptionObject.add_action(world_arg)
    launchDescriptionObject.add_action(model_arg)
    launchDescriptionObject.add_action(x_arg)
    launchDescriptionObject.add_action(y_arg)
    launchDescriptionObject.add_action(yaw_arg)
    launchDescriptionObject.add_action(sim_time_arg)
    launchDescriptionObject.add_action(world_launch)
    launchDescriptionObject.add_action(spawn_urdf_node)
    launchDescriptionObject.add_action(gz_bridge_node_delayed)
    launchDescriptionObject.add_action(gz_image_bridge_node)
    launchDescriptionObject.add_action(relay_camera_info_node)
    launchDescriptionObject.add_action(robot_state_publisher_node)
    launchDescriptionObject.add_action(joint_state_broadcaster_spawner)
    launchDescriptionObject.add_action(arm_controller_spawner)
    launchDescriptionObject.add_action(gripper_controller_spawner)
    launchDescriptionObject.add_action(ekf_node)

    return launchDescriptionObject