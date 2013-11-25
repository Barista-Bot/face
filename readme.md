face
====================

Eg.
```
$ rostopic pub /face/control face/faceRequests "emotion: 'joyous'
talking: false
question: ''"
```

ROS topic: /face/control
- emotion=[sad, happy, joyous, default, anticipation, confused]
- talking=[true,false]
- question=[some_string]

Credits:
- https://github.com/Sergeus/HCR
- https://github.com/bandinigo/RobotFace
