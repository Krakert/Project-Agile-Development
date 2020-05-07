from flask import Flask, render_template, url_for, redirect
from flask_mqtt import Mqtt

app = Flask(__name__)

# Mqtt Setup
app.config['MQTT_BROKER_URL'] = 'mqtt.hva-robots.nl'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'krakers'
app.config['MQTT_PASSWORD'] = 'kuNH5LNWptsGrPfL6Azh'
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
# Start connection
mqtt = Mqtt(app)

dataFromMqtt = ""


# Connect to the right topic
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    # Sub to the right topic
    mqtt.subscribe('krakers/PAD/WEB')


# Get a new message
@mqtt.on_message()
def handle_mqtt_message(client, userdata, msg):
    global dataFromMqtt
    dataFromMqtt = str(msg.payload.decode("utf-8"))


# routes aangemaakt zodat er genavigeerd kan worden!
@app.route('/')
@app.route('/home')
@app.route('/Home')
@app.route('/index')
@app.route('/Index')
def main():
    return render_template('index.html')



@app.route('/Sudoku')
@app.route('/sudoku')
def sudoku():
    return render_template('minigames_sudoku.html', title='Sudoku')

@app.route('/Rekenen')
@app.route('/rekenen')
def Rekenen():
    return render_template('minigames_rekenen.html', title='Rekenen')


@app.route('/Minigames')
@app.route('/minigames')
def minigames():
    return render_template('minigames.html', title='Minigames')


@app.route('/Beweeg')
@app.route('/beweeg')
def beweeg():
    global dataFromMqtt
    if dataFromMqtt == '#':
        render_template('index.html')
        return redirect('/')
    return render_template('beweeg.html', title='Beweeg')


@app.route('/Ondersteuning')
@app.route('/ondersteuning')
def ondersteuning():
    return render_template('ondersteuning.html', title='Ondersteuning')


@app.route('/Bestel')
@app.route('/bestel')
def bestel():
    return render_template('bestel.html', title='Bestel')


# debug = True houdt de server running!
if __name__ == '__main__':
    app.run(debug=True)
