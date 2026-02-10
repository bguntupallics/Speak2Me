from typing import Any

from supabase import Client


class HistoryService:
    def __init__(self):
        self.client: Client | None = None

    def init_client(self, client: Client):
        """Share the Supabase client from auth_service."""
        self.client = client

    async def log_command(
        self,
        user_id: str,
        command_type: str,
        input_data: dict[str, Any],
        output_data: dict[str, Any],
    ):
        self.client.table("command_history").insert({
            "user_id": user_id,
            "command_type": command_type,
            "input_data": input_data,
            "output_data": output_data,
        }).execute()

    async def get_history(
        self,
        user_id: str,
        limit: int = 20,
        offset: int = 0,
        command_type: str | None = None,
    ):
        query = (
            self.client.table("command_history")
            .select("*", count="exact")
            .eq("user_id", user_id)
            .order("created_at", desc=True)
            .range(offset, offset + limit - 1)
        )
        if command_type:
            query = query.eq("command_type", command_type)
        return query.execute()

    async def get_entry(self, user_id: str, entry_id: str):
        result = (
            self.client.table("command_history")
            .select("*")
            .eq("id", entry_id)
            .eq("user_id", user_id)
            .single()
            .execute()
        )
        return result.data


history_service = HistoryService()
