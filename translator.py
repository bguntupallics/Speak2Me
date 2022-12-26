from googletrans import Translator, constants
import speech_recognition as sr

languages = {
    "Spanish", "French", "German", "Italian", "Portuguese", "Dutch"
}


def run(speech_to_text):
    with sr.Microphone() as source:
        print("what language would you like to translate to?")
        for language in languages:
            print(language)
        audio = speech_to_text.listen(source)
    language = speech_to_text.recognize_google(audio)
    with sr.Microphone() as source:
        print("What would you like to translate?")
        audio = speech_to_text.listen(source)
    text_to_translate = speech_to_text.recognize_google(audio)
    return translate(language, text_to_translate)


def translate(language, text):
    target = "en"
    source = "en"
    if language == "Spanish" or language == "spanish" or language == "espanol":
        target = "es"
    elif language == "Italian" or language == "italian" or language == "italiano" or language == "italiana":
        target = "it"
    elif language == "German" or language == "german" or language == "deutsch":
        target = "de"
    elif language == "French" or language == "french" or language == "francais":
        target = "fr"
    elif language == "Dutch" or language == "dutch" or language == "nederlands":
        target = "nl"
    elif language == "Portuguese" or language == "portuguese" or language == "portugues":
        target = "pt"

    translator = Translator()
    translation = translator.translate(text, src=source, dest=target)
    return translation.text
