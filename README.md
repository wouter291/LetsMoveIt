# UR-5 pick and place Let's Move It

UR-5 pick and place package for UR-5 industrial robot. This package is used to do pick and place tasks with the UR-5 robotic arm. This README is used to explain how to install the pick and place package and the other required packages, and what steps must be taken to get everything running. 


## Getting started

For this project it is assumed you use Ubuntu 16.04 LTS with ROS Kinetic

### Prerequisites

What things you need to install the software and how to install them:

You will need the ur_modern_driver package from ThomasTimm. You can intall this package by running the following lines:

```
cd catkin_ws/src
git clone https://github.com/ros-industrial/ur_modern_driver.git
catkin_make
sudo apt-get install ros-kinetic-ur-*

```

This will give you the ability to run your program on a real Universal robot (UR3, UR5, UR10).



The next thing you will need to install is the universal_robot package. You can install this package by running the following lines:

```
cd catkin_ws/src
git clone https://github.com/ros-industrial/universal_robot.git
catkin_make
```

**Beaware that you need to change the universal_robot/ur_driver/src/ur_driver/io_interface.py to the io_interface.py that is uploaded to this github. Copy it and paste it in your catkin_ws/src/universal_robot/ur_driver/src/ur_driver. Don't forget to delete the old one.**


## Installing the Let's Move It package
To install the Let's Move It package in your catkin workspace, you will need to run the following lines:

```
cd catkin_ws/src
git clone https://github.com/wouter291/LetsMoveIt.git
catkin_make
```

## Test your installed package

To test if your package is installed correctly run:

```
roslaunch ur_modern_driver ur5_bringup.launch
rosrun LetsMoveIt StateMachine.py
```

If this runs without errors, the package is installed correctly.


```
rosrun rviz rviz
```

And add **RobotModel** to rviz.

