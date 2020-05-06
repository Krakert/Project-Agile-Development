#opgezocht door Renze, http://doc.aldebaran.com/2-8/naoqi/audio/alaudioplayer-api.html#ALAudioPlayerProxy::playFile__ssCR
from naoqi import qi

def main():
    # open sessie
    session = qi.Session()
    session.connect("padrick.robot.hva-robots.nl:9559")

    # spraak service
    tts = session.service("ALTextToSpeech")

    # audio service
    audioPlayer = session.service("ALAudioPlayer")

    # postuur service
    posture = session.service("ALRobotPosture")

    # animatie service
    animation_player = session.service("ALAnimationPlayer")

    # tegelijkertijd acties uitvoeren mbv qi.async
    # qi.async(animation_player.run, "animations/Stand/Gestures/Hey_1")
    # qi.async(audioPlayer.playFile, "/home/nao/wav/goosser4_1587549525.mp3")

    # input van de mqtt moet op de plek van de 1 komen bij choise.
    # dit is een soort van switchcase om liedjes + tegelijkertijd animatie en liedjes af te spelen.
    choise = 1

    if choise is 1:
        tts.say("u heeft het nummer Aan de amsterdamse grachten gekozen van Wim Sonneveld.")
        qi.async(animation_player.run, "animations/Stand/Gestures/Hey_1")
        qi.async(audioPlayer.playFile, "/home/nao/wav/goosser4_1587549525.mp3")
    elif choise is 2:
        tts.say("u heeft het nummer Aan Geef mij maar Amsterdam gekozen van Johnny Jordaan.")
        qi.async(animation_player.run, "animations/Stand/Gestures/Hey_1")
        #qi.async(audioPlayer.playFile, "/home/nao/wav/goosser4_1587549611.mp3")
    elif choise is 3:
        tts.say("u heeft het nummer Aan Opzij opzij opzij van Herman van Veen.")
        qi.async(animation_player.run, "animations/Stand/Gestures/Hey_1")
        #qi.async(audioPlayer.playFile, "/home/nao/wav/goosser4_1587549697.mp3")
    elif choise is 4:
        tts.say("u heeft het nummer Aan Ik ben vandaag zo vrolijk van Herman van Veen.")
        qi.async(animation_player.run, "animations/Stand/Gestures/Hey_1")
        #qi.async(audioPlayer.playFile, "/home/nao/wav/goosser4_1587549774.mp3")
    elif choise is 5:
        tts.say("u heeft het nummer Aan twee motten van Dorus.")
        qi.async(animation_player.run, "animations/Stand/Gestures/Hey_1")
        #qi.async(audioPlayer.playFile, "/home/nao/wav/goosser4_1587549697.mp3")

if __name__ == "__main__":

    main()


