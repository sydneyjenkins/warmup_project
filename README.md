# warmup_project

Robot behavior: drive in square
This feature makes the robot drive in a square indefinitely. To accomplish this, I have the robot drive in a straight line for a specified amount of time, then stop and turn left at a 90 degree angle. 

I include all relevant functions in the class MakeSquare. The init function initializes the ROS node and sets up the publisher. The sideturn function tells the robot to move forward for 10 seconds before stopping and turning left at a 90 degree angle. The run function repeatedly calls the sideturn function so that the robot will move forward and turn left indefinitely, thus moving in a square. 

I provide a gif in the bags directory. 


Challenges: 
To accomplish the driving in a square task, I had to form a basic udnerstanding of how to use ROS. Because I had no prior experience, this was difficult, and required a lot of background reading and searching documentation for relevant commands. 


Future Work: 
If I had more time, I would have tried to make my code a bit cleaner. 

Takeaways: 
- I learned the basics of ROS, which will be critical for future programming assignments. I learned new commands to accomplish tasks such as making the robot turn and change its speed. In addition, I learned the basics of how to structure ROS code. 
