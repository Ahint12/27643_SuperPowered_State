#!/usr/bin/env python3
# 
# Filename: allRuns.py
#

import os
import sys
from time import sleep, time

from defineRobot import *
from myBlocks import *




def Trun1A():
    motorStall('A', -25, -10)
    FrontMotor.on_for_degrees(10, 40, True)
    FrontMotor.off(brake=False)
    motorStall('D', -10, -8)

def Trun1B():
    motorStall('A', 25, 10)

def Trun1C():
    motorStall('A', -25, 10)
    FrontMotor.off(brake=False)
    motorStall('A', 25, 10)

def Run1_Thread():
    if (True):
        
        RobotName = os.popen("cat /etc/hostname").read()
        print("Using robot: %s" % (RobotName), file=sys.stderr)
        #########################################################
        # RUN 1: ?? Points
        #########################################################

        #####
        # M08: Watch Television - 20 points
        #####
        run1A = Thread(target=Trun1A)
        run1A.start()
        driveStraight(20, 50, False)
        driveStraight(45, 490, False)
        driveStraight(20, 100, True)
        
        #####
        # M07: Wind Turbine - 30 points
        #####
        driveStraight(-25, 100, True)
        run1B = Thread(target=Trun1B)
        run1B.start()
        if (RobotName == "ASHBOT"):
            oneWheelTurn('Right', 250, 2000, 225)
        else:
            oneWheelTurn('Right', 250, 2000, 175)
        WheelShutdown()
        driveStraight(20, 50, False)    
        driveStraight(45, 380, False)
        lineDetect(15, 3, "Black", False)
        lineDetect(15, 3, "White", True)
        # driveStraight(15, 10, True)
        if (RobotName == "ASHBOT"):
            oneWheelTurn('Left', 300, 2000, 330)
        else:
            oneWheelTurn('Left', 300, 2000, 330)
        WheelShutdown()
        driveStraight(-20, 60, True)
        motorStall('A', -25, -10)
        FrontMotor.on_for_degrees(10, 40, True)
        FrontMotor.off(brake=False)
        driveStraight(20, 330, True)
        sleep(0.3)
        driveStraight(-20, 150, True)
        move_tank.on_for_degrees(20, -20, 50)
        WheelShutdown()
        move_tank.on_for_degrees(-15, 15, 50)
        WheelShutdown()
        driveStraight(20, 300, True)
        sleep(0.1)
        driveStraight(-20, 150, True)
        move_tank.on_for_degrees(20, -20, 50)
        WheelShutdown()
        move_tank.on_for_degrees(-15, 15, 50)
        WheelShutdown()
        driveStraight(20, 300, True)
        sleep(0.1)
        driveStraight(-20, 150, True)
        move_tank.on_for_degrees(20, -20, 50)
        WheelShutdown()
        move_tank.on_for_degrees(-15, 15, 50)
        WheelShutdown()
        driveStraight(20, 300, True)
        sleep(0.1)

        #####
        # M15: Rechargeable Battery
        #####
        driveStraight(-20, 50, False)
        driveStraight(-40, 190, True)
        motorStall('D', 20, 17)
        BackMotor.off(brake=False)
        if (RobotName == "ASHBOT"):
            twoWheelTurn('Right', 200, 2000, 265)
        else:
            twoWheelTurn('Right', 200, 2000, 355)
        WheelShutdown()
        twoWheelTurn('Left', 200, 2000, 35)
        WheelShutdown()        
        driveStraight(25, 190, False)
        move_steering.on_for_degrees(0, 15, 100, True)
        driveStraight(-20, 50, True)
        WheelShutdown()
        sleep(0.6)
        motorStall('A', 25, 10)
        BackMotor.off(brake=False)

        #####
        # M06: Hybrid Car
        #####
        if (RobotName == "ASHBOT"):
            twoWheelTurn('Left', 200, 2000, 95)
        else:
            twoWheelTurn('Left', 200, 2000, 170)
        WheelShutdown()   
        driveStraight(-20, 50, False)
        driveStraight(-45, 425, True)
        WheelShutdown()
        # sleep(2.0)
        oneWheelTurn('Left', 200, 3000, 20)
        WheelShutdown()
        # sleep(2.0)
        BackMotor.on_for_degrees(-85, 150, True)
        BackMotorShutdown()
        # sleep(2.0)
        BackMotor.on_for_degrees(30, 145, True)
        BackMotor.off(brake=False)

        #####
        # M05: Smart Grid
        #####
        if (RobotName == "ASHBOT"):
            oneWheelTurn('Right', 300, 2000, 310)
        else:
            oneWheelTurn('Right', 300, 2000, 270)
        WheelShutdown()
        driveStraight(-20, 50, False)
        driveStraight(-50, 700, True)
        lineDetect(-15, 2, "White", False)
        lineDetect(-15, 2, "Black", True)
        WheelShutdown()
        driveStraight(20, 20, True)
        twoWheelTurn('Left', 200, 2000, 120)
        WheelShutdown()
        driveStraight(20, 65, True)
        lineSquare(15, 'Black', 'Right', 0.3)
        WheelShutdown()
        lineSquare(15, 'White', 'Left', 0.2)
        WheelShutdown()
        lineSquare(-12, 'Black', 'Right', 0.2)
        WheelShutdown()
        driveStraight(15, 70, True)
        motorStall('A', -25, -10)
        driveStraight(-15, 90, True)

        #####
        # M10: Power Plant
        #####
        run1C = Thread(target=Trun1C)
        run1C.start()
        lineSquare(-12, 'White', 'Right', 0.2)
        WheelShutdown()
        lineSquare(15, 'Black', 'Left', 0.2)
        WheelShutdown()
        lineSquare(-12, 'White', 'Right', 0.2)
        WheelShutdown()
        driveStraight(-20, 50, False)
        driveStraight(-45, 400, True)
        WheelShutdown()
        if (RobotName == "ASHBOT"):
            # twoWheelTurn('Right', 150, 3200, 330)
            move_tank.on_for_degrees(12, -12, 340)
        else:
            twoWheelTurn('Right', 280, 2500, 333)
        WheelShutdown()
        motorStall('A', -25, 10)
        FrontMotor.off(brake=False)
        driveStraight(20, 50, False)
        driveStraight(45, 200, True)
        lineSquare(15, 'White', 'Right', 0.2)
        lineSquare(15, 'Black', 'Left', 0.2)
        lineSquare(-15, 'White', 'Right', 0.2)
        # sleep(5.0)
        driveStraight(-20, 100, True)
        motorStall('A', -25, -10)
        FrontMotor.on_for_degrees(10, 30, True)
        FrontMotor.off(brake=False)
        driveStraight(20, 50, True)
        # sleep(2.0)
        FrontMotor.on_for_degrees(100, 85, True)
        driveStraight(20, 55, True)        
        # sleep(2.0)
        FrontMotor.on_for_degrees(-50, 120, True)
        FrontMotor.off(brake=False)
        driveStraight(-15, 100, True)
        twoWheelTurn('Left', 280, 2500, 140)
        driveStraight(25, 50, False)
        driveStraight(80, 1700, True)


        '''
        driveStraight(-15, 50, True)
        sleep(0.5)
        RWheel.on_for_degrees(25, 140)
        RWheelShutdown()
        LWheel.on_for_degrees(-25, 150)  
        LWheelShutdown()
        driveStraight(-70, 1050, True)
        '''
        # Return to masterProgram()

        

