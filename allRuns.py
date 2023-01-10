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
    motorStall('A', 15, 10)

def Run1_Thread():
    if (True):
        
        RobotName = os.popen("cat /etc/hostname").read()
        print("Using robot: %s" % (RobotName), file=sys.stderr)
        #########################################################
        # RUN 1: ?? Points
        #########################################################

        run1A = Thread(target=Trun1A)
        run1A.start()
        driveStraight(20, 50, False)
        driveStraight(35, 290, True)
        motorStall('A', -20, -10)
        driveStraight(15, 140, True)
        WheelShutdown()
        driveStraight(-15, 35, True)
        FrontMotor.on_for_degrees(12, 80, True)
        # FrontMotorShutdown()
        FrontMotor.on_for_degrees(-20, 80, True)
        # FrontMotorShutdown()
        FrontMotor.off(False)
        driveStraight(-25, 70, True)
        twoWheelTurn('Right', 200, 2000, 80)
        driveStraight(20, 50, False)
        driveStraight(40, 50, False)
        driveStraight(65, 800, False)
        lineSquare(15, 'Black', 'Right', 0.2)
        lineSquare(15, 'White', 'Left', 0.2)
        WheelShutdown()
        driveStraight(20, 50, True)
        WheelShutdown()
        twoWheelTurn('Right', 170, 3500, 167)
        lineSquare(15, 'White', 'Left', 0.25)
        # lineSquare(10, 'Black', 'Right', 0.2)
        driveStraight(15, 30, False)
        lineSquare(10, 'White', 'Right', 0.2)
        FrontMotor.on_for_degrees(95, 60, True)
        FrontMotor.on_for_degrees(-80, 60, True)
        FrontMotorShutdown()
        FrontMotor.on_for_degrees(20, 35, True)
        driveStraight(-10, 25, True)
        LWheel.on_for_degrees(-15, 70, True)
        WheelShutdown()
        FrontMotor.on_for_degrees(-35, 42, False)
        LWheel.on_for_degrees(15, 70, True)
        lineSquare(-10, 'White', 'Left', 0.2)
        # lineSquare(10, 'Black', 'Right', 0.1)
        oneWheelTurn('Left', 280, 2000, -290)
        driveStraight(20, 50, False)
        driveStraight(45, 50, False)
        driveStraight(85, 1700, True)
        # Return to masterProgram()

def Trun2A():
    motorStall('A', 10, 5)
        
def Trun2B():
    motorStall('A', -10, -5)

def Run2_Thread():
    if (True):

        #########################################################
        # RUN 2: ?? Points
        #########################################################

        #####
        # M08: Watch Television - 20 points
        #####
        run2A = Thread(target=Trun2A)
        run2A.start()
        driveStraight(20, 50, False )
        driveStraight(45, 370, False)
        driveStraight(20, 120, True)

        #####
        # M07: Wind Turbine - 30 points
        #####
        driveStraight(-20, 30, False)
        driveStraight(-35, 100, False)
        driveStraight(-20, 30, True)
        RWheel.on_for_degrees(25, 205)
        RWheelShutdown()
        driveStraight(20, 50, False)
        driveStraight(45, 350, False)
        lineDetect(15, 3, "Black", False)
        lineDetect(15, 3, "White", True)
        # driveStraight(15, 7, True)
        # LWheel.on_for_degrees(25, 360)
        # LWheelShutdown()
        oneWheelTurn('Left', 280, 2000, 360)
        driveStraight(20, 210, True)
        sleep(0.1)
        driveStraight(-20, 90, True)
        driveStraight(20, 140, True)
        sleep(0.1)
        driveStraight(-20, 90, True)
        driveStraight(20, 140, True)
        sleep(0.1)
        driveStraight(-20, 90, True)
        driveStraight(20, 140, True)
        sleep(0.1)

        #####
        # M14: Toy Factory - 30 points
        #####
        driveStraight(-25, 50, False)
        driveStraight(-35, 300, True)
        sleep(0.3)
        driveStraight(20, 80, True)
        # LWheel.on_for_degrees(-20, 190, True)
        # LWheelShutdown()
        oneWheelTurn('Left', 280, 2000, -190)
        # RWheel.on_for_degrees(20, 350, True)
        # RWheelShutdown()
        oneWheelTurn('Right', 280, 2000, 350)
        driveStraight(20, 50, False)
        driveStraight(40, 180, True)
        lineSquare(12, 'Black', 'Left', 0.2)
        run2B = Thread(target=Trun2B)
        run2B.start()
        lineSquare(-15, 'White', 'Right', 0.1)
        # LWheel.on_for_degrees(25, 235, True)
        # LWheelShutdown()
        oneWheelTurn('Left', 280, 2000, 235)
        # LWheel.on_for_degrees(15, 60, True)
        # LWheelShutdown()
        # sleep(0.1)
        # LWheel.on_for_degrees(-15, 60, True)
        # LWheelShutdown()
        FrontMotor.on_for_degrees(15, 100, True)
        LWheel.on_for_degrees(-25, 35, True)
        LWheelShutdown()
        driveStraight(-20, 50, False)
        driveStraight(-85, 1600, True)
        BackMotor.off(brake=False)

        # Return to masterProgram()


def Trun3A():
    motorStall('D', 10, 7)
    BackMotor.on_for_degrees(-10, 20, True)
    # BackMotor.off(brake=False)

def Trun3B():
    # motorStall('D', -10, -7)
    BackMotor.on_for_degrees(-15, 110, True)
    BackMotorShutdown()

