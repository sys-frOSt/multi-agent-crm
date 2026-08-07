"""Graph node registration."""

from __future__ import annotations

from collections.abc import Callable

from ..agents.crm import handle_crm_task
from ..agents.email import handle_email_task
from ..agents.lead import handle_lead_task
from ..agents.planner import handle_planner_task
from .state import GraphState


def register_nodes() -> dict[str, Callable[[GraphState], str]]:
    """Return the callable node registry used by the graph builder."""

    return {
        "planner": handle_planner_task,
        "crm": handle_crm_task,
        "lead": handle_lead_task,
        "email": handle_email_task,
    }
