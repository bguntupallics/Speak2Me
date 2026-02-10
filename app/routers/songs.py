from fastapi import APIRouter, HTTPException

from app.models.song import SongSearchRequest, SongSearchResponse
from app.services.song_service import song_service

router = APIRouter()


@router.post("/search", response_model=SongSearchResponse)
async def search_songs(request: SongSearchRequest):
    try:
        results = await song_service.search(
            query=request.query,
            limit=request.limit,
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Spotify service error: {e}")

    return SongSearchResponse(
        query=request.query,
        results=results,
    )
