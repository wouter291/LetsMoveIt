#!/usr/bin/env python
import time
import sys
import rospy
import yaml
from geometry_msgs.msg import Pose, TwistStamped
from std_msgs.msg import String
from SendMove import SendMove
from io_interface import set_digital_out, get_states, set_states, callback
from ur_msgs.srv import *
from ur_msgs.msg import *


class StateMachine (object):
    def __init__(self):
        rospy.init_node('StateMachineNode', anonymous=True)
        self.pub = rospy.Publisher('/ur_driver/URScript', String, queue_size=10, latch=True)
    
        self.addr = '/home/ubuntu/catkin_ws/src/LetsMoveIt/yaml/poses.yaml'
        rospy.Subscriber("tool_velocity", TwistStamped, self.getToolVelocity)

        set_states()
        rospy.Subscriber("/ur_driver/io_states", IOStates, self.callback)     
        self.Digital_Out_States = [0,0,0,0,0,0,0,0,0,0]  #8(controller)+2(tool)
        self.Digital_In_States = [0,0,0,0,0,0,0,0,0,0]   #8(controller)+2(tool)
        self.Analog_Out_States = [0,0]  #2(controller)
        self.Analog_In_States = [0,0]   #2(controller)+0(tool)
        #get_states()
        
        #Set output to default
        set_digital_out(0,1) #opening gripper
        set_digital_out(1,0) #close gripper

       
    def getToolVelocity(self, msg):
        self.xVel = msg.twist.linear.x
        self.yVel = msg.twist.linear.y
        self.zVel = msg.twist.linear.z
        self.rxVel = msg.twist.angular.x
        self.ryVel = msg.twist.angular.y
        self.rzVel = msg.twist.angular.z

   
    def callback(self, data):
        for i in range(0,10):
            del self.Digital_Out_States[i]
            self.Digital_Out_States.insert(i, data.digital_out_states[i].state)
        for i in range(0,10):
            del self.Digital_In_States[i]
            self.Digital_In_States.insert(i, data.digital_in_states[i].state)

    
    def waitForPosition(self):
        #This function waits untill the arm reached the position by waiting for the tool velocity to reach zero
        time.sleep(0.3)
        while (abs(self.xVel) > 0.0001 or abs(self.yVel) > 0.0001 or abs(self.zVel) > 0.0001) and not rospy.is_shutdown():
            rospy.loginfo_throttle(1, "Robot is moving to position")
        rospy.loginfo("Robot reached position")
    
    
    def getPos(self, pos_name):
        file = open(self.addr, 'r')
        y = yaml.load(file)
        file.close()
        poses = y
        wanted_pose = poses.get(pos_name)
        #print wanted_pose
        return wanted_pose

    
    def buildMove(self, moveType, pose):
        # acceleration = 1  #Joint acceleration in rad/s^2
        # speed = 0.8 #Joint speed in rad/s
        time = 0 #Time the move must take
        radius = 0 # Blend radius in m, so the robot moves trough the point instead of stopping
        array = list(pose)
        #print array
        sendable = "move%s(%s, a=%s, v=%s, t=%s, r=%s)" % (moveType, array, self.acceleration, self.speed, time, radius)
        #sendable = "movej(p[0.00, 0.3, 0.4, 2.22, -2.22, 0.00], a=1.0, v=0.1"
        #print sendable
        return sendable

    
    def sendMove(self, string):
        st = String()        
        st.data = string
        self.pub.publish(st)

        
    def testSequence(self):
        try:
            # #Starting the robot
            # print("Press 'Enter' to start the robot")
            # raw_input()
            excecute = StateMachine() 

            input0 = self.Digital_In_States[0]
            input1 = self.Digital_In_States[1]
            input2 = self.Digital_In_States[2]
            input3 = self.Digital_In_States[3]
            input4 = self.Digital_In_States[4]
            input5 = self.Digital_In_States[5]
            input6 = self.Digital_In_States[6]
            input7 = self.Digital_In_States[7]
            #print "input4 =", input4
            #time.sleep(1)


            if (input4 == 0):

                #ready signal for lift to false
                set_digital_out(7,0) 

                #Abovelift
                self.speed = 0.8
                self.acceleration = 0.8
                self.sendMove(self.buildMove('j',self.getPos('Abovelift')))
                excecute.waitForPosition()
                
                #PickingBoxAtLift
                self.speed = 0.8
                self.acceleration = 0.8
                self.sendMove(self.buildMove('j',self.getPos('PickingBoxAtLift')))
                excecute.waitForPosition()

                #Closegripper
                set_digital_out(0,0) #opening gripper
                set_digital_out(1,1) #close gripper
                time.sleep(0.5)

                #Abovelift
                self.speed = 0.8
                self.acceleration = 0.8
                self.sendMove(self.buildMove('j',self.getPos('Abovelift')))
                excecute.waitForPosition()

                #ready signal for lift true
                set_digital_out(7,1)

                #InFrontOfConveyerBelt
                self.speed = 1.5
                self.acceleration = 1
                self.sendMove(self.buildMove('j',self.getPos('InFrontOfConveyerBelt')))
                excecute.waitForPosition() 
                
                #AboveConveyorBelt
                self.speed = 1.5
                self.acceleration = 1
                self.sendMove(self.buildMove('j',self.getPos('AboveConveyorBelt')))
                excecute.waitForPosition()

                #ready signal for lift false
                set_digital_out(7,0) 

                #PlacingBoxAtConveyorBelt
                self.speed = 0.8
                self.acceleration = 0.8
                self.sendMove(self.buildMove('j',self.getPos('PlacingBoxAtConveyorBelt')))
                excecute.waitForPosition()

                #Open gripper
                set_digital_out(1,0) #close gripper
                set_digital_out(0,1) #opening gripper
                time.sleep(0.5)
                
                #AboveConveyorBelt
                self.speed = 0.8
                self.acceleration = 0.8
                self.sendMove(self.buildMove('j',self.getPos('AboveConveyorBelt')))
                excecute.waitForPosition()

                #InFrontOfConveyerBelt
                self.speed = 1.5
                self.acceleration = 1
                self.sendMove(self.buildMove('j',self.getPos('InFrontOfConveyerBelt')))
                excecute.waitForPosition() 

                #AboveLift
                self.speed = 1.5
                self.acceleration = 1
                self.sendMove(self.buildMove('j',self.getPos('Abovelift')))
                excecute.waitForPosition()


        except rospy.ROSInternalException:
            return
        except KeyboardInterrupt:
            return


if __name__ == '__main__':
    while(1):
        objStateMachine = StateMachine()
        objStateMachine.testSequence()
       