def Run2_Thread():
    if (True):
        BackMotor.off(brake=False)
        # Return to masterProgram()


def Trun3A():
    motorStall('A', 6, 4)
    motorStall('D', -15, -10)
    BackMotorShutdown()

def Trun3B():
    motorStall('A', 15, 8)
    motorStall('D', 10, 7)
    BackMotor.on_for_degrees(-10, 20, False)

def Run3_Thread():
    if (True):
        
        #########################################################
        # RUN 3: ?? Points
        #########################################################

        run3A = Thread(target=Trun3A)
        run3A.start()
        # move_steering.on_for_degrees(0, 30, 180) 
        driveStraight(30, 200, True)
        turnLineDetect('B', 25, 2, 'Black', True)
        turnLineDetect('C', 15, 2, 'Black', False)
        turnLineDetect('C', 15, 2, 'White', True)
        PLF_Degrees1(2, -1, 600, True)
        PLF_LineDetect1(2, -1, 'White', False)
        PLF_LineDetect1(2, -1, 'Black', True)
        oneWheelTurn('Right', 200, 2000, 50)
        driveStraight(20, 40, True)
        FrontMotor.on_for_degrees(-8, 70, True)
        FrontMotor.off(brake=False)
        run3B = Thread(target=Trun3B)
        run3B.start()
        move_steering.on_for_degrees(0, 20, 300)
        WheelShutdown()
        BackMotor.on_for_degrees(-20, 60, True)
        BackMotorShutdown()
        BackMotor.on_for_degrees(30, 60, True)
        BackMotorShutdown()
        sleep(0.2)
        BackMotor.on_for_degrees(-25, 60, True)
        BackMotorShutdown()
        BackMotor.on_for_degrees(30, 60, True)
        BackMotorShutdown()
        sleep(0.2)
        BackMotor.on_for_degrees(-25, 60, True)
        BackMotorShutdown()
        BackMotor.on_for_degrees(30, 60, True)
        BackMotorShutdown()
        driveStraight(-20, 50, False)
        driveStraight(-30, 270, True)
        RWheel.on_for_degrees(20, 20, True)
        WheelShutdown()
        motorStall('A', -15, -8)
        move_steering.on_for_degrees(-12, -20, 50, brake=False)
        move_steering.on_for_degrees(-16, -50, 400, brake=False)
        driveStraight(-80, 1000, True)


        # Return to masterProgram()

        
