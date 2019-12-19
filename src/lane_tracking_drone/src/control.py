#!/usr/bin/env python

import numpy as np
import cv2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Pose

def controller():
	pub=rospy.Publisher('xyzw',Pose,queue_size=10)
	pose=Pose()
	rospy.init_node('controller', anonymous=True)
	while not rospy.is_shutdown():
		print("x=#1 = go forward 1cm")
		pose.orientation.x=input()
		print("y=#1 = go left 1cm")
		pose.orientation.y=input()
		print("z=#1 = go up 1cm")
		pose.orientation.z=input()
		print("w=#1 = take off, -1 = landing")
		pose.orientation.w=input()

		print(pose)
		pub.publish(pose)

if __name__=='__main__':
	try:
		controller()
	except rospy.ROSInterruptException as e:
		print(e)