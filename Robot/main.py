#!/usr/bin/env python

# import installed libraries
import naoqi
from nao import nao
import paho.mqtt.client as mqtt

# Defines
# Setup for the MQTT broker
broker = "mqtt.hva-robots.nl"
# Sub to the topic, here Js will sent the String to say
topicSpeak = "krakers/PAD/NAO/SAY"

client = mqtt.Client("PC_receiver")
client.username_pw_set(username="krakers", password="kuNH5LNWptsGrPfL6Azh")

# Setup for the Nao robot
NAO = nao("PADrick")
IP_ADRES = "padrick.robot.hva-robots.nl"
PORT = 9559  # Use port 9559 for Online robot, for now Offline robot
openSession = NAO.connect(IP_ADRES, PORT)

# Variables
dataToSay = ""
dataFromMqtt = ""
# Start MQTT connection with the broker and subscribe to the topic
client.connect(broker)
client.subscribe(topicSpeak)


# Callback function for MQTT Broker
def on_message(client, userdata, msg):
    global dataToSay
    # global dataFromMqtt
    if msg.topic == topicSpeak:
        dataToSay = str(msg.payload.decode("utf-8"))
        #print(dataToSay)
        NAO.audio.say(dataToSay, openSession)
        updateToZeo()
    else:
        dataFromMqtt = str(msg.payload.decode("utf-8"))


# Set dataFromMqtt back to Null
def updateToZeo(topic):
    global dataFromMqtt
    dataFromMqtt = ""
    client.publish(topic, dataFromMqtt)


def main():
    global dataFromMqtt
    client.loop_start()
    # Send nothing to the sub
    client.publish(topicSpeak, "")

    while True:
        client.on_message = on_message



if __name__ == '__main__':
    main()
