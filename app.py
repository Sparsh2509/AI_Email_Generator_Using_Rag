from rag.retrieval_test import retrieve_context
from prompts.email_prompt import build_email_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7
)

# Example input
sender = "Sparsh"
recipient = "HR Manager"
company = "AI Startup"
purpose = "internship request"
tone = "professional"
key_points = "- Built RAG systems\n- Strong in Python\n- Passionate about AI"
length = "medium"

# 🔥 Important — Make smarter retrieval query
query = f"{purpose} {tone} email"

context = retrieve_context(query)

prompt = build_email_prompt(
    sender,
    recipient,
    company,
    purpose,
    tone,
    key_points,
    length,
    context
)

response = llm.invoke(prompt)

print(response.content)