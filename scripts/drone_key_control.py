#!/usr/bin/env python
from __future__ import print_function
import rospy
import time
import roslib; roslib.load_manifest('teleop_twist_keyboard')
from geometry_msgs.msg import Pose
import sys, select, termios, tty


msg = """

key intro:
w = forward
s = backard
a = left
d = right
q = turn left
e = turn right
r = takeoff
f = landing

"""

moveBindings = {
	'w':(1,0,0,0),
	's':(-1,0,0,0),
	'q':(0,0,1,0),
	'e':(0,0,-1,0),
	'a':(0,1,0,0),
	'd':(0,-1,0,0),
	'r':(0,0,0,1),
	'f':(0,0,0,-1),
}

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

if __name__=="__main__":
	settings = termios.tcgetattr(sys.stdin)

	pub = rospy.Publisher("xyzw", Pose, queue_size = 1)
	rospy.init_node('drone_key_controller')

	x = 0
	y = 0
	z = 0
	w = 0

	try:
		print(msg)
		while(1):
			key = getKey()
			print(key)
			if key in moveBindings.keys():
				x = moveBindings[key][0]
				y = moveBindings[key][1]
				z = moveBindings[key][2]
				w = moveBindings[key][3]
			else:
				x = 0
				y = 0
				z = 0
				w = 0
				if (key == '\x03'):
					break

			ang = 10
			pose = Pose()
			pose.orientation.x = x*ang
			pose.orientation.y = y*ang
			pose.orientation.z = z*ang
			pose.orientation.w = w
			pub.publish(pose)

	except Exception as e:
		print(e)

	finally:
		pose = Pose()
		pose.orientation.x = 0
		pose.orientation.y = 0
		pose.orientation.z = 0
		pose.orientation.w = 0
		pub.publish(pose)

		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)