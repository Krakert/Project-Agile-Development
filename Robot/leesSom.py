from naoqi import qi
import paho.mqtt.client as mqtt

# Defines
# Setup for the MQTT broker
broker = "mqtt.hva-robots.nl"
topicSpeak = "krakers/PAD/NAO/SAY"

client = mqtt.Client("Audio_receiver")
client.username_pw_set(username="krakers", password="kuNH5LNWptsGrPfL6Azh")

# Variables
dataToSay = ""
client.connect(broker)
client.subscribe(topicSpeak)


# Callback function for MQTT Broker
def on_message(client, userdata, msg):
    global dataToSay
    if msg.topic == topicSpeak:
        dataToSay = str(msg.payload.decode("utf-8"))
        print (dataToSay)

def updateToZero():
    #client.publish(topicSpeak, "")
    global dataToSay
    dataToSay = ""
def main():
    global dataToSay

    session = qi.Session()
    session.connect("padrick.robot.hva-robots.nl:9559")
    tts = session.service("ALTextToSpeech")

    client.loop_start()
    client.publish(topicSpeak, "")

    while True:
        client.on_message = on_message
        tts.say(dataToSay)
        updateToZero()


if __name__ == "__main__":
    main()
