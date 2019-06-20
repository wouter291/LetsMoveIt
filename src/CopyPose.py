#!/usr/bin/env python
"""
This is a project made for RoboHub Eindhoven.

Summary:
This program makes it able to to save poses to a yaml file.

!!! IT SAVES THE JOINT POSITIONS NOT THE END EFFECTOR POSITION !!!

This is done to make sure the robot will always give the same fysical position.
It subscribes to the /joint_states topic which should be only running the robot model.
If there are additional joints present then the robot will save those also. 
This will not be good for the understanding of the position for the other apps.
 """

import sys
import rospy
import yaml
import string
from sensor_msgs.msg import JointState

class CopyPose(object):
    def __init__(self):
        rospy.init_node('CopyPoseNode', anonymous=True)
        
        #Subscriber to the /joint_states
        self.joint_state_sub = rospy.Subscriber("/joint_states", JointState, self.jointStateCallback )

        self.saved_pos = JointState.position
        self.saved_poses = {}
        self.adr = '/home/ubuntu/catkin_ws/src/ur_script_control/yaml/poses.yaml'
        
        self.savingPose()

    def jointStateCallback(self, msg):
        #print msg.position
        self.saved_pos = msg.position
        
    def savingPose(self):
        name = raw_input("Give this pos a name: ")
        disposable = raw_input("Press Enter to save")

        file = open(self.adr, 'r')
        y = yaml.load(file)
        file.close()
        self.saved_poses = y
        if self.saved_poses == None :
            self.saved_poses = dict()
        
        if self.saved_poses.get(name, 0):
            print "Name: '%s' already exists in the file, try other name." % name
            self.__init__()
        else:
            self.saved_poses[name] = self.saved_pos
            print "saved new pose :%s" % name 
            #print "pose : %s" % self.saved_pos
            file = open(self.adr, 'w+')
            yaml.dump(self.saved_poses, file)
            file.close()



if __name__ == '__main__':
    try:
        x = CopyPose()
        #rospy.spin()             
        
    except rospy.ROSInterruptException:
        pass