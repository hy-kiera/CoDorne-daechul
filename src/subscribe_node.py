#!/usr/bin/env python

import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError

def callback(data):
	rospy.loginfo("heard %s", data.data)
"""
	try:
		sub_image=self.bridge.imgmsg_to_cv2(data.Image, "bgr8")
	except CvBridgeError as e:
		print(e)

	cv2.imshow("sub", sub_image)
	cv2.waitKey(1)
"""
def subscribing():
	rospy.init_node("sub_node",anonymous=True)

	rospy.Subscriber('String', String, callback)
	
	rospy.spin()
	#cv2.destroyAllWindows()

if __name__=='__main__':
	subscribing()