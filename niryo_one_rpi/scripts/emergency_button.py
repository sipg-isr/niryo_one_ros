#!/usr/bin/env python
import rospy

from niryo_one_msgs.msg import DigitalIOState
from niryo_one_msgs.srv import SetInt

activate_robot_srv = None
robot_on = True

def digital_io_callback(data):
	if activate_robot_srv is None:
		rospy.logerr("Niryo One Emergency Button: activate robot srv not ready!")
		return
	
	#corresponds to io16
	emergency_button = data.states[2]
	if emergency_button == 0: # goes 0 if button pressed
		if robot_on:
			rospy.loginfo("Niryo One Emergency Button: Emergency Button Pressed!")
			activate_robot_srv(emergency_button)
			robot_on = False
	else:
		robot_on = True
	
	return

if __name__ == "__main__":
	rospy.init_node("niryo_one_emergency_buttom")
	rospy.wait_for_service("/niryo_one/activate_learning_mode")
	activate_robot_srv = rospy.ServiceProxy("/niryo_one/activate_learning_mode", SetInt)
	rospy.Subscriber("/niryo_one/rpi/digital_io_state", DigitalIOState, digital_io_callback)
	rospy.spin()