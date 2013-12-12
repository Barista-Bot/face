#!/usr/bin/env python2
import roslib
import rospy
from std_msgs.msg import String
from face.msg import faceRequests
from face.msg import headCoordinates
import subprocess
import os

process = None

def emotionCallback(data):
    rospy.loginfo("Changing emotion/talking status. emotion=" + str(data.emotion) + "talking" + str(data.talking))
    
    global process

    if (data.talking):
        process.stdin.write("e=" + data.emotion + ";t=true;m=" + data.question)
    else:
        process.stdin.write("e=" + data.emotion + ";t=false;m="+ data.question)

def headCallback(data):
    rospy.loginfo("Changing eye coordinates. ed=" + str(data.x) + ":" + str(data.y) + ":" + str(data.z))

    global process
    process.stdin.write("ed=" + str(data.x) + ":" + str(data.y) + ":" + str(data.z))

def listener():
    rospy.init_node('ROSFace', anonymous=True)

    rospy.Subscriber("/face/control", faceRequests, emotionCallback)
    rospy.Subscriber("/face/eyecontrol", headCoordinates, headCallback)

    global process

    directory = os.path.join(
        roslib.packages.get_pkg_dir('face'),
        "RobotFace/node/app.js"
    )
    rospy.loginfo("starting " + directory)
    process = subprocess.Popen(["nodemon", directory], stdin=subprocess.PIPE)
    rospy.spin()

if __name__ == '__main__':
    listener()
