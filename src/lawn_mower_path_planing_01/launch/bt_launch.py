import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions.node import Node

def generate_launch_description():
    # Path
    bt_xml_dir = os.path.join(get_package_share_directory('lawn_mower_path_planing_01'), 'bt_xml')

    # Parameters
    bt_xml = LaunchConfiguration('lawn_mower_path_planing_01', default=bt_xml_dir+'/test_01.xml')

    behavior_tree = Node(
        package='lawn_mower_path_planing_01',
        executable='bt_ros2',
        parameters=[{'bt_xml': bt_xml}],
        output='screen'
    )

    ld = LaunchDescription()
    ld.add_action(behavior_tree)
    return ld
