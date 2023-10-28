#!/usr/bin/python3 Esta parte de tomo del sitio http://python4fun.blogspot.com/2008/06/get-key-press-in-python.html
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from numpy import pi
TERMIOS = termios
def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c


def main_code():
    rospy.init_node('move_turtle',anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel',Twist,queue_size=10)
    telportA=rospy.ServiceProxy('turtle1/teleport_absolute',TeleportAbsolute)
    telportR=rospy.ServiceProxy('turtle1/teleport_relative',TeleportRelative)
    rate = rospy.Rate(10)
    vel = Twist()
    res = TeleportAbsolute()

    while not rospy.is_shutdown():
        key=getkey()
        vel.linear.x = 0
        vel.angular.z = 0
        if key == b'w':
            vel.linear.x = 1
        elif key == b's':
            vel.linear.x = -1
        elif key == b'a':
            vel.angular.z = 1
        elif key == b'd':
            vel.angular.z = -1
        elif key == b'r':
            resp1=telportA(5.544445,5.544445,0)
        elif key == b' ':
            resp2 = telportR(0,pi)
        rospy.loginfo(key)
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        main_code()
    except rospy.ROSInterruptException:
        pass


