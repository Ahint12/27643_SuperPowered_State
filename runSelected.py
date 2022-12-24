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
        # Start coding your Run here
        print("Starting runSelected()", file=sys.stderr)

        # twoWheelTurn('Left', 230, 3000, 333)
        # WheelShutdown()
        # move_steering.on_for_degrees(0, -10, 150, True)
        # WheelShutdown()
        motorStall('A', 15, 10)
        motorStall('D', -10, -7)
        BackMotorShutdown()