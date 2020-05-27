class audio:

    def say(self, text,session):
        textToSpeechService = session.service("ALTextToSpeech")
        print (text)
        textToSpeechService.say(text)

    def playAudioFile(self,session, talkBefore, talkAfter):
        self.say(talkBefore, session)
        animation_player = session.service("ALAnimationPlayer")
        audioPlayer = session.service("ALAudioPlayer")