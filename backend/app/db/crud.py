import uuid

def create_lead(
        customer_name: str,
        email: str,
        product: str,
        company: str

):

    lead_id=f"LEAD-{uuid.uuid4().hex[:8].upper()}"
    