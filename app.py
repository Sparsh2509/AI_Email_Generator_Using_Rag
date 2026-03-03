import os
from dotenv import load_dotenv
from rag.retriever import retrieve_context
from prompts.email_prompt import build_email_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
gemini_key = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7,
    api_key=gemini_key
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