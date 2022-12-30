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
            command.append(float(words[i]))
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
            command.append("**")
            command.append(3)
        elif words[i] == "squared":
            command.append("**")
            command.append(2)
        elif words[i] == "root":
            if words[i - 1] == "square":
                command.append(float(1 / 2))
                command.append("root")
            elif words[i - 1] == "cube":
                command.append(float(1 / 3))
                command.append("root")
            elif words[i - 1] == "fourth":
                command.append(float(1 / 4))
                command.append("root")
            elif words[i - 1] == "fifth":
                command.append(float(1 / 5))
                command.append("root")
            elif words[i - 1] == "sixth":
                command.append(float(1 / 6))
                command.append("root")
            elif words[i - 1] == "seventh":
                command.append(float(1 / 7))
                command.append("root")
            elif words[i - 1] == "eight":
                command.append(float(1 / 8))
                command.append("root")
            elif words[i - 1] == "ninth":
                command.append(float(1 / 9))
                command.append("root")
            elif words[i - 1][0: len(words[i - 1]) - 2].isnumeric():
                number = float(words[i - 1][0: len(words[i - 1]) - 2])
                command.append(float(1/number))
                command.append("root")
            else:
                command.append(float(1 / 2))
                command.append("root")
        elif words[i] == "the" and words[i - 1] == "to":
            command.append("**")
            command.append(float(words[i + 1][0: len(words[i + 1]) - 2]))
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
    elif command[1] == "root":
        return float(b ** a)
