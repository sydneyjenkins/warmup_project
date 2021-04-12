# warmup_project

Robot behavior: drive in square
This feature makes the robot drive in a square indefinitely. To accomplish this, I have the robot drive in a straight line for a specified amount of time, then stop and turn left at a 90 degree angle. 

I include all relevant functions in the class MakeSquare. The init function initializes the ROS node and sets up the publisher. The sideturn function tells the robot to move forward for 10 seconds before stopping and turning left at a 90 degree angle. The run function repeatedly calls the sideturn function so that the robot will move forward and turn left indefinitely, thus moving in a square. 

I provide a gif in the bags directory. 

Robot behavior: follow person
This feature makes the robot pursue an object in its surroundings and approach it until it is some distance away. It should be able to modify its path if the object is moved. It pursues an object in front of it, and if no such object exists, it will pursue the closest object. 

I include all relevant functions in the class Follower. The init function initializes the ROS node, sets up the publisher, and subscribes to the laser scanner. The image_callback function uses the data from the laser scanner to see if there's anything in front of the robot. If there is not, then the robot identifies the angle corresponding to the closest object, if such an angle exists, and rotates to face it. Once facing an object, it moves forward until it is some distance away, and then stops. 

I provide a gif in the bags directory. 

Behavior: follow wall
This feature makes the robot approach a wall and then move beside it at some distance indefinitely. It can approach the wall from any angle and round corners. The robot is a little slow. 

I include all relevant functions in the class Follower. The init function initializes the ROS node, sets up the publisher, and subscribes to the laser scanner. The image_callback function uses the data from the laser scanner to see if there's a wall to the right of the robot or if the wall is further than some distance. If the wall is further than some distance, then the robot moves forward. If the robot is by the wall but the angle between them is too large or small, the robot adjusts the angle by rotating. If the robot approaches a wall in front of it, it rotates to the left. Additionally, if the wall is to the right and there are no walls within distance in front of the robot, then the robot will move forward until it gets close to a wall, at which point it starts to turn. 

I provide a gif in the bags directory.

Challenges: 
To accomplish the driving in a square task, I had to form a basic udnerstanding of how to use ROS. Because I had no prior experience, this was difficult, and required a lot of background reading and searching documentation for relevant commands. Additionally, when I was coding the wall follower, the robot kept stopping a distance away from the wall for no apparaent reason. After struggling with this for a while, I reached out to Pouya and he realized that whenever you restart the gazebo world, it can change such that what the robot sees is different from what you see. 


Future Work: 
If I had more time, I would have tried to make my code a bit cleaner. Additionally, I would have tried to make the wall follower more graceful and quick. In it's current form, the robot is very slow and tends to correct its position a lot, meaning it doesn't move in very straight lines. I think it would look a lot nicer if the robot was able to cleanly turn once it encountered a wall and move in a straight line until it encounters a corner. However, I didn't have as much time to work on the wall follower as I had hoped because I had to spend extra time trying to figure out why the robot was stopping in front of the wall, as discussed in teh previous paragraph.

Takeaways: 
- I learned the basics of ROS, which will be critical for future programming assignments. I learned new commands to accomplish tasks such as making the robot turn and change its speed. In addition, I learned the basics of how to structure ROS code. 
- I learned that sometimes it's bad to restart the gazebo world. This is because then what you see might not be what the robot sees. This subsequently makes it very hard to understand what the code is doing and to debug it. 