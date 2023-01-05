#!/usr/bin/env python3
# 
# Filename: runSelected.py
#

import os
import sys
from time import sleep, time

from defineRobot import *
from myBlocks import *



    
def runSelected():

    if (True):
        # Start coding your run here
        print("Starting runSelected()", file=sys.stderr)


        motorStall('D', 10, 7)
        BackMotor.on_for_degrees(-10, 20, False)
        BackMotorShutdown()
        sleep(0.2)
        BackMotor.on_for_degrees(-20, 55, True)
        BackMotorShutdown()
        BackMotor.on_for_degrees(30, 55, True)
        BackMotorShutdown()
        sleep(0.2)
        BackMotor.on_for_degrees(-25, 55, True)
        BackMotorShutdown()
        BackMotor.on_for_degrees(30, 55, True)
        BackMotorShutdown()
        sleep(0.2)
        BackMotor.on_for_degrees(-25, 55, True)
        BackMotorShutdown()
        BackMotor.on_for_degrees(30, 55, True)
        BackMotorShutdown()



        '''
        driveStraight(20, 80, True)
        LWheel.on_for_degrees(-20, 190, True)
        LWheelShutdown()
        RWheel.on_for_degrees(20, 350, True)
        RWheelShutdown()
        driveStraight(25, 230, True)
        lineSquare(12, 'Black', 'Left', 0.2)
        lineSquare(-15, 'White', 'Right', 0.2)
        motorStall('A', -10, -5)
        LWheel.on_for_degrees(20, 230, True)
        LWheelShutdown()
        FrontMotor.on_for_degrees(25, 100, True)
        '''

        '''
        lineDetect(15, 2, 'Black', True)
        oneWheelTurn('Left', 220, 2500, -200)
        sleep(3.0)
        lineDetect(15, 3, 'White', True)        
        sleep(3.0)
        lineDetect(15, 3, 'Black', True)

        # driveStraight(20, 100, True)

        driveStraight(35, 230, True)
        twoWheelTurn('Left', 170, 3500, 76)
        driveStraight(40, 100, False)
        driveStraight(50, 900, False)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(15, 'White', 'Left', 0.2)
        WheelShutdown()
        driveStraight(20, 300, True)
        sleep(0.3)
        driveStraight(-20, 140, True)
        move_tank.on_for_degrees(30, -30, 50)
        WheelShutdown()
        move_tank.on_for_degrees(-20, 20, 50)
        WheelShutdown()
        driveStraight(20, 300, True)
        sleep(0.3)

        driveStraight(-20, 50, False)
        WheelShutdown()
        '''