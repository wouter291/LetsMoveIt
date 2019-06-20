# UR-5 pick and place Let's Move It

UR-5 pick and place package for UR-5 industrial robot. This package is used to do pick and place tasks with the UR-5 robotic arm. This README is used to explain how to install the pick and place package and the other required packages, and what steps must be taken to get everything running. 


## Getting started

For this project it is assumed you use Ubuntu 16.04 LTS with ROS Kinetic

### Prerequisites

What things you need to install the software and how to install them:

You will need the ur_modern_driver package from ros-industrial. You can intall this package by running the following lines:

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

First make sure you have a connection with the robot. To make sure you have a connection do the following:

```
Connect the Ethernet cable to your PC
Go to internet settings and select wired connection
Edit connection
Change from automatic to manual
Click on "add"
Fill in the ip addres with the last number different from the real ip addres 
  (for example: if the real ip address is "192.168.66.5" fill in "192.168.66.1")
Fill in the netmask (if not automatically) to "24"
Fill in the gateway to "255.255.255.0"
```


To test if your package is installed correctly run the following lines:

```
roslaunch ur_modern_driver ur5_bringup.launch robot_ip:=[IP_OF_THE_ROBOT]
rosrun LetsMoveIt StateMachine.py
```
**Be aware, the coordinates in the StateMachine.py are filled in for our purpouse ! Be carefull with running the program before you destroy anything*** 

If this runs without errors, the package is installed correctly.


Run the following line to see the virtual robot:
```
rosrun rviz rviz
```

And add **RobotModel** to rviz.

