import math
import speech_recognition as sr

accepted_terms = [
    "add", "plus", "subtract", "minus", "multiply", "times", "divide", "divided by", "to the", "squared", "cubed",
    "square", "cube", "root",
]


def run(speech_to_text):
    with sr.Microphone() as source:
        print("What would you like to calculate?")
        audio = speech_to_text.listen(source)
    command_text = speech_to_text.recognize_google(audio)
    command = parse(command_text)
    return calculate(command)


def parse(text):
    command = []
    words = str.split(text)
    for i in range(len(words)):
        if words[i].isnumeric():
            command.append(int(words[i]))
        elif words[i] == "^":
            operation = "**"
            command.append(operation)
    return command


def calculate(command):
    pass
