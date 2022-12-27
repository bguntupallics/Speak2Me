import speech_recognition
import speech_recognition as sr
import translator
import transcriber
import song_finder
import calculator

speech_to_text = sr.Recognizer()

commands = [
    "calculate", "calculator", "translate", "Translate", "Translator", "translator",
    "Find a song", "Find the song", "find a song", "find the song", "Write to file", "write to file", "Speech to text",
    "speech to text", "transcribe"
]


def start():
    with sr.Microphone() as source:
        print("What would you like to do?")
        print("Translate")
        print("Calculate")
        print("Find a Song")
        print("Write to file")
        print("Say \"Exit\" to close application")
        audio = speech_to_text.listen(source)
    return audio


def run(input_text):
    if input_text == "calculate" or input_text == "calculator":
        output = calculator.run(speech_to_text)
        print(output)
    elif input_text == "translate" or input_text == "translator":
        translated_text = translator.run(speech_to_text)
        print(translated_text)
    elif input_text == "find the song" or input_text == "find a song" or input_text == "shazam":
        songs = song_finder.run(speech_to_text)
        number = 1
        for song in songs:
            print(str(number) + ". Song: " + song.title + ", By: " + song.artist)
            number += 1
    elif input_text == "transcribe" or input_text == "write to file" or input_text == "write to a file" or input_text == "speech to text":
        transcriber.run(speech_to_text)


while True:
    try:
        start_audio = start()
        text = speech_to_text.recognize_google(start_audio)
        if text in commands:
            run(text)
        elif text == "done" or text == "quit" or text == "exit" or text == "close" or text == "stop":
            print("Bye Bye!")
            break
        else:
            print("Command does not exist. Try Again")
    except speech_recognition.UnknownValueError:
        print("Couldn't understand what you said. Try Again")
