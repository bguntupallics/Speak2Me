from pydantic import BaseModel


class TranscribeRequest(BaseModel):
    text: str
    filename: str = "transcription.txt"


class TranscribeResponse(BaseModel):
    filename: str
    character_count: int
    content_preview: str
