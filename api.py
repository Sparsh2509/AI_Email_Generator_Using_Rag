from fastapi import FastAPI
from pydantic import BaseModel
from rag.retriever import retrieve_templates       
from prompts.email_prompt import build_prompt       
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# Request schema
class EmailRequest(BaseModel):
    sender_name: str
    recipient_name: str
    company_name: str
    purpose: str
    tone: str
    length: str
    key_points: str

@app.get("/")
def root():
    return {"message": "AI Email Generator API is running"}

@app.post("/generate-email")
def generate_email(request: EmailRequest):
    templates = retrieve_templates(request.purpose)

    
    prompt = build_prompt(
        sender_name=request.sender_name,
        recipient_name=request.recipient_name,
        company_name=request.company_name,
        purpose=request.purpose,
        tone=request.tone,
        length=request.length,
        key_points=request.key_points,
        context=templates
    )

    response = model.generate_content(prompt)

    return {"email": response.text}
