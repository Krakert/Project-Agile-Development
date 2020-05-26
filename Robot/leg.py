import time
class leg:
    def __init__(self):
        pass

    def talkAndWalk(self, session, text, timeToSpeak, moveAmount = []):
        motion = session.service("ALMotion")
        tts    = session.service("ALTextToSpeech")
        motion.moveInit()
        motion.moveTo(moveAmount[0], moveAmount[1], 0)
        time.sleep(timeToSpeak)
        tts.say(text)