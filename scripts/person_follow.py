#!/usr/bin/env python3

import rospy, cv2,  numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
# msg needed for /scan.
from sensor_msgs.msg import LaserScan

# How close we will get to wall.
distance = 0.4

class Follower:

        def __init__(self):
                #   set self.process_scan as the function to be used for callback.
                rospy.Subscriber("/scan", LaserScan, self.image_callback)

                # Get a publisher to the cmd_vel topic.
                self.twist_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

                self.twist = Twist()

        def image_callback(self, data):

                
                #cv2.circle(image, (5, 5), 20, (0,0,255), -1)
                angle_count = 0
                min_distance, min_angle = 500, 0
                if data.ranges[0] > 500:
                        min_angle = numpy.argmin(data.ranges)
                        #while (angle_count < 360 and data.ranges[angle_count] > 500):
                        #        angle_count = angle_count + 1
                        #        if data.ranges[angle_count] < min_distance: 
                        #                min_distance = data.ranges[angle_count]
                        #                min_angle = angle_count
                        self.twist.linear.x = 0
                        self.twist.angular.z = (min_angle*3.14159265/180)/3
                        self.twist_pub.publish(self.twist)
                else:
                        if data.ranges[angle_count] > distance:
                                # Go forward if not close enough to wall.
                                self.twist.linear.x = 0.1
                                self.twist.angular.z = 0
                                self.twist_pub.publish(self.twist)
                        else:
                                # Close enough to wall, stop.
                                self.twist.linear.x = 0
                                self.twist.angular.z = 0
                                self.twist_pub.publish(self.twist)
      
if __name__ == '__main__':

        rospy.init_node('person_follower')
        follower = Follower()
        rospy.spin()
