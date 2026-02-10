import asyncio
import os
import tempfile

import whisper


class WhisperService:
    def __init__(self, model_size: str = "base"):
        self.model = None
        self.model_size = model_size

    def load_model(self):
        """Load the Whisper model. Called once at app startup."""
        self.model = whisper.load_model(self.model_size)

    async def transcribe(self, audio_bytes: bytes, file_extension: str = ".wav") -> dict:
        """Transcribe audio bytes to text. Runs Whisper in a thread to avoid blocking."""
        with tempfile.NamedTemporaryFile(suffix=file_extension, delete=False) as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name

        try:
            result = await asyncio.to_thread(self.model.transcribe, tmp_path)
            return {
                "text": result["text"].strip(),
                "language": result.get("language", "en"),
            }
        finally:
            os.unlink(tmp_path)


# Singleton instance
whisper_service = WhisperService()
