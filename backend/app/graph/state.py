from __future__ import annotations
from langchain_core.messages import AnyMessage

import os
from typing import TypedDict , Annotated,Any
import operator



class CRMState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    #user
    user_query:str

    #customer
    customer_name:str | None
    email: str| None
    product: str | None
    company: str | None

    intent: str | None
    plan: list[str]
    current_agent: str | None

    lead_created: bool
    lead_id: str | None
    email_sent: bool

    response: str