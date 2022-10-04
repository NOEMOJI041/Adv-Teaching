import os
import speech_recognition as sr
import requests
import json
import nlpcloud



# tomp3 = r"D:\PROJECTS\TEACHER\Shikshak\ggwp.webm D:\PROJECTS\TEACHER\Shikshak\Lecture1.mp3"
# towav = r"D:\PROJECTS\TEACHER\Shikshak\Lecture1.mp3 D:\PROJECTS\TEACHER\Shikshak\Lecture1.wav"
#
# print(".....converting videos....")
# os.system(tomp3)
# os.system(towav)
# print("....videos converted....")

r = sr.Recognizer()

with sr.AudioFile("D:/PROJECTS/TEACHER/Shikshak/Lecture1.wav") as source:
    audio = r.record(source, duration=100)

try:
    print("...converting speech to text...")
    text = r.recognize_google(audio)
    print(text)
    print("...speech-to-text done...")


    client = nlpcloud.Client("bart-large-cnn", "Your_Token")
    # Returns a json object.
    r = client.summarization(f"""{text}""")


    print(r)


except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0} ".format(e))



