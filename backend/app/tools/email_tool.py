from langchain_core.tools import tool


@tool
def send_email(
    to: str,
    subject: str,
    body: str,
) -> str:
    """Send an email to a customer."""

    # Placeholder implementation
    return f"Email successfully sent to {to}."