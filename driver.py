import speech_recognition
import speech_recognition as sr
import translator
import transcriber
import song_finder
import calculator

speech_to_text = sr.Recognizer()

commands = [
    "calculate", "calculator", "Calculator", "Calculate", "translate", "Translate", "Translator", "translator",
    "Find a song", "Find the song", "find a song", "find the song", "Write to file", "write to file", "Speech to text",
    "speech to text"
]


def start():
    with sr.Microphone() as source:
        print("What would you like to do?")
        print("Translate")
        print("Calculate")
        print("Find a Song")
        print("Write to file")
        audio = speech_to_text.listen(source)
    return audio


while True:
    try:
        start_audio = start()
        input_text = speech_to_text.recognize_google(start_audio)
        if input_text in commands:
            break
        else:
            print("Command does not exist. Try Again")
    except speech_recognition.UnknownValueError:
        print("Couldn't understand what you said. Try Again")

if input_text == "calculate" or input_text == "calculator" or input_text == "Calculate" or input_text == "Calculator":
    output = calculator.run(speech_to_text)

elif input_text == "translate" or input_text == "translator" or input_text == "Translate" or input_text == "Translator":
    translated_text = translator.run(speech_to_text)
    print(translated_text)
