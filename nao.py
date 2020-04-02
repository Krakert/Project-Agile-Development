import qi
from arm import arm
from leg import leg
from audio import audio
from head import head
class nao:
    name = None
    arm = arm()
    leftLeg = leg("Left Leg")
    talk = audio()
    head = head()

    def __init__(self, name):
        self.name = name

    def connect(self, ip, port):
        session = qi.Session()
        session.connect("tcp://" + ip + ":" + str(port))
        return session

    def runBuildInAnimation(self, session):
        buildInAnimation = session.service("ALAnimationPlayer")
        buildInAnimation.run("animations/Stand/Gestures/Hey_1,")