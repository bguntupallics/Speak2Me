from pydantic import BaseModel


class AudioTranscriptionResponse(BaseModel):
    text: str
    language: str
    duration_seconds: float | None = None
