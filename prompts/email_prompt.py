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
You are a professional email writer.

Use the reference examples below only for tone and structure.
Do NOT explain anything.
Do NOT add extra headings.
Return ONLY the final email.

Reference Examples:
{context}

Write a {tone} {purpose} email.

Sender: {sender_name}
Recipient: {recipient_name}
Company: {company_name}

Key Points:
{key_points}

Length: {length}

Output format:
Subject: <brief and professional subject line related to {purpose}, do NOT include sender name>
Dear {recipient_name},

<email body>

Best regards,
{sender_name}
"""