def Trun3C():
    BackMotor.on_for_degrees(15, 45, True)

def Trun3D():
    motorStall('D', -15, -10)
    BackMotor.on_for_degrees(10, 15, True)
    # BackMotor.off(brake=False)

def Run3_Thread():
    if (True):

        run3A = Thread(target=Trun3A)
        run3A.start()
        driveStraight(20, 140, True)
        oneWheelTurn('Right', 250, 2000, 205)
        WheelShutdown()
        driveStraight(20, 50, False)
        driveStraight(40, 50, False)
        driveStraight(60, 1000, True)
        WheelShutdown()
        BackMotor.on_for_degrees(-15, 110, True)
        BackMotorShutdown()
        # run3B = Thread(target=Trun3B)
        # run3B.start()
        LWheel.on_for_degrees(15, 20, True)
        driveStraight(20, 70, True)
        turnLineDetect('C', 15, 3, 'White', True)
        turnLineDetect('C', 15, 3, 'Black', True)
        RWheel.on_for_degrees(15, 40, True)
        RWheelShutdown()
        PLF_LineDetect1(3, 1, 'Black', True)
        run3C = Thread(target=Trun3C)
        run3C.start()
        oneWheelTurn('Right', 250, 2000, 350)
        driveStraight(-10, 40, True)
        motorStall('D', 15, 12)
        driveStraight(20, 55, True)
        run3D = Thread(target=Trun3D)
        run3D.start()        
        driveStraight(20, 120, True)
        twoWheelTurn('Right', 250, 2000, 190)
        driveStraight(20, 165, True)
        oneWheelTurn('Left', 250, 2000, 270)
        driveStraight(30, 60, False)
        lineSquare(15, 'Black', 'Left', 0.2)
        lineSquare(15, 'White', 'Right', 0.1)
        oneWheelTurn('Right', 200, 2000, 45)
        driveStraight(35, 180, True)
        oneWheelTurn('Right', 200, 2000, 245)
        WheelShutdown()
        driveStraight(35, 230, True)
        oneWheelTurn('Right', 200, 2000, 295)
        driveStraight(20, 50, False)
        driveStraight(40, 50, False)
        #driveStraight(80, 1800, True)
        move_steering.on_for_degrees(6, 80, 1700, True)
        WheelShutdown()
        
        
        # Return to masterProgram()


def Trun4A():
    motorStall('A', 6, 4)
    motorStall('D', -15, -10)
    BackMotorShutdown()

def Trun4B():
    motorStall('A', 15, 8)
    motorStall('D', 10, 7)
    BackMotor.on_for_degrees(-10, 20, False)
    BackMotorShutdown()

        
def Trun4Z():
    motorStall('A', -15, -7)
    motorStall('D', -10, -7)
    BackMotor.on_for_degrees(10, 60)
    BackMotor.off(brake=False)

def Run4_Thread():
    if (True):

        #########################################################
        # NEW RUN 4
        #########################################################

        run4A = Thread(target=Trun4A)
        run4A.start()
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
        FrontMotor.off(False)
        run4B = Thread(target=Trun4B)
        run4B.start()
        move_steering.on_for_degrees(0, 20, 300)
        WheelShutdown()
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
        driveStraight(-20, 50, False)
        driveStraight(-30, 260, True)
        RWheel.on_for_degrees(20, 20, True)
        WheelShutdown()
        motorStall('A', -15, -8)
        move_steering.on_for_degrees(-12, -20, 50, brake=False)
        move_steering.on_for_degrees(-17, -50, 400, brake=False)
        driveStraight(-85, 1000, True)
        WheelShutdown()

        '''
        #########################################################
        # OLD RUN 4
        #########################################################

        run4A = Thread(target=Trun4A)
        run4A.start()
        driveStraight(30, 510, True)
        motorStall('A', -15, -7)
        FrontMotorShutdown()

        #####
        # M03: Energy Storage - 35 points - 10 x 3 energy units + 5 points for removing tray
        #####
        lineSquare(-15, "Black", "Left", 0.2)
        lineSquare(-15, "White", "Left", 0.2)
        driveStraight(-15, 20, True)
        RWheel.on_for_degrees(20, 180)
        RWheelShutdown()
        driveStraight(20, 55, True)
        RWheel.on_for_degrees(20, 185)
        RWheelShutdown()
        driveStraight(-20, 90, True)
        BackMotor.on_for_degrees(-20, 37)
        BackMotorShutdown()
        move_steering.on_for_degrees(12, 80, 1900)
        WheelShutdown()
        '''

        # Return to masterProgram()


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
        WheelShutdown()
        run5A = Thread(target=Trun5A)
        run5A.start()
        driveStraight(20, 50, False)
        driveStraight(60, 1150, False)
        driveStraight(30, 100, True)
        sleep(0.1)
        driveStraight(-30, 230, True) 

        #####
        # M12: Water Reservoir
        #####
        move_tank.on_for_degrees(-15, 15, 170, True)
        WheelShutdown()
        driveStraight(30, 120, True)
        driveStraight(-20, 120, True)
        FrontMotor.on_for_degrees(-12, 110)
        FrontMotorShutdown()
        driveStraight(-30, 150, True)

        sound.set_volume(pct=100)
        sound.play_file('/home/robot/sounds/NeverGonnaGive.wav', volume=100)
        # sound.play_file('/home/robot/sounds/fanfare.wav', volume=100)

        # Return to masterProgram(), reset display


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