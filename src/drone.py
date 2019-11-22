#!/usr/bin/env python

import cv2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def drone():
	pub=rospy.Publisher('image_raw', Image, queue_size=10)
	rospy.init_node("drone", anonymous=True)

	capture=cv2.VideoCapture(0)
	capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
	capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

	while capture.isOpened():
		ret, frame=capture.read()
		pub_img=CvBridge().cv2_to_imgmsg(frame, "bgr8")

		cv2.waitKey(1000)
		pub.publish(pub_img)

	pub_img.release()
	cv2.destroyAllWindows()

if __name__=='__main__':
	try:
		drone()
	except rospy.ROSInterruptException as e:
		print(e)