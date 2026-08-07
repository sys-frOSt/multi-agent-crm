"""Chat API entry points."""

from __future__ import annotations

from ..graph.builder import build_graph
from ..graph.state import GraphState


def chat(message: str) -> str:
    state = GraphState(messages=[message])
    return build_graph().run(state)
