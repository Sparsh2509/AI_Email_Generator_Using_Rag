from fastapi import FastAPI
from pydantic import BaseModel
from rag.retriever import retrieve_context       
from prompts.email_prompt import build_email_prompt       
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    "gemini-2.5-flash-lite",
    generation_config={"temperature": 0.7}  
)

class EmailRequest(BaseModel):
    sender_name: str
    recipient_name: str
    company_name: str
    purpose: str
    tone: str
    length: str
    key_points: list[str]

@app.get("/")
def root():
    return {"message": "AI Email Generator API is running"}

@app.post("/generate-email")
def generate_email(request: EmailRequest):
    try:
        templates = retrieve_context(request.purpose)
        key_points_str = "\n".join(f"- {point}" for point in request.key_points)

        prompt = build_email_prompt(
            sender_name=request.sender_name,
            recipient_name=request.recipient_name,
            company_name=request.company_name,
            purpose=request.purpose,
            tone=request.tone,
            length=request.length,
            key_points=key_points_str,
            context=templates
        )

        response = model.generate_content(prompt)

        return {
            "success": True,
            "data": {
                "email": response.text
            },
        }

    except Exception as e:
        return {
            "success": False,
            "data": None,
            "error": str(e)
        }