def Trun4A():
    motorStall('A', 15, 7)

def Run4_Thread():
    if (True):

        #########################################################
        # RUN 4: 0 Points
        #########################################################

        run4A = Thread(target=Trun4A)
        run4A.start()
        driveStraight(30, 510, True)
        motorStall('A', -15, -7)
        FrontMotorShutdown()
        move_steering.on_for_degrees(-7, -20, 50)
        move_steering.on_for_degrees(-16, -60, 600)
        # Return to masterProgram(), reset display
        PrintRunNumbersToDisplay()


def Trun5A():
    motorStall('A', 15, 10)

def Run5_Thread():
    if (True):

        #########################################################
        # RUN 5: ?? Points
        #########################################################

        #####
        # M01: Innovation Project & M13: Power-To-X
        #####
        run5A = Thread(target=Trun5A)
        run5A.start()
        driveStraight(45, 1300, True)
        driveStraight(-30, 300, True) 

        #####
        # M12: Water Reservoir
        #####
        move_tank.on_for_degrees(-15, 15, 165, True)
        WheelShutdown()
        driveStraight(30, 110, True)
        driveStraight(-20, 50, True)
        FrontMotor.on_for_degrees(-10, 100)
        FrontMotorShutdown()
        driveStraight(-30, 250, True)

        sound.set_volume(pct=100)
        # sound.play_file('/home/robot/sounds/NeverGonnaGive.wav', volume=100)
        sound.play_file('/home/robot/sounds/fanfare.wav', volume=100)

        # Return to masterProgram(), reset display
        PrintRunNumbersToDisplay()


def Run1(state):
    if state:
        print("Run1 button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 1", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()

        t = multiprocessing.Process(target=Run1_Thread)
        t.start()

        while True:
            if btn.any():
                sound.play_note("E4", 0.25)
                print("Abort Run button pressed", file=sys.stderr)  
                t.terminate()
                WheelShutdown()
                break
            if (not t.is_alive()): 
                print("Run1_Thread successfully completed, exiting", file=sys.stderr)  
                break 
            sleep(0.5)

        PrintRunNumbersToDisplay()


def Run2(state):
    if state:
        print("Run2 button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 2", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()

        t = multiprocessing.Process(target=Run2_Thread)
        t.start()

        while True:
            if btn.any():
                sound.play_note("E4", 0.25)
                print("Abort Run button pressed", file=sys.stderr)  
                t.terminate()
                WheelShutdown()
                break
            if (not t.is_alive()): 
                print("Run2_Thread successfully completed, exiting", file=sys.stderr)  
                break 
            sleep(0.5)

        PrintRunNumbersToDisplay()


def Run3(state):
    if state:
        print("Run3 button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 3", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()

        t = multiprocessing.Process(target=Run3_Thread)
        t.start()

        while True:
            if btn.any():
                sound.play_note("E4", 0.25)
                print("Abort Run button pressed", file=sys.stderr)  
                t.terminate()
                WheelShutdown()
                break
            if (not t.is_alive()): 
                print("Run3_Thread successfully completed, exiting", file=sys.stderr)  
                break 
            sleep(0.5)

        PrintRunNumbersToDisplay()


def Run4(state):
    if state:
        print("Run4 button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 4", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()

        t = multiprocessing.Process(target=Run4_Thread)
        t.start()

        while True:
            if btn.any():
                sound.play_note("E4", 0.25)
                print("Abort Run button pressed", file=sys.stderr)  
                t.terminate()
                WheelShutdown()
                break
            if (not t.is_alive()): 
                print("Run4_Thread successfully completed, exiting", file=sys.stderr)  
                break 
            sleep(0.5)

        PrintRunNumbersToDisplay()


def Run5(state):
    if state:
        print("Run5 button pressed", file=sys.stderr)  
        sound.beep()
        # Clear the first 2 rows of text on the LCD screen using the lcd.rectangle function
        lcd.rectangle(False, x1=0, y1=0, x2=177, y2=39, fill_color='white',outline_color='white')
        lcd.text_pixels("RUN 5", clear_screen=False, x=0, y=0, text_color='black', font=DisplayFont)
        lcd.update()

        t = multiprocessing.Process(target=Run5_Thread)
        t.start()

        while True:
            if btn.any():
                sound.play_note("E4", 0.25)
                print("Abort Run button pressed", file=sys.stderr)  
                t.terminate()
                WheelShutdown()
                break
            if (not t.is_alive()): 
                print("Run5_Thread successfully completed, exiting", file=sys.stderr)  
                break 
            sleep(0.5)

        PrintRunNumbersToDisplay()