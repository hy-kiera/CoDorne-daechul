#!/usr/bin/env python

import time
import rospy
from std_msgs.msg import String
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import numpy as np
import os
import csv
from classifier.yolo import YOLO
import rospkg
import yaml
from cv_bridge import CvBridge
import matplotlib.pyplot as plt


class ObjectDetection:
    yolo = None
    config = None
    bridge = None
    def __init__(self):

        rospy.init_node('object_detection_node')

        rospack = rospkg.RosPack()
        path = rospack.get_path('object_detection')

        #Load config
        # if rospy.has_param("/object_detection_config"):
        # 	object_detection_config = rospy.get_param("/object_detection_config", "./config/object_detection.yaml")
        # print("no key")
        # object_detection_config = "./config/object_detection.yaml"
        # self.config = yaml.load(object_detection_config)

        # self.yolo = YOLO(path+self.config['classification']['model'], path+self.config['classification']['anchors'], path+self.config['classification']['classes'])
        self.yolo = YOLO(path+'/scripts/classifier/model/yolo.h5', path+'/scripts/classifier/model/tiny_yolo_anchors.txt', path+'/scripts/classifier/model/classes.txt')
        self.bridge = CvBridge()
        
        print("created YOLO object")
        img = cv2.imread("/home/exist/Pictures/test_image.jpeg", cv2.IMREAD_COLOR)
        self.classify(img)
        #change the camera topic if it is different
        rospy.Subscriber('/camera/color/image_raw', Image, self.classify)
        # rospy.Publisher()
        rospy.spin()

    def bgr_to_rgb(self, img):
        b, g, r = cv2.split(img)
        return cv2.merge([r,g,b])
        
    def classify(self, image):
        # img = self.bridge.imgmsg_to_cv2(image, "bgr8")
        # img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        image = self.bgr_to_rgb(image)
        scores, classes, img_ret, box = self.yolo.detect_image(image)
        fig = plt.figure()
        img = [image, img_ret]
        title = ["original", "object detect"]
        for i in range(2):
            ax = fig.add_subplot(1, 2, i+1)
            imgplot = ax.imshow(img[i])
            ax.set_title(title[i])
        # plt.imshow(img_ret)
        plt.show()
        print("=================class================\n", classes)


if __name__ == '__main__':
    try:
        ObjectDetection()
    except rospy.ROSInterruptException:
        rospy.logerr('Could not start object detection node.')

