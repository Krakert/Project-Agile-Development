import qi
from nao import nao


def main():
    NAO = nao("PADrick")
    openSession = NAO.connect("padrick.local", 9559)
    NAO.talk.say("Hello", openSession)
    NAO.leftLeg.talkAndWalk("Hallo Milo", openSession)



if __name__ == '__main__':
    main()
