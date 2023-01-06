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

        run6A = Thread(target=Trun6A)
        run6A.start()
        driveStraight(20, 50, False)
        driveStraight(35, 290, True)
        motorStall('A', -20, -10)
        driveStraight(15, 140, True)
        WheelShutdown()
        driveStraight(-15, 35, True)
        FrontMotor.on_for_degrees(12, 80)
        FrontMotorShutdown()
        FrontMotor.on_for_degrees(-20, 80)
        FrontMotorShutdown()
        FrontMotor.off(False)
        driveStraight(-25, 70, True)
        twoWheelTurn('Right', 200, 2000, 80)
        driveStraight(20, 50, False)
        driveStraight(40, 50, False)
        driveStraight(60, 800, False)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(15, 'White', 'Left', 0.2)
        WheelShutdown()
        driveStraight(20, 50, True)
        WheelShutdown()
        twoWheelTurn('Right', 170, 3500, 167)
        lineSquare(15, 'White', 'Left', 0.25)
        lineSquare(10, 'Black', 'Right', 0.2)
        lineSquare(10, 'White', 'Left', 0.3)
        FrontMotor.on_for_degrees(90, 50, True)
        FrontMotor.on_for_degrees(-80, 50, True)
        FrontMotorShutdown()
        FrontMotor.on_for_degrees(20, 30, True)
        driveStraight(-10, 25, True)
        LWheel.on_for_degrees(-15, 80, True)
        WheelShutdown()
        FrontMotor.on_for_degrees(-35, 42, False)
        LWheel.on_for_degrees(15, 80, True)
        lineSquare(-10, 'White', 'Left', 0.2)
        lineSquare(10, 'Black', 'Right', 0.2)
        oneWheelTurn('Left', 250, 2000, -300)
        driveStraight(20, 50, False)
        driveStraight(45, 50, False)
        driveStraight(85, 1600, True)











        '''
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