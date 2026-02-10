from pydantic import BaseModel, Field


class SongSearchRequest(BaseModel):
    query: str = Field(..., description="Song title, lyrics snippet, or artist name")
    limit: int = Field(default=5, ge=1, le=20)


class SongResult(BaseModel):
    title: str
    artist: str
    album: str | None = None
    spotify_url: str
    album_art_url: str | None = None


class SongSearchResponse(BaseModel):
    query: str
    results: list[SongResult]
