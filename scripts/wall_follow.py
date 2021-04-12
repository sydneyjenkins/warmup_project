#!/usr/bin/env python3

import rospy, cv2,  numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
# msg needed for /scan.
from sensor_msgs.msg import LaserScan

# How close we will get to wall.
distance = .8

class Follower:

        def __init__(self):
                rospy.init_node('wall_follow')

                #   set self.process_scan as the function to be used for callback.
                rospy.Subscriber("/scan", LaserScan, self.image_callback)

                # Get a publisher to the cmd_vel topic.
                self.twist_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

                self.twist = Twist()

        def image_callback(self, data):
                angle_count = 0
                #echo("/cmd_vel")
                min_angle = numpy.argmin(data.ranges)
                if (min_angle > 273 or min_angle <= 268) or (data.ranges[min_angle] > distance):# and data.ranges[min_angle] > distance:
                        min_angle = numpy.argmin(data.ranges)
                        #if min_angle == 0 and data.ranges[min_angle] > distance:
                        if data.ranges[min_angle] >= distance: 
                            self.twist.linear.x = 0.2
                            self.twist.angular.z = 0
                            self.twist_pub.publish(self.twist)
                        elif min_angle < 15 or min_angle > 345: 
                            self.twist.linear.x = 0
                            self.twist.angular.z = 30*3.14159265/180
                            self.twist_pub.publish(self.twist)
                        elif min_angle < 273: 
                            self.twist.linear.x = 0
                            #current_angle = 0 
                            #if True: #while(current_angle < 5):
                                #t1 = rospy.Time.now().to_sec()
                                #current_angle = 5*3.14159625/180*(t1-t0)
                            self.twist.angular.z = -3*3.14159265/180
                            self.twist_pub.publish(self.twist)
                        else:  
                            self.twist.linear.x = 0
                            self.twist.angular.z = 3*3.14159265/180
                            self.twist_pub.publish(self.twist)
                else:
                        if data.ranges[0] > distance+.4: #data.ranges[0] > distance+.05:
                                # Go forward if not close enough to wall.
                                self.twist.linear.x = 0.2
                                self.twist.angular.z = 0
                                self.twist_pub.publish(self.twist)
                        else:
                                # Close enough to wall, stop.
                                self.twist.linear.x = 0.2
                                self.twist.angular.z = 10*3.14159265/180
                                self.twist_pub.publish(self.twist)
      
if __name__ == '__main__':
        follower = Follower()
        rospy.spin()
