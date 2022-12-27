import speech_recognition as sr
from os.path import join


def run(speech_to_text):
    with sr.Microphone() as source:
        print("What would you like to name your file?")
        audio = speech_to_text.listen(source)
    filename = speech_to_text.recognize_google(audio)
    if ".txt" not in filename:
        filename += ".txt"
    # Get input for username on GUI when implementing GUI
    username = "21bguntupalli"
    path = "/Users/" + username + "/Desktop"
    try:
        file = open(join(path, filename), "w")
        print("Say what you would like to write into the file. Say \"stop\" \"done\" or \"quit\" when done")
        while True:
            with sr.Microphone() as source:
                audio = speech_to_text.listen(source)
            input_text = speech_to_text.recognize_google(audio)
            if input_text == "stop" or input_text == "done" or input_text == "quit":
                file.close()
                print("Successfully created, wrote, and closed file. File is in your desktop.")
                break
            else:
                file.write(input_text)
    except:
        print("Something went wrong, going back to main menu...")
