import speech_recognition as sr
import lyricsgenius

genius = lyricsgenius.Genius("CLIENT ACCESS TOKEN")


def run(speech_to_text):
    with sr.Microphone() as source:
        print("Say the lyrics of the song you would like to find or the title of the song")
        audio = speech_to_text.listen(source)
    lyrics = speech_to_text.recognize_google(audio)
    return find_song(lyrics)


def find_song(lyrics):
    print(lyrics)
    result = genius.search(lyrics)
    songs = [
        genius.search_song(song_id=result['hits'][0]['result']['id']),
        genius.search_song(song_id=result['hits'][1]['result']['id']),
        genius.search_song(song_id=result['hits'][2]['result']['id']),
        genius.search_song(song_id=result['hits'][3]['result']['id']),
        genius.search_song(song_id=result['hits'][4]['result']['id'])
    ]
    return songs
