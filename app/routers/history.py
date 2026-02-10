from fastapi import APIRouter, Depends, HTTPException, Query

from app.dependencies import get_current_user
from app.models.history import CommandHistoryEntry, CommandHistoryResponse
from app.services.history_service import history_service

router = APIRouter()


@router.get("/", response_model=CommandHistoryResponse)
async def get_history(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    command_type: str | None = Query(default=None),
    current_user=Depends(get_current_user),
):
    result = await history_service.get_history(
        user_id=str(current_user.id),
        limit=limit,
        offset=offset,
        command_type=command_type,
    )
    entries = [CommandHistoryEntry(**entry) for entry in result.data]
    return CommandHistoryResponse(
        entries=entries,
        total_count=result.count or len(entries),
    )


@router.get("/{entry_id}", response_model=CommandHistoryEntry)
async def get_history_entry(
    entry_id: str,
    current_user=Depends(get_current_user),
):
    entry = await history_service.get_entry(
        user_id=str(current_user.id),
        entry_id=entry_id,
    )
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return CommandHistoryEntry(**entry)
