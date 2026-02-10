import asyncio

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SongService:
    def __init__(self):
        self.sp = None

    def init_client(self, client_id: str, client_secret: str):
        """Initialize Spotify client. Called at startup."""
        auth_manager = SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret,
        )
        self.sp = spotipy.Spotify(auth_manager=auth_manager)

    async def search(self, query: str, limit: int = 5) -> list[dict]:
        results = await asyncio.to_thread(
            self.sp.search, q=query, type="track", limit=limit
        )
        tracks = results["tracks"]["items"]
        return [
            {
                "title": track["name"],
                "artist": ", ".join(a["name"] for a in track["artists"]),
                "album": track["album"]["name"],
                "spotify_url": track["external_urls"]["spotify"],
                "album_art_url": (
                    track["album"]["images"][0]["url"]
                    if track["album"]["images"]
                    else None
                ),
            }
            for track in tracks
        ]


song_service = SongService()
