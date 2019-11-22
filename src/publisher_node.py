#!/usr/bin/env python

import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError

def publishing():
	#capture=cv2.VideoCapture(0)
	#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
	#capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

	pub_str=rospy.Publisher('string', String, queue_size=10)
	#pub_image=rospy.Publisher('image', Image, queue_size=10)
	#pub_cameraInfo=rospy.Publisher('camerainfo', CameraInfo, queue_size=10)

	rospy.init_node('pub_node',anonymous=True)

	while not rospy.is_shutdown():
		#ret, frame=capture.read()
		#print(ret)
		#print(frame)
		str="hello"

		pub_str.publish(str)
		#pub_image.publish(frame)
		#pub_cameraInfo.publish(ret)
	#capture.release()

if __name__=='__main__':
	try:
		publishing()
	except rospy.ROSInterruptException as e:
		print(e)
