from fastapi import APIRouter, HTTPException

from app.models.translation import TranslateRequest, TranslateResponse
from app.services.translation_service import translation_service

router = APIRouter()


@router.post("/translate", response_model=TranslateResponse)
async def translate_text(request: TranslateRequest):
    try:
        translated = await translation_service.translate(
            text=request.text,
            target=request.target_language,
            source=request.source_language,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Translation service error: {e}")

    return TranslateResponse(
        original_text=request.text,
        translated_text=translated,
        source_language=request.source_language,
        target_language=request.target_language,
    )
