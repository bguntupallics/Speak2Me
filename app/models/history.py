from datetime import datetime
from typing import Any

from pydantic import BaseModel


class CommandHistoryEntry(BaseModel):
    id: str
    user_id: str
    command_type: str
    input_data: dict[str, Any]
    output_data: dict[str, Any]
    created_at: datetime


class CommandHistoryResponse(BaseModel):
    entries: list[CommandHistoryEntry]
    total_count: int
