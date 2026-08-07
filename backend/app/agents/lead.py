"""Lead scoring agent."""

from __future__ import annotations

from ..graph.state import GraphState


def handle_lead_task(state: GraphState) -> str:
    return f"lead: {state.messages[-1] if state.messages else 'ready'}"
