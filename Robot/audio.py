from naoqi import qi

audio = None
class audio:

    def say(self, text,session):
        textToSpeechService = session.service("ALTextToSpeech")
        textToSpeechService.say(text)


    def playAudioFile(self,session, talkBefore, animationToPlay, audioFileToPlay):
        global audio
        if talkBefore is not None:
            self.say(talkBefore, session)
        animation_player = session.service("ALAnimationPlayer")
        audioPlayer = session.service("ALAudioPlayer")
        qi.async(animation_player.run, animationToPlay)
        qi.async(audioPlayer.playFile, audioFileToPlay)

    def killAudio(self, session):
        speechPlayer = session.service("ALTextToSpeech")
        audioPlayer = session.service("ALAudioPlayer")
        audioPlayer.stopAll()
        speechPlayer.stopAll()