#!/usr/bin/env python

import cv2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def callback(data):
	#rospy.loginfo(data)
	sub_img=CvBridge().imgmsg_to_cv2(data, "bgr8")
	rospy.loginfo(sub_img)
	
	cv2.imshow("camera",sub_img)
	cv2.waitKey(1)

def pc():
	rospy.init_node('pc', anonymous=True)
	sub=rospy.Subscriber('image_raw', Image, callback)
	rospy.spin()

if __name__=='__main__':
	try:
		pc()
	except rospy.ROSInterruptException as e:
		print(e)
