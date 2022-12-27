import speech_recognition as sr
from googletrans import Translator, constants
import lyricsgenius

genius = lyricsgenius.Genius("iGDnfitT658AgmGeWByUI0QrAmiUbJKv1d2LnPojGzDE2aCELIza1l8lBDxr5onD")
translator = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Speak!")
#     audio = translator.listen(source)
#
# print("You Said: " + translator.recognize_google(audio))

result = genius.search("i get those goosebumps every time")
song = result['hits'][0]['result']['id']
song2 = result['hits'][1]['result']['id']
found = genius.search_song(song_id=song)
found2 = genius.search_song(song_id=song2)
print(found.title)
print(found2)
