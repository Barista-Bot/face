#!/usr/bin/env python2

import rospy
import face.msg

class Controller(object):
    def __init__(self):
        self.pub = rospy.Publisher('/face/control', face.msg.faceRequests)

    def update(self, is_talking=False, message=''):
        self.pub.publish(face.msg.faceRequests(talking=is_talking, question=message))

    def clear(self):
        self.update(is_talking=False, message='')

