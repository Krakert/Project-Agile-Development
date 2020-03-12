import qi
from arm import arm
from leg import leg
from audio import audio
class nao:
    name = None
    leftArm = arm("left arm")
    rightArm = arm("right arm")
    leftLeg = leg("Left Leg")
    talk = audio()

    def __init__(self, name):
        self.name = name

    def connect(self, ip, port):
        session = qi.Session()
        session.connect("tcp://" + ip + ":" + str(port))
        return session