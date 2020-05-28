import qi
from arm import arm
from leg import leg
from audio import audio
from head import head


class nao:
    name = None
    arm = arm()
    leg = leg()
    audio = audio()
    head = head()

    def __init__(self, name):
        self.name = name

    def connect(self, ip, port):
        print (ip)
        print (port)
        session = qi.Session()
        session.connect("tcp://" + ip + ":" + str(port))
        # Get the robot up (standing) and let him breath
        motion_service = session.service("ALMotion")
        posture_service = session.service("ALRobotPosture")

        life_service = session.service("ALAutonomousLife")
        life_service.setAutonomousAbilityEnabled("BasicAwareness", True)
        life_service.setAutonomousAbilityEnabled("AutonomousBlinking", True)

        motion_service.wakeUp()

        posture_service.goToPosture("StandInit", 3)
        motion_service.setBreathEnabled('Body', True)

        return session

    def runBuildInAnimation(self, session, toShow):
        buildInAnimation = session.service("ALAnimationPlayer")
        qi.async(buildInAnimation.run, toShow)


    def blinkLed(self, session):
        blink = session.service("ALLeds")
        blink.off()