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
client.loop_start()

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
    NAO.talk.say("Welokm bij de oplevering", openSession)
    #NAO.runBuildInAnimation(openSession)       # Werkt door de Corona dus niet

    NAO.head.moveHead(openSession, ["HeadYaw", "HeadPitch"], [0,0], [2,2])

    while True:
        client.on_message = on_message
        if dataFromMqtt == "1":
            NAO.head.moveHead(openSession, ["HeadYaw", "HeadPitch"], [10, 10], [0.2, 0.2])
            updateToZeo()
        elif dataFromMqtt == "2":
            NAO.head.moveHead(openSession, ["HeadYaw", "HeadPitch"], [0,0], [0.2,0.2])
            updateToZeo()

if __name__ == '__main__':
    main()
