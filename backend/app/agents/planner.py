"""Planner agent."""

from __future__ import annotations

from ..graph.state import GraphState


def handle_planner_task(state: GraphState) -> str:
    return f"planner: {state.messages[-1] if state.messages else 'ready'}"
