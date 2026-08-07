"""Shared graph state for the multi-agent backend."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class GraphState:
    """Minimal state container passed between graph nodes."""

    messages: list[str] = field(default_factory=list)
    current_agent: str = "planner"
    context: dict[str, Any] = field(default_factory=dict)
