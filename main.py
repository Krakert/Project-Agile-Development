#!/usr/bin/env python

#import installed libraries
import qi
from nao import nao
import paho.mqtt.client as mqtt

# Defines
# Setup for the MQTT broker
broker = "mqtt.hva-robots.nl"
topic = "krakers/PAD"
client = mqtt.Client("PC_receiver")
client.username_pw_set(username="krakers", password="kuNH5LNWptsGrPfL6Azh")

# Setup for the Nao robot
NAO = nao("PADrick")
openSession = NAO.connect("127.0.0.1", 55938)

# Variables
dataFromMqtt = ""
# Start MQTT connection with the broker and subscribe to the topic
client.connect(broker)
client.subscribe(topic)


# Callback function for MQTT Broker
def on_message(client, userdata, msg):
    global dataFromMqtt
    dataFromMqtt = str(msg.payload.decode("utf-8"))

def updateToZeo():
    global dataFromMqtt
    dataFromMqtt = ""
    client.publish(topic, dataFromMqtt)

def main():
    global dataFromMqtt
    client.loop_start()
    client.publish(topic, "")
    print ("Connected to Mqtt")
    nao.audio.say("Welokm bij de oplevering", openSession)
    #NAO.runBuildInAnimation(openSession)       # Werkt door de Corona dus niet

    nao.head.moveHead(openSession, ["HeadYaw", "HeadPitch"], [0,0], [2,2])

    while True:
        client.on_message = on_message
        if dataFromMqtt == "1":
            nao.head.moveHead(openSession, ["HeadYaw", "HeadPitch"], [10, 10], [0.2, 0.2])
            updateToZeo()
        elif dataFromMqtt == "2":
            nao.head.moveHead(openSession, ["HeadYaw", "HeadPitch"], [0,0], [0.2,0.2])
            updateToZeo()
        elif dataFromMqtt == "3":
            nao.arm.moveArm(openSession, "left", 0.5, ["ShoulderRoll", "ElbowYaw"], [70, 30], 0.3)
            updateToZeo()
        elif dataFromMqtt == "4":
            nao.arm.moveArm(openSession, "right", 0.5, ["ShoulderRoll", "ElbowYaw"], [70, 30], [2, 0.3])
            updateToZeo()
        elif dataFromMqtt == "5":
            nao.arm.moveArmToRestPosistion(openSession, "left")
            updateToZeo()
        elif dataFromMqtt == "6":
            nao.arm.moveArmToRestPosistion(openSession, "right")
            updateToZeo()
        elif dataFromMqtt == "7":
            nao.arm.moveArm(openSession, "left", 1, ["ShoulderPitch", "ShoulderRoll", "ElbowYaw", "Hand"], [-71, 17, -5, 1.0], 1)
            nao.arm.moveArm(openSession, "left", 1, ["ElbowRoll"], [-65], 0.3)
            nao.arm.moveArm(openSession, "left", 1, ["ElbowRoll"], [-2], 0.3)
            nao.arm.moveArm(openSession, "left", 1, ["ElbowRoll"], [-65], 0.3)
            nao.arm.moveArm(openSession, "left", 1, ["ElbowRoll"], [-2], 0.3)
            dataFromMqtt = "5"
        elif dataFromMqtt == "8":
            nao.leg.talkAndWalk(openSession, "Wat leuk zo`n oplevering digitaal", 2, [0.2, 0])
            updateToZeo()
if __name__ == '__main__':
    main()
