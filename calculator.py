import math
import speech_recognition as sr

accepted_terms = [
    "add", "subtract", "multiply", "divide", "squared", "cube root"
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
        elif words[i] == "/":
            command.append(words[i])
        elif words[i] == "*":
            command.append(words[i])
        elif words[i] == "-":
            command.append(words[i])
        elif words[i] == "+":
            command.append(words[i])
    return command


def calculate(command):
    pass
