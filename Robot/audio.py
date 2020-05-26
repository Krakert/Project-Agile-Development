class audio:

    def say(self, text,session):
        textToSpeechService = session.service("ALTextToSpeech")
        print (text)
        textToSpeechService.say(text)