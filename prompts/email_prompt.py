def build_email_prompt(
    sender_name,
    recipient_name,
    company_name,
    purpose,
    tone,
    key_points,
    length,
    context=""
):
    return f"""
You are an expert professional email writer.

Reference Examples:
{context}

Write a {tone} {purpose} email.

Sender: {sender_name}
Recipient: {recipient_name}
Company: {company_name}

Key Points:
{key_points}

Keep it {length}.
Generate:
1. 3 subject lines ranked by engagement.
2. Email body.
"""