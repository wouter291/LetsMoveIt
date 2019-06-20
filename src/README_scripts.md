# Explanation for the different scripts 

In this README you will find information about the scripts for running the pick and place machine with the UR-5.

## Copy pose 

With CopyPose.py you will be able to safe different robot position to a yaml file, which can be used for controlling the robot. The coordinates are safed, under a custom name, in the yaml folder with the name poses.yaml. 

**Make sure you change the directory for this folder in this script, otherwise it won't work.**

To do this, follow the next steps:

```
Go to CopyPose.py
In the class CopyPose go to def __init__(self):
Change the directory in the following line: self.adr = '/home/ubuntu/catkin_ws/src/ur_script_control/yaml/poses.yaml' to your own directory.
```

Try making your own poses by putting the robot in the desired position and running the code. 


## Statemachine ##

The StatMachine.py is the main script for moving the robot.

**Make sure you change the directory for this folder in this script, otherwise it won't work.**

To do this, follow the next steps:

```
Go to StateMachine.py
In the class StateMachine go to def __init__(self):
Change the directory in the following line: self.adr = '/home/ubuntu/catkin_ws/src/ur_script_control/yaml/poses.yaml' to your own directory.
```

In the testSequence there are different movements described. For example:
  ```
  #Abovelift
  self.speed = 0.8
  self.acceleration = 0.8
  self.sendMove(self.buildMove('j',self.getPos('Abovelift')))
  excecute.waitForPosition()
  ```
We've defined a position with the CopyPose script called "Abovelift" you can change these to your own poses made with the CopyPose script to make the robot move to the desired pose. You can also change the speed and acceleration of the robot for eacht movement. **Note** The speed and acceleration are both defined in **radians**.

**Controlling the gripper outputs**

For controlling our gripper we've used two different outputs, closing and opening the gripper(DO0 and DO1).

**Note** your outputs from your gripper could be different!

You can set the outputs by calling the folowing function:

set_digital_out(n,v)

Where:

n = output port

v = value(0 or 1)

