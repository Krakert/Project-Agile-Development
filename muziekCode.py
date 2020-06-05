#opgezocht door Renze, http://doc.aldebaran.com/2-8/naoqi/audio/alaudioplayer-api.html#ALAudioPlayerProxy::playFile
import sys
from naoqi import qi
import time
import random

"""""
#simpele functie om de nao te laten lopen
def walk(session, moveAmount = []):
    motion = session.service("ALMotion")
    motion.moveInit()
    motion.moveTo(moveAmount[0], moveAmount[1], 0)
"""""

def choose_song(choice):

    # open sessie
    session = qi.Session()
    session.connect("padrick.robot.hva-robots.nl:9559")

    # spraak service
    tts = session.service("ALTextToSpeech")

    # audio service
    audio_Player = session.service("ALAudioPlayer")

    # postuur service
    posture = session.service("ALRobotPosture")

    # animatie service
    animation_player = session.service("ALAnimationPlayer")

    # tegelijkertijd acties uitvoeren mbv qi.async
    # qi.async(animation_player.run, "animations/Stand/Gestures/Hey_1")
    # qi.async(audioPlayer.playFile, "/home/nao/wav/goosser4_1587549525.mp3")

    # input van de mqtt moet op de plek van de 1 komen bij choice.
    # dit is een soort van switchcase om liedjes + tegelijkertijd animatie en liedjes af te spelen.

    #defineer animaties
    wave = "animations/Stand/Gestures/Hey_1"

    #defineer liedjes
    song_names = ["Aan de amsterdamse grachten van Wim Sonneveld",
                  "Geef mij maar Amsterdam gekozen van Johnny Jordaan",
                  "Opzij opzij opzij van Herman van Veen",
                  "Ik ben vandaag zo vrolijk van Herman van Veen",
                  "twee motten van Dorus"]

    song_location = ["/home/nao/wav/goosser4_1587549525.mp3",
                     "/home/nao/wav/goosser4_1587549611.mp3",
                     "/home/nao/wav/goosser4_1587549697.mp3",
                     "/home/nao/wav/goosser4_1587549774.mp3",
                     "/home/nao/wav/goosser4_1587549936.mp3"]

    #keuze vanaf nummer 1
    choice = choice - 1
    
    #fouten afvang verkeerde input
    nummers_lengte = len(song_names)
    if choice > nummers_lengte or choice < nummers_lengte:
        tts.say("Sorry dit is geen optie.")
        sys.exit()

    #random tekst voor na het afspelen van het nummer.
    eind_lied_tekst = ["Dat was een leuk liedje.",
                       "Was dat niet fantastisch?!",
                       "Dat nummer geeft de dag weer kleur."]
    eind_nummer = random.randint(0, 2)

    #laten staan van de robot
    posture.goToPosture("StandInit", 1.0)
    time.sleep(2.0)

    #afspelen van het nummer
    tts.say("U heeft het nummer" + song_names[choice] + " gekozen.")
    fut1 = qi.async(animation_player.run, wave)
    fut2 = qi.async(audio_Player.playFile, song_location[choice])
    fut1.wait()
    fut2.wait()
    time.sleep(1)
    tts.say(eind_lied_tekst[eind_nummer])

def main():
    # open sessie
    session = qi.Session()
    session.connect("padrick.robot.hva-robots.nl:9559")
    tts = session.service("ALTextToSpeech")
    tts.say("hallo ik doe het")
    choose_song(-1)

if __name__ == "__main__":
    main()