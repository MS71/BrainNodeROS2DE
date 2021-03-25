# BrainNodeROS2DE

Basics: webots + e-puck + create2 + gnomes 

Similar:
https://github.com/cyberbotics/webots_ros2/wiki/Tutorial-E-puck-for-ROS2-Beginners

# Start Lawn Mower Sim 01

* terminal A>source /opt/ros/foxy/setup.sh
* terminal A>colcon build

* terminal A>source install/setup.sh
* terminal A>ros2 launch lawn_mower_sim_01 robot_launch.py

* terminal B>source /opt/ros/foxy/setup.sh
* terminal B>source install/setup.sh
* terminal B>ros2 launch lawn_mower_sim_01 robot_tools_launch.py rviz:=true nav:=true map:=/path/to/your/map.yaml

* terminal C>ros2 run lawn_mower_sim_01 drive_calibrator --ros-args -p type:=linear
* terminal C>ros2 run lawn_mower_sim_01 drive_calibrator --ros-args -p type:=angular

* terminal C>source /opt/ros/foxy/setup.sh
* terminal C>source install/setup.sh
* terminal C>ros2 launch lawn_mower_path_planing_01 bt_launch.py




