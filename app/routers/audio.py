from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.models.audio import AudioTranscriptionResponse
from app.services.whisper_service import whisper_service
from app.utils.audio import validate_audio_file

router = APIRouter()


@router.post("/transcribe", response_model=AudioTranscriptionResponse)
async def transcribe_audio(file: UploadFile = File(...)):
    contents = await file.read()

    error = validate_audio_file(file.content_type, file.filename, len(contents))
    if error:
        raise HTTPException(status_code=400, detail=error)

    extension = Path(file.filename).suffix if file.filename else ".wav"
    result = await whisper_service.transcribe(contents, extension)

    return AudioTranscriptionResponse(**result)
