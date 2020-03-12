class audio:

    def say(self, text,session):
        textToSpeechService = session.service("ALTextToSpeech")
        textToSpeechService.say(text)