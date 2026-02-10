from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.transcription import TranscribeRequest
from app.services.transcription_service import transcription_service

router = APIRouter()


@router.post("/generate")
async def generate_transcription(request: TranscribeRequest):
    result = transcription_service.generate(
        text=request.text,
        filename=request.filename,
    )

    return StreamingResponse(
        iter([result["content"]]),
        media_type="text/plain",
        headers={
            "Content-Disposition": f'attachment; filename="{result["filename"]}"'
        },
    )
