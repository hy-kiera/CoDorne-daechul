# CoDrone-daechul
PBL Project in Hanyang University : A drone with attendance instead of you!

## Members
| Name | Role | 
|:----:|:----:|
|[이하영](github.com/hy-kiera)|Develop(image)|
|[조경찬](github.com/devcre)|Develop(image)|
|[유현상](github.com/RyuHS1942)|Develop(camera)|
|[정은수](github.com/BinCHip)|Develop(codrone)|

## Goal
Create a drone that recognizes the room number and goes to the room of your choice.

## Environment
 - server
 ```
 Ubuntu 18.04 Bionic
 catkin
 melodic
 ```
 - codrone2(raspberry pi zero w)
 ```
 Raspbian Jessie
 catkin
 kinetic
 ```

## Requirements
 - server
 ```
 python==2.7
 python==3.6
 tensorflow==1.13.1
 cv_bridge==1.13.0
 numpy==1.13.3
 rospy==1.14.3
 opencv==1.11.14
 Keras==2.3.1
 ```
 - codrone2(raspberry pi zero w)
 ```
 python==2.7
 python==3.6
 rospy==1.12.14
 ```
 
## Getting Started 
1. clone the CoDrone-daechul project on your computer(server) and codrone2
```
git clone git@github.com:hy-kiera/CoDrone-daechul.git
```
2. set the recommened environment on your computer(server)
```
pip install <requirements> # they must be installed with pip(python2.x)
or
apt-get install <requirements>
```

3. go to your catkin repository and build
```
cd <YOUR_CATKIN_WORKSPACE>/CoDrone-daechul
catkin build
```

4. launch the project
 - server
 ```
 roslaunch object_detection object_detection.launch
 ```
 
## TODO
- [x] Communicate between raspberry pi 0 w and server
- [x] Send image captured by raspberry pi camera to server
- [ ] Control the codrone2 by server
- [ ] Detect the object(room number)
- [ ] Get the location value of the object(room number)
- [ ] Lane Tracking
