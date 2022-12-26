import speech_recognition as sr
from googletrans import Translator, constants

translator = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak!")
    audio = translator.listen(source)

print("You Said: " + translator.recognize_google(audio))
