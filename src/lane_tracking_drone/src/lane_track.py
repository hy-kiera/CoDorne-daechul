#!/usr/bin/env python

import numpy as np
import cv2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Pose
import matplotlib.pyplot as plt

pose=Pose()

def detect_edges(frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([105, 105, 105])
        mask = cv2.inRange(hsv, lower_black, upper_black)
        edges = cv2.Canny(mask, 150, 300) # need to modify
        return edges

def strengthen(img):
    strengthen_img=np.power(img,2)
    #cv2.imshow("frame_lane",strengthen_img)
    #cv2.waitKey(100)
    return strengthen_img

def weighted_img(img, initial_img, a=1, b=1., r=0.):
    return cv2.addWeighted(initial_img, a, img, b, r)

def callback(data):
    sub_img=CvBridge().imgmsg_to_cv2(data, "bgr8")
    sub_img=cv2.flip(sub_img,0)
    #rospy.loginfo(sub_img)
    #cv2.imshow("video_capture",sub_img)
    #cv2.waitKey(100)

    gray = cv2.cvtColor(sub_img,cv2.COLOR_BGR2GRAY)

    canny_img = cv2.Canny(gray,150,300,apertureSize=3)

    height = canny_img.shape[0]
    width = canny_img.shape[1]

    d = height // 3
    epo1 = 0
    epo2 = d
    crop_img = canny_img[epo1:epo2]

    # strengthen
    strengthen_img = np.power(crop_img, 2)
    crop_height = strengthen_img.shape[0]
    crop_width = strengthen_img.shape[1]
    
    middles = []

    for i in range(len(strengthen_img)):
        lcur = crop_width // 2 - (crop_width // 4)
        rcur = crop_width // 2 + (crop_width // 4)

        while(strengthen_img[i][lcur] == 0 or strengthen_img[i][rcur] == 0):
            if strengthen_img[i][lcur] == 0:
                lcur -= 1
            if strengthen_img[i][rcur] == 0:
                rcur += 1
            if lcur < 0:
                lcur = 0
                break
            if rcur > crop_width - 1:
                rcur = crop_width - 1
                break

        middle = (rcur + lcur) // 2
        middles.append(middle)
    color = (255, 0, 0)

    for i in range(epo1, epo2):
        result = cv2.line(sub_img,(middles[i-epo1],i), (middles[i-epo1],i), color, 5)

    cv2.imshow("video_capture",result)
    cv2.waitKey(1)

    x_center = np.mean(middles)
    rospy.loginfo(x_center)

    if(x_center<width):
        pose.orientation.x=0
        pose.orientation.y=-1
        pose.orientation.z=0
        pose.orientation.w=0
    else :
        pose.orientation.x=0
        pose.orientation.y=1
        pose.orientation.z=0
        pose.orientation.w=0

    pose.orientation.x=1
    pose.orientation.y=0
    pose.orientation.z=0
    pose.orientation.w=0

    print(pose)

def detector():
    rospy.init_node('detector', anonymous=True)
    sub=rospy.Subscriber('video_capture', Image, callback)
    pub=rospy.Publisher('xyzw',Pose,queue_size=10)
    pub.publish(pose)
    rospy.spin()

if __name__=='__main__':
    try:
        detector()
    except rospy.ROSInterruptException as e:
        print(e)