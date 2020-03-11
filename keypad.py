#!/usr/bin/env python

#import installed libraries
import RPi.GPIO as GPIO
import time

#setup GPIO
GPIO.setmode(GPIO.BCM)                                                                              # Setup the pinlayout
GPIO.setwarnings(False)                                                                             # disable warnings

KEYPAD = [                                                                                          # Grid for keypad
    [[1, 0], [2, 0], [3, 0]],
    [[4, 0], [5, 0], [6, 0]],
    [[7, 0], [8, 0], [9, 0]],
    [["*", 0], [0, 0], ["#", 0]]
]

COLOM = [14, 15, 18]                                                                                # Input pins for the Coloms
ROW = [23, 24, 25, 8]                                                                               # Input pins for the Row
GPIO.setup(COLOM, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)                                              # Setup the inputs pins
GPIO.setup(ROW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)                                                # with a pull down

def checkPressed():                                                                                 # this will check the buttons
    for i in range (len(ROW)):                                                                      # pressed
        for j in range (len(COLOM)):
            if GPIO.input(ROW[i]) and GPIO.input(COLOM[j]):
                KEYPAD[i][j][1] = 1                                                                 # When a button is pressed set
            if not GPIO.input(ROW[i]) and not GPIO.input(COLOM[j]) and KEYPAD[i][j][1]:             # position [x][x][1] to True,
                KEYPAD[i][j][1] = 0                                                                 # button is pressed.
                return KEYPAD[i][j][0]                                                              # When the button was pressed
                                                                                                    # and [x][x][1] is true
                                                                                                    # print the key from [x][x][0]