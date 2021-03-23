# BrainNodeROS2DE

Basics: webots + e-puck + create2 + gnomes 

Similar:
https://github.com/cyberbotics/webots_ros2/wiki/Tutorial-E-puck-for-ROS2-Beginners

# Start Lawn Mower Sim 01
terminal A>source /opt/ros/foxy/setup.sh
terminal A>colcon build
terminal A>ros2 launch lawn_mower_sim_01 robot_launch.py

terminal B>source /opt/ros/foxy/setup.sh
terminal B>ros2 launch lawn_mower_sim_01 robot_launch.py
terminal B>ros2 launch lawn_mower_sim_01 robot_tools_launch.py rviz:=true nav:=true
