ALLOWED_CONTENT_TYPES = {
    "audio/wav", "audio/x-wav", "audio/wave",
    "audio/mpeg", "audio/mp3",
    "audio/mp4", "audio/x-m4a",
    "audio/flac", "audio/x-flac",
    "audio/ogg", "audio/vorbis",
    "audio/webm",
}

ALLOWED_EXTENSIONS = {".wav", ".mp3", ".m4a", ".flac", ".ogg", ".webm"}

MAX_FILE_SIZE = 25 * 1024 * 1024  # 25 MB


def validate_audio_file(content_type: str | None, filename: str | None, size: int) -> str | None:
    """Returns an error message if invalid, or None if valid."""
    if size > MAX_FILE_SIZE:
        return f"File too large ({size / 1024 / 1024:.1f}MB). Max is 25MB."

    if filename:
        ext = "." + filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
        if ext and ext not in ALLOWED_EXTENSIONS:
            return f"Unsupported file extension: {ext}. Supported: {ALLOWED_EXTENSIONS}"

    return None
