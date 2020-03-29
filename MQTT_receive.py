import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(msg.payload)


broker = "mqtt.hva-robots.nl"
client = mqtt.Client("krakers_2")
client.username_pw_set(username="krakers", password="kuNH5LNWptsGrPfL6Azh")

client.connect(broker)  # connect to broker
client.subscribe("krakers/PAD")

client.loop_start()

while True:
    client.on_message = on_message