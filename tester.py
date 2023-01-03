import speech_recognition as sr
from googletrans import Translator
import lyricsgenius

genius = lyricsgenius.Genius("CLIENT ACCESS TOKEN HERE")
translator = sr.Recognizer()
trans = Translator()

# with sr.Microphone() as source:
#     print("Speak!")
#     audio = translator.listen(source)
#
# print("You Said: " + translator.recognize_google(audio))

# result = genius.search("i get those goosebumps every time")
# song = result['hits'][0]['result']['id']
# song2 = result['hits'][1]['result']['id']
# found = genius.search_song(song_id=song)
# found2 = genius.search_song(song_id=song2)
# print(found.title)
# print(found2)


