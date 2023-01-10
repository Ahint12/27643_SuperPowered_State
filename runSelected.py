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

        motorStall('A', -15, -10)
        FrontMotor.off(brake = False)
        sleep(1.0)
        LWheel.on_for_degrees(15, 60, True)
        sleep(1.0)
        LWheel.on_for_degrees(-15, 60, True)
        sleep(1.0)
        FrontMotor.on_for_degrees(26, 100, True)
        sleep(1.0)
        FrontMotor.off(brake = False)