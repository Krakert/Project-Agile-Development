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
# Start MQTT connection with the broker and subscribe to the topic
client.connect(cfg.MQTT["BROKER"])
client.subscribe([(topicSpeak, 0), (topicNAVI, 0)])


# Callback function for MQTT Broker
def on_message(client, userdata, msg):
    global page
    global audioFile
    if msg.topic == topicNAVI:
        page = str(msg.payload.decode("utf-8"))
    if msg.topic == topicSpeak:
        print (msg.payload.decode("utf-8"))
        audioFile


# Set dataFromMqtt back to Null
def updateToZeo(topic):
    client.publish(topic, "")


def main():
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
        elif page == MUZIEK:
            nao.audio.say(cfg.DICTIONARY[7][random.randint(0, len(cfg.DICTIONARY[0])) - 1], openSession)
            print(audioFile)
            if audioFile == "motten":
                print ("Hoer")
                nao.audio.playAudioFile(openSession, "101 bars", "animations/Stand/Gestures/Hey_1", "/home/nao/wav/goosser4_1587549936.mp3")
            # page = None
        elif page == NIEUWS:
            nao.audio.say(cfg.DICTIONARY[8][random.randint(0, len(cfg.DICTIONARY[0])) - 1], openSession)
            page = None
        elif page == HULP:
            nao.audio.say(cfg.DICTIONARY[9][random.randint(0, len(cfg.DICTIONARY[0])) - 1], openSession)
            page = None


if __name__ == '__main__':
    main()
