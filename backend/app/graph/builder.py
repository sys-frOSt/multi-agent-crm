"""Build a lightweight in-process graph for the backend."""

from __future__ import annotations

from dataclasses import dataclass, field

from .nodes import register_nodes
from .router import route_state
from .state import GraphState


@dataclass
class SimpleGraph:
    nodes: dict[str, callable] = field(default_factory=register_nodes)

    def run(self, state: GraphState) -> str:
        node_name = route_state(state)
        node = self.nodes.get(node_name, self.nodes["planner"])
        return node(state)


def build_graph() -> SimpleGraph:
    """Create the default graph instance."""

    return SimpleGraph()
