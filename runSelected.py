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

        motorStall('A', -25, -10)
        FrontMotor.on_for_degrees(10, 40, True)
        FrontMotor.off(brake=False)
        driveStraight(20, 300, True)
        sleep(0.5)
        driveStraight(-20, 140, True)
        move_tank.on_for_degrees(30, -30, 50)
        WheelShutdown()
        move_tank.on_for_degrees(-20, 20, 50)
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
        driveStraight(-20, 140, True)
        move_tank.on_for_degrees(30, -30, 50)
        WheelShutdown()
        move_tank.on_for_degrees(-20, 20, 50)
        WheelShutdown()
        driveStraight(20, 300, True)
        sleep(0.3)

        driveStraight(-20, 50, False)
        WheelShutdown()

        