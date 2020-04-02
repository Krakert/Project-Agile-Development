import qi
from nao import nao


def main():
    NAO = nao("PADrick")
    openSession = NAO.connect("127.0.0.1", 50270)
    NAO.talk.say("Hello", openSession)

if __name__ == '__main__':
    main()
