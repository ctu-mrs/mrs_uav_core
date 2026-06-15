#!/usr/bin/env python3

import launch
import os
import sys

from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch_ros.actions import ComposableNodeContainer, LoadComposableNodes
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import (
        LaunchConfiguration,
        IfElseSubstitution,
        PythonExpression,
        PathJoinSubstitution,
        EnvironmentVariable,
        )

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    ld = launch.LaunchDescription()

    # #{ uav_name

    uav_name = LaunchConfiguration('uav_name')

    ld.add_action(DeclareLaunchArgument(
        'uav_name',
        default_value=os.getenv('UAV_NAME', "uav1"),
        description="The uav name used for namespacing.",
    ))

    # #} end of custom_config

    # #{ standalone

    standalone = LaunchConfiguration('standalone')

    declare_standalone = DeclareLaunchArgument(
        'standalone',
        default_value='false',
        description='Whether to start a as a standalone or load into an existing container.'
    )

    ld.add_action(declare_standalone)

    # #} end of standalone

    # #{ custom_config

    custom_config = LaunchConfiguration('custom_config')

    # this adds the args to the list of args available for this launch files
    # these args can be listed at runtime using -s flag
    # default_value is required to if the arg is supposed to be optional at launch time
    ld.add_action(DeclareLaunchArgument(
        'custom_config',
        default_value="",
        description="Path to the custom configuration file. The path can be absolute, starting with '/' or relative to the current working directory",
        ))

    # behaviour:
    #     custom_config == "" => custom_config: ""
    #     custom_config == "/<path>" => custom_config: "/<path>"
    #     custom_config == "<path>" => custom_config: "$(pwd)/<path>"
    custom_config = IfElseSubstitution(
            condition=PythonExpression(['"', custom_config, '" != "" and ', 'not "', custom_config, '".startswith("/")']),
            if_value=PathJoinSubstitution([EnvironmentVariable('PWD'), custom_config]),
            else_value=custom_config
            )

    # #} end of custom_config

    # #{ platform_config

    platform_config = LaunchConfiguration('platform_config')

    # this adds the args to the list of args available for this launch files
    # these args can be listed at runtime using -s flag
    # default_value is required to if the arg is supposed to be optional at launch time
    ld.add_action(DeclareLaunchArgument(
        'platform_config',
        default_value="",
        description="Path to the custom configuration file. The path can be absolute, starting with '/' or relative to the current working directory",
        ))

    # behaviour:
    #     platform_config == "" => platform_config: ""
    #     platform_config == "/<path>" => platform_config: "/<path>"
    #     platform_config == "<path>" => platform_config: "$(pwd)/<path>"
    platform_config = IfElseSubstitution(
            condition=PythonExpression(['"', platform_config, '" != "" and ', 'not "', platform_config, '".startswith("/")']),
            if_value=PathJoinSubstitution([EnvironmentVariable('PWD'), platform_config]),
            else_value=platform_config
            )

    # #} end of platform_config

    # #{ world_config

    world_config = LaunchConfiguration('world_config')

    # this adds the args to the list of args available for this launch files
    # these args can be listed at runtime using -s flag
    # default_value is required to if the arg is supposed to be optional at launch time
    ld.add_action(DeclareLaunchArgument(
        'world_config',
        default_value="",
        description="Path to the custom configuration file. The path can be absolute, starting with '/' or relative to the current working directory",
        ))

    # behaviour:
    #     world_config == "" => world_config: ""
    #     world_config == "/<path>" => world_config: "/<path>"
    #     world_config == "<path>" => world_config: "$(pwd)/<path>"
    world_config = IfElseSubstitution(
            condition=PythonExpression(['"', world_config, '" != "" and ', 'not "', world_config, '".startswith("/")']),
            if_value=PathJoinSubstitution([EnvironmentVariable('PWD'), world_config]),
            else_value=world_config
            )

    # #} end of world_config

    # #{ network_config

    network_config = LaunchConfiguration('network_config')

    # this adds the args to the list of args available for this launch files
    # these args can be listed at runtime using -s flag
    # default_value is required to if the arg is supposed to be optional at launch time
    ld.add_action(DeclareLaunchArgument(
        'network_config',
        default_value="",
        description="Path to the custom configuration file. The path can be absolute, starting with '/' or relative to the current working directory",
        ))

    # behaviour:
    #     network_config == "" => network_config: ""
    #     network_config == "/<path>" => network_config: "/<path>"
    #     network_config == "<path>" => network_config: "$(pwd)/<path>"
    network_config = IfElseSubstitution(
            condition=PythonExpression(['"', network_config, '" != "" and ', 'not "', network_config, '".startswith("/")']),
            if_value=PathJoinSubstitution([EnvironmentVariable('PWD'), network_config]),
            else_value=network_config
            )

    # #} end of network_config

    # #{ use_sim_time

    use_sim_time = LaunchConfiguration('use_sim_time')

    ld.add_action(DeclareLaunchArgument(
        'use_sim_time',
        default_value=os.getenv('USE_SIM_TIME', "false"),
        description="Should the node subscribe to sim time?",
    ))

    # #} end of custom_config

    container_name = ["/", uav_name, "/uav_core_container"]

    def setup_core_container(context):

        debug_str = context.launch_configurations.get('debug', 'false')
        is_debug = debug_str.lower() == 'true'

        node_prefix = ""
        if is_debug:
            try:
                node_prefix = "debug_roslaunch " + os.ttyname(sys.stdout.fileno())
            except OSError:
                print("WARNING: Cannot attach debug_roslaunch. No valid TTY found.")

        core_container = ComposableNodeContainer(
            namespace=uav_name, # These variables are safely captured from the outer scope
            name='uav_core_container',
            # executable='component_container_mt',
            # package='rclcpp_components',
            # executable='component_container_isolated',
            # package='rclcpp_components',
            # package='mrs_uav_managers',
            # executable='events_container',
            executable='component_container_events_cbg',
            package='rclcpp_components',
            output="screen",
            parameters=[
                {'use_intra_process_comms': True},
                {'thread_num': os.cpu_count()},
                {'use_sim_time': use_sim_time},
            ],
            prefix=[node_prefix],
            # prefix="valgrind --tool=memcheck --leak-check=no --track-origins=no --show-reachable=no --errors-for-leak-kinds=definite --num-callers=12",
            condition=UnlessCondition(standalone)
        )

        return [core_container]

    ld.add_action(OpaqueFunction(function=setup_core_container))

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('mrs_uav_managers'), '/launch/control_manager.launch.py'
            ]),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'custom_config': custom_config,
                'platform_config': platform_config,
                'world_config': world_config,
                'network_config': network_config,
                'standalone': standalone,
                'container_name': container_name,
            }.items()
        )
    )

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('mrs_uav_managers'), '/launch/safety_area_manager.launch.py'
            ]),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'custom_config': custom_config,
                'platform_config': platform_config,
                'world_config': world_config,
                'network_config': network_config,
                'standalone': standalone,
                'container_name': container_name,
            }.items()
        )
    )

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('mrs_uav_managers'), '/launch/uav_manager.launch.py'
            ]),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'custom_config': custom_config,
                'platform_config': platform_config,
                'world_config': world_config,
                'network_config': network_config,
                'standalone': standalone,
                'container_name': container_name,
            }.items()
        )
    )

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('mrs_uav_managers'), '/launch/transform_manager.launch.py'
            ]),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'custom_config': custom_config,
                'platform_config': platform_config,
                'world_config': world_config,
                'network_config': network_config,
                'standalone': standalone,
                'container_name': container_name,
            }.items()
        )
    )

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('mrs_uav_managers'), '/launch/constraint_manager.launch.py'
            ]),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'custom_config': custom_config,
                'platform_config': platform_config,
                'world_config': world_config,
                'network_config': network_config,
                'standalone': standalone,
                'container_name': container_name,
            }.items()
        )
    )

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('mrs_uav_managers'), '/launch/gain_manager.launch.py'
            ]),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'custom_config': custom_config,
                'platform_config': platform_config,
                'world_config': world_config,
                'network_config': network_config,
                'standalone': standalone,
                'container_name': container_name,
            }.items()
        )
    )

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('mrs_uav_managers'), '/launch/estimation_manager.launch.py'
            ]),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'custom_config': custom_config,
                'platform_config': platform_config,
                'world_config': world_config,
                'network_config': network_config,
                'standalone': standalone,
                'container_name': container_name,
            }.items()
        )
    )

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('mrs_uav_trajectory_generation'), '/launch/trajectory_generation.launch.py'
            ]),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'custom_config': custom_config,
                'platform_config': platform_config,
                'standalone': standalone,
                'container_name': container_name,
            }.items()
        )
    )

    ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('mrs_uav_status'), '/launch/acquisition.launch.py'
            ]),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'custom_config': custom_config,
                'platform_config': platform_config,
                'standalone': standalone,
                'container_name': container_name,
            }.items()
        )
    )

    return ld
