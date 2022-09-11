#!/usr/bin/env python3
import rospy
import time
import pygame


####################################### Gain set for this code is 2.0 ################################################

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

    gear1 = 0
    gear2 = 0
    gear3 = 0
    gear4 = 0
    gear5 = 0
    gear6 = 0


    while not rospy.is_shutdown():
        axes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


        pygame.event.pump()
#        print(joystick.get_axis(2))
#        if joystick.get_button(18) != 1 and joystick.get_axis(2) < 1.1 and joystick.get_axis(2) > -1.1:
#            axes[1] = float("{0:.2f}".format((-0.50 * joystick.get_axis(2) + 0.50)))

        if joystick.get_button(12) == 1 and joystick.get_axis(1) < 0.50:
            gear1 = 1
            gear2 = 0
            gear3 = 0
            gear4 = 0
            gear5 = 0
            gear6 = 0
            
        if joystick.get_button(13) == 1 and joystick.get_axis(1) < 0.50:
            gear1 = 0
            gear2 = 1
            gear3 = 0
            gear4 = 0
            gear5 = 0
            gear6 = 0

        if joystick.get_button(14) == 1 and joystick.get_axis(1) < 0.50:
            gear1 = 0
            gear2 = 0
            gear3 = 1
            gear4 = 0
            gear5 = 0
            gear6 = 0

        if joystick.get_button(15) == 1 and joystick.get_axis(1) < 0.50:
            gear1 = 0
            gear2 = 0
            gear3 = 0
            gear4 = 1
            gear5 = 0
            gear6 = 0

        if joystick.get_button(16) == 1 and joystick.get_axis(1) < 0.50:
            gear1 = 0
            gear2 = 0
            gear3 = 0
            gear4 = 0
            gear5 = 1
            gear6 = 0

        if joystick.get_button(17) == 1 and joystick.get_axis(1) < 0.50:
            gear1 = 0
            gear2 = 0
            gear3 = 0
            gear4 = 0
            gear5 = 0
            gear6 = 1

        if joystick.get_button(12) == 0 and joystick.get_button(13) == 0 and joystick.get_button(14) == 0 and joystick.get_button(15) == 0 and joystick.get_button(16) == 0 and joystick.get_button(17) == 0:
            gear1 = 0
            gear2 = 0
            gear3 = 0
            gear4 = 0
            gear5 = 0
            gear6 = 0


        if joystick.get_button(18) == 1 and joystick.get_axis(2) < 1.1 and joystick.get_axis(2) > -1.1:
            axes[1] = -0.5*float("{0:.2f}".format((-0.50 * joystick.get_axis(2) + 0.50)))

        if joystick.get_axis(0) < -0.03 and joystick.get_axis(2) < 0.89: #joystick.get_axis(2) < 1.1 and joystick.get_axis(2) > -1.1:
            axes[3] = -0.5*joystick.get_axis(0)

        if joystick.get_axis(0) > 0.03 and joystick.get_axis(2) < 0.89: #joystick.get_axis(2) < 1.1 and joystick.get_axis(2) > -1.1:
            axes[3] = -0.5*joystick.get_axis(0)

        gears = [gear1,gear2,gear3,gear4,gear5,gear6]


        if joystick.get_button(18) != 1 and joystick.get_axis(2) < 1.1 and joystick.get_axis(2) > -1.1:
            if gears[0] == 1:
                axes[1] = 0.3*float("{0:.2f}".format((-0.50 * joystick.get_axis(2) + 0.50)))
            elif gears[1] == 1:
                axes[1] = 0.4*float("{0:.2f}".format((-0.50 * joystick.get_axis(2) + 0.50)))
            elif gears[2] == 1:
                axes[1] = 0.5*float("{0:.2f}".format((-0.50 * joystick.get_axis(2) + 0.50)))
            elif gears[3] == 1:
                axes[1] = 0.65*float("{0:.2f}".format((-0.50 * joystick.get_axis(2) + 0.50)))
            elif gears[4] == 1:
                axes[1] = 0.8*float("{0:.2f}".format((-0.50 * joystick.get_axis(2) + 0.50)))
            elif gears[5] == 1:
                axes[1] = float("{0:.2f}".format((-0.50 * joystick.get_axis(2) + 0.50)))


        print(axes[1],axes[3])
        print(gears)


        # publish joy message
        msg = Joy(header=None, axes=axes, buttons=buttons)
        pub.publish(msg)
        rospy.sleep(1/HZ)
#        rospy.sleep(0.5)


if __name__ == '__main__':
    try:
        keyCatcher()
    except rospy.ROSInterruptException:
         pass
