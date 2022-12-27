import math
import speech_recognition as sr

accepted_terms = [
    "add", "subtract", "multiply", "divide", "squared", "cube root", "^", "*", "/", "√", "-", "+", "power", "cubed"
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
            command.append("**")
        elif words[i] == "/":
            command.append(words[i])
        elif words[i] == "*":
            command.append(words[i])
        elif words[i] == "-":
            command.append(words[i])
        elif words[i] == "+":
            command.append(words[i])
        elif words[i] == "cubed":
            command.append(3)
            command.append("**")
        elif words[i] == "squared":
            command.append(2)
            command.append("**")
    return command


def calculate(command):
    a = command[0]
    b = command[2]
    if command[1] == "+":
        return float(a + b)
    elif command[1] == "-":
        return float(a - b)
    elif command[1] == "*":
        return float(a * b)
    elif command[1] == "/":
        return float(a / b)
    elif command[1] == "**":
        return float(a ** b)

