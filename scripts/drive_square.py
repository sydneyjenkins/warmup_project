#!/usr/bin/env python3

import rospy

# msgs needed for /cmd_vel
from geometry_msgs.msg import Twist, Vector3
import time

class MakeSquare(object):
    """ This node publishes ROS messages containing the 3D coordinates of a single point """

    def __init__(self):
        # initialize the ROS node
        rospy.init_node('makesquare')
        # setup publisher to the cmd_vel ROS topic
        self.robot_movement_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    def side_turn(self):
        # make the robot go straight for a given amount of time
        # before making a 90 degree left-hand turn
        rospy.sleep(1)
        r = rospy.Rate(.1)

        # setup the twist message we want to send
        my_path = Twist()
        start_time = time.time()
        my_path.linear.x = .1
        my_path.angular.z = 0
        # measure the amount of time that has elapsed since starting this "edge"
        # of the square, stopping once 10 seconds have passed
        while time.time() - start_time < 10: 
            rospy.sleep(1)
            self.robot_movement_pub.publish(my_path)

        start_time2 = time.time()
        # stop movement forward and turn left
        my_path.linear.x = 0
        my_path.angular.z = 30*3.1415926/180 #converting to radians
        rospy.sleep(1)
        # make turn
        self.robot_movement_pub.publish(my_path)
        rospy.sleep(1)

    def run(self):
        # have robot repeat movements indefinitely,
        # thus moving in a square
        while not rospy.is_shutdown():
            self.side_turn()

if __name__ == '__main__':
    # instantiate the ROS node and run it
    node = MakeSquare()
    node.run()

