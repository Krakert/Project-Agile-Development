#opgezocht door Renze, http://doc.aldebaran.com/2-8/naoqi/audio/alaudioplayer-api.html#ALAudioPlayerProxy::playFile
from naoqi import qi
import motion
import time
"""""
def stepForwardOrBackward(Distance):                   dit is een functie om de robot te laten lopen, let op werkt nog niet volledig zuiver!
    # open sessie
    session = qi.Session()
    session.connect("padrick.robot.hva-robots.nl:9559")

    #bewegings service
    motion_service = session.service("ALMotion")
    X = Distance
    Y = 0.0
    Theta = 0.0
    Frequency = 0.0
    motion_service.moveToward(X, Y, Theta, [["Frequency", Frequency]])
    time.sleep(4.0)
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

    # animation_player.run("")
    # animation_player.runTag("hello")
    #defineer animaties
    wave = "animations/Stand/Gestures/Hey_1"

    #defineer locatie liedjes
    song_1 = "/home/nao/wav/goosser4_1587549525.mp3"
    song_2 = "/home/nao/wav/goosser4_1587549611.mp3"
    song_3 = "/home/nao/wav/goosser4_1587549697.mp3"
    song_4 = "/home/nao/wav/goosser4_1587549774.mp3"
    song_5 = "/home/nao/wav/goosser4_1587549697.mp3"

    song_name1 = "Aan de amsterdamse grachten van Wim Sonneveld"
    song_name2 = "Geef mij maar Amsterdam gekozen van Johnny Jordaan"
    song_name3 = "Opzij opzij opzij van Herman van Veen"
    song_name4 = "Ik ben vandaag zo vrolijk van Herman van Veen"
    song_name5 = "twee motten van Dorus"

    posture.goToPosture("StandInit", 1.0)
    time.sleep(2.0)

    if choice is 1:
        tts.say("U heeft het nummer" + song_name1 + " gekozen.")
        qi.async(animation_player.run, wave)
        qi.async(audio_Player.playFile, song_1)
        tts.say("Wat een klassieker!")
    elif choice is 2:
        tts.say("U heeft het nummer" + song_name2 + " gekozen.")
        qi.async(animation_player.run, wave)
        qi.async(audio_Player.playFile, song_2)
        tts.say("Geef mij maar Amsterdam, want in Rotjeknor heb ik niks te zoeken.")
    elif choice is 3:
        tts.say("U heeft het nummer" + song_name3 + " gekozen.")
        qi.async(animation_player.run, wave)
        qi.async(audio_Player.playFile, song_3)
        tts.say("Nou voor uit dan maar. Ik ga wel een stapje opzij.")
    elif choice is 4:
        tts.say("U heeft het nummer" + song_name4 + " gekozen.")
        qi.async(animation_player.run, wave)
        qi.async(audio_Player.playFile, song_4)
        tts.say("Ik ben van dit nummer een stukje vrolijker geworden. U hopelijk ook!")
    elif choice is 5:
        tts.say("U heeft het nummer" + song_name5 + " gekozen.")
        qi.async(animation_player.run, wave)
        qi.async(audio_Player.playFile, song_5)
        tts.say("aaah altijd leuk zo een liedje van vroeger.")
    else:
        tts.say("Sorry, deze optie bestaat niet.")

def main():
    # open sessie
    session = qi.Session()
    session.connect("padrick.robot.hva-robots.nl:9559")

    choose_song(6)


if __name__ == "__main__":
    main()


