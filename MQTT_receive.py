# Simple test code for MQTT, when a message is send, the message will be printed.

import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(msg.payload)


broker = "mqtt.hva-robots.nl"
client = mqtt.Client("PC_receiver")
client.username_pw_set(username="krakers", password="kuNH5LNWptsGrPfL6Azh")
client.connect(broker)
client.subscribe("krakers/PAD")
client.loop_start()

while True:
    client.on_message = on_message