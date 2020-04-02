#!/usr/bin/env python

#Import installed libraries
import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
import os

#Setup GPIO
GPIO.setmode(GPIO.BCM)                                                                              # Setup the pinlayout
GPIO.setwarnings(False)                                                                             # disable warnings

COLOM = [14, 15, 20]                                                                                # Input pins for the Coloms
ROW = [23, 24, 25, 8]                                                                               # Input pins for the Row
GPIO.setup(COLOM, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)                                              # Setup the inputs pins
GPIO.setup(ROW, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)                                                # with a pull down
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

KEYPAD = [                                                                                          # Grid for keypad
    [[1, 0], [2, 0], [3, 0]],
    [[4, 0], [5, 0], [6, 0]],
    [[7, 0], [8, 0], [9, 0]],
    [["*", 0], [0, 0], ["#", 0]]
]

running = True

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
def checkConnection():
    hostName = "8.8.8.8"
    try:
        response = os.system("ping -c 1 " + hostName)
    except Exception, e:
        return False
    if response == 0:
        return True


def on_disconnect(client, userdata, rc):
    client.connect(broker)

#Setup MQTT
broker="mqtt.hva-robots.nl"
client = mqtt.Client("Raspberry_pi")
client.username_pw_set(username="krakers",password="kuNH5LNWptsGrPfL6Azh")


while not running:
    if checkConnection():
        running = True
    else:
        time.sleep(1)

while running:
    valuePressedKey = checkPressed()
    if valuePressedKey is not None:
        client.on_disconnect = on_disconnect
        client.connect(broker, port = 1883, keepalive = 1)
        client.publish("krakers/PAD", valuePressedKey)
    time.sleep(0.0001)