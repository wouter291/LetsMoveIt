# Explanation for the different scripts 

In this README you will find information about the scripts for running the pick and place machine with the UR-5.

## Copy pose 

With CopyPose.py you will be able to safe different robot position to a yaml file, which can be used for controlling the robot. The coordinates are safed, under a custom name, in the yaml folder with the name poses.yaml. 

**Make sure you change the directory for this folder in this script, otherwise it won't work.**

To do this, follow the next steps:

```
Go to CopyPose.py
In the class CopyPose go to def __init__(self):
Change the directory in the following line to your own directory: self.adr = '/home/ubuntu/catkin_ws/src/ur_script_control/yaml/poses.yaml'
```

Try making your own poses by putting the robot in the desired position and running the code. 


## Statemachine ##
