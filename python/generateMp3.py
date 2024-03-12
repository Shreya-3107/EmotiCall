mp3FileName = 'myAudio2.mp3'

import pyttsx3 as tts

engine = tts.init()

engine.save_to_file(
        '''this is a test file''', 
        mp3FileName
    )

engine.runAndWait()