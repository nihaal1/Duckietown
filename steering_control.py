#!/usr/bin/env python3
import rospy
import time
import pygame

from sensor_msgs.msg import Joy

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
axis_values = {}

HZ = 30

#main where implementation happens

def keyCatcher():
    rospy.init_node('joy-cli')
    pub = rospy.Publisher('~joy', Joy, queue_size=1)

    while not rospy.is_shutdown():
        axes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


        pygame.event.pump()
#        print(joystick.get_axis(2))
        if joystick.get_button(18) != 1 and joystick.get_axis(2) < 1.1 and joystick.get_axis(2) > -1.1:
            axes[1] = float("{0:.2f}".format((-0.50 * joystick.get_axis(2) + 0.50)))

        if joystick.get_button(18) == 1 and joystick.get_axis(2) < 1.1 and joystick.get_axis(2) > -1.1:
            axes[1] = -float("{0:.2f}".format((-0.50 * joystick.get_axis(2) + 0.50)))

#        if joystick.get_axis(0) < -0.05:
        if joystick.get_axis(0) < -0.03 and joystick.get_axis(2) < 0.89:
            axes[3] = -float("{0:.2f}".format(joystick.get_axis(0)))

#        if joystick.get_axis(0) > 0.05:
        if joystick.get_axis(0) > 0.03 and joystick.get_axis(2) < 0.89:
           axes[3] = -float("{0:.2f}".format(joystick.get_axis(0)))

        print(axes[1],axes[3])



        # publish joy message
        msg = Joy(header=None, axes=axes, buttons=buttons)
        pub.publish(msg)
        rospy.sleep(1/HZ)


if __name__ == '__main__':
    try:
        keyCatcher()
    except rospy.ROSInterruptException:
         pass
