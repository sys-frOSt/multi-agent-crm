"""CRM agent."""

from __future__ import annotations

from ..graph.state import GraphState


def handle_crm_task(state: GraphState) -> str:
    return f"crm: {state.messages[-1] if state.messages else 'ready'}"
