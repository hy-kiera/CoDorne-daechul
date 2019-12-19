#!/usr/bin/env python

import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge#, CvBridgeErrors

def publishing():
	capture=cv2.VideoCapture("http://192.168.34.2:8090?action=stream")
	#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
	#capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
	bridge = CvBridge()

	#pub_str=rospy.Publisher('string', String, queue_size=10)
	pub_image=rospy.Publisher('video_capture', Image, queue_size=10)
	#pub_cameraInfo=rospy.Publisher('camerainfo', CameraInfo, queue_size=10)
	rospy.loginfo(pub_image)
	rospy.init_node('video_capturer',anonymous=True)

	while True:#not rospy.is_shutdown():
		ret, frame=capture.read()
		p_image = bridge.cv2_to_imgmsg(frame, "bgr8")
		#print(ret)
		#print(pub_image)
		#str="hello"

		#pub_str.publish(str)
		pub_image.publish(p_image)
		#pub_cameraInfo.publish(ret)
		#cv2.imshow('test',frame)
		#cv2.waitKey(11)

	capture.release()
	cv2.destroyAllWindows()

if __name__=='__main__':
	try:
		publishing()
	except rospy.ROSInterruptException as e:
		print(e)