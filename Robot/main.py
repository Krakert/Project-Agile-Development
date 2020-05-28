#!/usr/bin/env python

# import installed libraries
from naoqi import qi
from nao import nao
import paho.mqtt.client as mqtt
import configRobot as cfg
import random
import time

# Defines
# Setup for the MQTT broker
# Sub to the topic, here Js will sent the String to say
topicMain = cfg.MQTT["TOPIC_MAIN"]
topicSpeak = cfg.MQTT["TOPIC_SPEAK"]
topicNAVI = cfg.MQTT["TOPIC_NAVI"]

client = mqtt.Client(cfg.MQTT["CLIENT"])
client.username_pw_set(username=cfg.MQTT["USERNAME"], password=cfg.MQTT["PASSWORD"])

# Setup for the Nao robot
NAO = nao(cfg.NAO["NAME"])
openSession = NAO.connect(cfg.NAO["IP_ADRESS"], cfg.NAO["PORT"])

# enumeratie of 'website'
HOME = "0"
BEWEGING = "1"
GAMES = "2"
SODOKU = "2.1"
REKENEN = "2.2"
REKENEN1 = "2.2.1"
REKENEN2 = "2.2.2"
REKENEN3 = "2.2.3"
MUZIEK = "3"
NIEUWS = "4"
HULP = "5"

audioFile = None
page = None
done = None
# Start MQTT connection with the broker and subscribe to the topic
client.connect(cfg.MQTT["BROKER"])
client.subscribe([(topicSpeak, 0), (topicNAVI, 0)])


# Callback function for MQTT Broker
def on_message(client, userdata, msg):
    global page
    global audioFile
    print (msg.topic + msg.payload.decode("utf-8"))

    if msg.topic == topicNAVI:
        page = str(msg.payload.decode("utf-8"))
    if msg.topic == topicSpeak:
        nao.audio.say(msg.payload, openSession)


# Set dataFromMqtt back to Null
def updateToZeo(topic):
    client.publish(topic, "")


def main():
    global audioFile
    global done
    global page
    global dataFromMqtt
    client.loop_start()
    while True:
        client.on_message = on_message
        if page == HOME:
            nao.audio.killAudio(openSession)
            # pick a random line out the config file
            nao.audio.say(cfg.DICTIONARY[0][random.randint(0, len(cfg.DICTIONARY[0])) - 1], openSession)
            page = None
        elif page == BEWEGING:
            nao.audio.say(cfg.DICTIONARY[1][random.randint(0, len(cfg.DICTIONARY[0])) - 1], openSession)
            page = None
        elif page == GAMES:
            nao.audio.say(cfg.DICTIONARY[2][random.randint(0, len(cfg.DICTIONARY[0])) - 1], openSession)
            page = None
        elif page == SODOKU:
            nao.audio.say(cfg.DICTIONARY[3][random.randint(0, len(cfg.DICTIONARY[0])) - 1], openSession)
            page = None
        elif page == REKENEN:
            nao.audio.say(cfg.DICTIONARY[4][random.randint(0, len(cfg.DICTIONARY[0])) - 1], openSession)
            page = None
        elif page == MUZIEK:
            if done is not True:
                nao.audio.say(cfg.DICTIONARY[7][random.randint(0, len(cfg.DICTIONARY[0])) - 1], openSession)
                done = True
            if audioFile == "motten":
                print("Liedje")
                nao.audio.playAudioFile(openSession, "", "animations/Stand/Gestures/Hey_1",
                                        "/home/nao/wav/krakers_1590589230.mp3")
                audioFile = None
        elif page == NIEUWS:
            if done is not True:
                nao.audio.say(cfg.DICTIONARY[8][random.randint(0, len(cfg.DICTIONARY[0])) - 1], openSession)
                done = True
        elif page == HULP:
            nao.audio.say(cfg.DICTIONARY[9][random.randint(0, len(cfg.DICTIONARY[0])) - 1], openSession)
            page = None


if __name__ == '__main__':
    main()
