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

        BackMotor.on_for_degrees(-15, 110, True)
        BackMotorShutdown()
        motorStall('D', -10, -7)        