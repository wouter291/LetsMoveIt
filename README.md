# UR-5 pick and place Let's Move It

UR-5 pick and place package for UR-5 industrial robot. This package is used to excecute pick and place tasks with the UR-5 robotic arm. This README explains how to install the pick and place package and the other required packages, and what steps must be taken to get everything up and running. 


## Getting started

For this project it is assumed you have

 - Ubuntu 16.04 LTS 

 - ROS Kinetic 

 - Python 2.7
 
**NOTE** this program won't work with Python 3.0 or higher.


## Prerequisites

###### What things do you need to install for the software to work and how to install them:

First you will need the _ur_modern_driver_ package from _ros-industrial_. You can install this package by running the following commands:

```
cd catkin_ws/src
git clone https://github.com/ros-industrial/ur_modern_driver.git
cd catkin_ws
catkin_make
```

Run the following command:
```
sudo apt-get install ros-kinetic-ur-*
```
This will give you the ability to run your program on a real Universal robot (UR3, UR5, UR10).



The next thing you will need to install is the _universal_robot_ package. You can install this package by running the following commands:

```
cd catkin_ws/src
git clone https://github.com/ros-industrial/universal_robot.git
cd catkin_ws
catkin_make
```

**NOTE** that you need to change the *universal_robot/ur_driver/src/ur_driver/io_interface.py*to the *io_interface.py* that is in the src folder uploaded to this github. Copy it and paste it in your catkin_ws/src/universal_robot/ur_driver/src/ur_driver. Don't forget to delete the old one.


## Installing the Let's Move It package
To install the _Let's Move It package_ in your catkin workspace, you will need to run the following commands:

```
cd catkin_ws/src
git clone https://github.com/wouter291/LetsMoveIt.git
cd catkin_ws
catkin_make
cd ~
source catkin_ws/devel/setup.bash
```

## Test your installed package

First make sure you have a connection with the robot. To make sure you have a connection do the following:

```
1. Connect the Ethernet cable to your PC
2. Go to internet settings and select wired connection
3. Click "Edit"
4. Go to IPv4 settings
5. Change from automatic to manual
6. Click on "Add"
7. Fill in the ip addres with the last number different from the real ip addres 
    (for example: if the real ip address is "192.168.66.5" fill in "192.168.66.1")
8. Fill in the netmask (if not automatically) to "24"
9. Fill in the gateway to "255.255.255.0"
```


To test if your package is installed correctly run the following lines:

```
roslaunch ur_modern_driver ur5_bringup.launch robot_ip:=[IP_OF_THE_ROBOT]
```

Open the StateMachine.py, from the src folder, in an editor of choice and run the code.

**Be aware, the coordinates in the StateMachine.py are filled in for our purpouse ! Be carefull with running the program before you destroy anything*** 

If this runs without errors, the package is installed correctly.


Run the following line to see the virtual robot:
```
rosrun rviz rviz
```
Set the fixed frame to **world**

And add **RobotModel** to RViz.

**HINT** save the current layout so that RViz will start with the correct fixed frame and robot model.

