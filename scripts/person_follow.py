#!/usr/bin/env python3

import rospy, cv2,  numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
# msg needed for /scan.
from sensor_msgs.msg import LaserScan

# How close we will get to person.
distance = 0.4

class Follower:

        def __init__(self):
                #   set self.process_scan as the function to be used for callback.
                rospy.Subscriber("/scan", LaserScan, self.image_callback)

                # Get a publisher to the cmd_vel topic.
                self.twist_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

                self.twist = Twist()

        def image_callback(self, data):
        # Sense and pursue person
                angle_count = 0
                min_distance, min_angle = 500, 0
                if data.ranges[0] > 500:
                        #If there's nothing in front of robot,
                        min_angle = numpy.argmin(data.ranges)
                        self.twist.linear.x = 0
                        self.twist.angular.z = (min_angle*3.14159265/180)/3
                        self.twist_pub.publish(self.twist)
                else:
                        if data.ranges[angle_count] > distance:
                                # If further than distance from person, keep approaching
                                self.twist.linear.x = 0.1
                                self.twist.angular.z = 0
                                self.twist_pub.publish(self.twist)
                        else:
                                # Close enough to person, stop
                                self.twist.linear.x = 0
                                self.twist.angular.z = 0
                                self.twist_pub.publish(self.twist)
      
if __name__ == '__main__':

        rospy.init_node('person_follower')
        follower = Follower()
        rospy.spin()
