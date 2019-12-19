#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		hello_str = "i am ironman %s" % rospy.get_time()
		#rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rospy.Subscriber("response", String, callback)
		rate.sleep()

if __name__== '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass