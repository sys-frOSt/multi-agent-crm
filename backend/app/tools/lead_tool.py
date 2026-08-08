from langchain_core.tools import tool

from app.db import crud


@tool
def create_lead(
    customer_name: str,
    email: str,
    product: str,
    company: str
)->str:
    """Create a new lead in the CRM."""


    lead=crud.create_lead(
        customer_name=customer_name,
        email=email,
        product=product,
        company=company
    
    )
     return f"Lead {lead.id} created successfully."