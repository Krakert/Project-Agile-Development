import time
from naoqi import ALProxy
class leg:
    name = None

    def __init__(self, name):
        self.name = name

    def move(self, session):
        print("leg move")

        motion = session.service("ALMotion")
        motion.moveInit()
        motion.moveTo(0.1, 0.1, 0)

    def talkAndWalk(self, text, session):
        motion = ALProxy("ALMotion", "padrick.local", 9559)
        tts    = ALProxy("ALTextToSpeech", "padrick.local", 9559)
        motion.moveInit()
        motion.post.moveTo(0.3, 0, 0)
        time.sleep(1)
        tts.say(text)