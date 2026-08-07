"""Email agent."""

from __future__ import annotations

from ..graph.state import GraphState


def handle_email_task(state: GraphState) -> str:
    return f"email: {state.messages[-1] if state.messages else 'ready'}"
