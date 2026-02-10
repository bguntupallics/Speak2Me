class TranscriptionService:
    def generate(self, text: str, filename: str) -> dict:
        if not filename.endswith(".txt"):
            filename += ".txt"

        content = text.strip()
        return {
            "filename": filename,
            "content": content,
            "character_count": len(content),
            "content_preview": content[:200],
        }


transcription_service = TranscriptionService()
