#opgezocht door Renze, http://doc.aldebaran.com/2-8/naoqi/audio/alaudioplayer-api.html#ALAudioPlayerProxy::playFile
from naoqi import qi
import time

#simpele functie om de nao te laten lopen
def walk(session, moveAmount = []):
    motion = session.service("ALMotion")
    motion.moveInit()
    motion.moveTo(moveAmount[0], moveAmount[1], 0)


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
    song_5 = "/home/nao/wav/goosser4_1587549936.mp3"

    song_name1 = "Aan de amsterdamse grachten van Wim Sonneveld"
    song_name2 = "Geef mij maar Amsterdam gekozen van Johnny Jordaan"
    song_name3 = "Opzij opzij opzij van Herman van Veen"
    song_name4 = "Ik ben vandaag zo vrolijk van Herman van Veen"
    song_name5 = "twee motten van Dorus"

    posture.goToPosture("StandInit", 1.0)
    time.sleep(2.0)

    if choice is 1:
        fut1 = qi.async(animation_player.run, wave)
        fut2 = qi.async(audio_Player.playFile, song_1)
        tts.say("U heeft het nummer" + song_name1 + " gekozen.")
        fut1.wait()
        fut2.wait()
        time.sleep(1)
        tts.say("Wat een klassieker!")
    elif choice is 2:
        fut1 = qi.async(animation_player.run, wave)
        fut2 = qi.async(audio_Player.playFile, song_2)
        tts.say("U heeft het nummer" + song_name2 + " gekozen.")
        fut1.wait()
        fut2.wait()
        time.sleep(1)
        tts.say("Geef mij maar Amsterdam, want in Rotjeknor heb ik niks te zoeken.")
    elif choice is 3:
        fut1 = qi.async(animation_player.run, wave)
        fut2 = qi.async(audio_Player.playFile, song_3)
        tts.say("U heeft het nummer" + song_name3 + " gekozen.")
        fut1.wait()
        fut2.wait()
        time.sleep(1)
        tts.say("Nou voor uit dan maar. Ik ga wel een stapje opzij.")
        walk(session, [0, 0.1])
    elif choice is 4:
        fut1 = qi.async(animation_player.run, wave)
        fut2 = qi.async(audio_Player.playFile, song_4)
        tts.say("U heeft het nummer" + song_name4 + " gekozen.")
        fut1.wait()
        fut2.wait()
        time.sleep(1)
        tts.say("Ik ben van dit nummer een stukje vrolijker geworden. U hopelijk ook!")
    elif choice is 5:
        fut1 = qi.async(animation_player.run, wave)
        fut2 = qi.async(audio_Player.playFile, song_5)
        tts.say("U heeft het nummer" + song_name5 + " gekozen.")
        fut1.wait()
        fut2.wait()
        time.sleep(1)
        tts.say("aaah altijd leuk zo een liedje van vroeger.")
    else:
        tts.say("Sorry, deze optie bestaat niet.")

def main():
    # open sessie
    session = qi.Session()
    session.connect("padrick.robot.hva-robots.nl:9559")

    choose_song(3)


if __name__ == "__main__":
    main()


