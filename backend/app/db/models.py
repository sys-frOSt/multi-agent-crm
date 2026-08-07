"""Database models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ChatRecord:
    id: int
    message: str
