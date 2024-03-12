
import speech_recognition as sr
engine = sr.Recognizer()

#  read mp3 file
mp3FileName = 'myAudio.mp3'
with sr.AudioFile(mp3FileName) as source:
    print('File is being analised...')
    audio = engine.record(source)

#  Extract and print text
try:
    text = engine.recognize_google(audio)
    print(f'Text: {text}')
    txtFile = open('textFromMp3.txt', 'w')
    txtFile.writelines(text)
except:
    print('Something gone very wrong...')
