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

        motorStall('A', -25, -10)
        sleep(1)
        motorStall('A', 25, 10)
        sleep(1)
        motorStall('A', -25, -10)
        sleep(1)
        motorStall('A', 25, 10)
        sleep(1)