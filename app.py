import os
from dotenv import load_dotenv
from rag.retriever import retrieve_context
from prompts.email_prompt import build_email_prompt
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Load Gemini API Key
gemini_key = os.getenv("GEMINI_API_KEY")

if not gemini_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7,
    api_key=gemini_key
)



print("\n===== AI Email Copilot (RAG Powered) =====\n")

sender = input("Enter sender name: ")
recipient = input("Enter recipient name: ")
company = input("Enter company name: ")
purpose = input("Enter purpose (e.g., internship request / cold email / follow up): ")
tone = input("Enter tone (professional / friendly / persuasive): ")
length = input("Enter length (short / medium / long): ")

print("\nEnter key points (type 'done' when finished):")

points = []
while True:
    line = input()
    if line.lower() == "done":
        break
    points.append("- " + line)

key_points = "\n".join(points)



query = f"{purpose} {tone} email template"
context = retrieve_context(query)


print("\n----- RETRIEVED CONTEXT FROM FAISS -----\n")
print(context)
print("\n-------------------------------------------\n")



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

print("\n===== GENERATED EMAIL =====\n")
print(response.content)
print("\n================================\n")