"""Routing logic for deciding which agent should handle a request."""

from __future__ import annotations

from .state import GraphState


def route_state(state: GraphState) -> str:
    """Choose the next agent based on the latest user message."""

    if not state.messages:
        return "planner"

    message = state.messages[-1].lower()
    if any(keyword in message for keyword in ("email", "send", "follow up")):
        return "email"
    if any(keyword in message for keyword in ("lead", "score", "qualify")):
        return "lead"
    if any(keyword in message for keyword in ("crm", "customer", "account")):
        return "crm"
    return "planner"
