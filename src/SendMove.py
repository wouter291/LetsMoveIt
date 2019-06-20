#!/usr/bin/env python
import sys
import rospy
import std_msgs

class SendMove (object):
    def __init__(self):
        rospy.init_node('Send_move_node', anonymous=True)
        #Publisher to URscript topic
        self.pub = rospy.Publisher('/ur_driver/URScript',std_msgs.msg.String, queue_size=10 )

    def buildMove(self, moveType, pose):
        #Moving on jointpositions = "movej([-1.95, -1.58, 1.16, -1.15, -1.55, 1.18], a=1.0, v=0.1)"+"\n"
        #Moving on posepositions = "movej(p[0.00, 0.3, 0.4, 2.22, -2.22, 0.00], a=1.0, v=0.1)" + "\n"
        acceleration = 1.0  #Joint acceleration in rad/s^2
        speed = 1.0 #Joint speed in rad/s
        time = 0 #Time the move must take
        radius = 0 # Blend radius in m, so the robot moves trough the point instead of stopping
        sendable = "move%s(%s, a=%s, v=%s, t=%s, r=%s)"(moveType, pose, acceleration, speed, time, radius)
        return sendable

    def sendMove(self, string):
        self.pub.publish(string)
        print "Published: %s  "(string)

if __name__ == '__main__':
    try:
        x = SendMove()
        rospy.spin()             
        
    except rospy.ROSInterruptException:
        pass