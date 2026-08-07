"""CRUD helpers."""

from __future__ import annotations

from .models import ChatRecord


def create_chat_record(record_id: int, message: str) -> ChatRecord:
    return ChatRecord(id=record_id, message=message)
