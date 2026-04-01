# 📧 AI Email Copilot using RAG

An AI-powered Email Generator built using **Retrieval-Augmented Generation (RAG)**.  
By combining semantic template retrieval via Hugging Face embeddings with the reasoning power of Google Gemini, this system crafts highly personalized, context-aware professional emails tailored to any specific scenario, role, or tone.

Live UI Demo: [https://aiemailgeneratorusingrag-lfcvucjigqzpjmza3ruhhg.streamlit.app/](https://aiemailgeneratorusingrag-lfcvucjigqzpjmza3ruhhg.streamlit.app/) 

Live REST API: [https://ai-email-generator-using-rag.onrender.com](https://ai-email-generator-using-rag.onrender.com)

---

## 🚀 Features

- Generate professional emails (Cold Email, Internship Request, Follow-up, Apology, Sales Outreach)
- Context-aware generation using RAG
- Semantic template retrieval using FAISS
- HuggingFace embeddings (all-MiniLM-L6-v2)
- Gemini 2.5 Flash Lite for generation
- Interactive Streamlit UI
- Deployed on Streamlit Cloud

---

## 🏗 Architecture

User Input  
↓  
Generate Semantic Query  
↓  
HuggingFace Embeddings  
↓  
FAISS Vector Search  
↓  
Retrieve Top-K Templates  
↓  
Inject Context into Prompt  
↓  
Gemini LLM Generates Email  

---

## 🛠 Tech Stack

- Python
- Streamlit
- LangChain
- HuggingFace Embeddings
- FAISS Vector Database
- Google Gemini API
- dotenv
- FastAPI (REST API)
- Postman (API Testing)

---

## 📂 Project Structure


```
AI_Email_Generator/
│
├── streamlit_app.py            # Streamlit UI for generating emails using Gemini API
├── app.py                      # CLI-based email generation interface
│
├── rag/
│   ├── build_vectorstore.py    # Creates hugging face embeddings and builds FAISS vector index
│   ├── retriever.py            # Retrieves top relevant email templates using semantic search
│
├── prompts/
│   ├── email_prompt.py         # Builds structured prompt using user input + retrieved context to 
│                               # control and formatt LLM output
│
├── Email_Templates_idea/       # Collection of sample email templates for RAG knowledge base
│
├── faiss_index/                # Stored FAISS vector database files
├── requirements.txt            # Project dependencies
├── api.py                      # FastAPI REST endpoint to expose RAG pipeline
└── README.md                   # Project documentation
```

---

## ⚙ How It Works

1. User enters:
   - Sender name
   - Recipient name
   - Company name
   - Purpose
   - Tone
   - Key points

2. System:
   - Converts query into embeddings
   - Retrieves similar email templates from FAISS
   - Injects context into structured prompt
   - Gemini generates final email

This ensures more structured and consistent output compared to plain prompt-based generation.

---

## 📥 Sample Request

Below is an example user input provided through the UI:

```
Sender Name: Sparsh
Recipient Name: HR Manager
Company Name: ABC Technologies
Purpose: Internship Request
Tone: Professional
Length: Medium
Key Points:
- Built RAG systems
- Strong in Python
- Passionate about AI
```

---

## 📤 Sample Response

```
Subject: Application for AI Internship Opportunity

Dear HR Manager,

I hope this message finds you well.

My name is Sparsh, and I am writing to express my strong interest in internship opportunities at ABC Technologies. I have been following your innovative work in the AI space and greatly admire your commitment to building impactful technology solutions.

I have hands-on experience building Retrieval-Augmented Generation (RAG) systems and possess strong proficiency in Python. My passion for artificial intelligence drives me to continuously learn and contribute meaningfully to challenging projects.

I would welcome the opportunity to further discuss how I can contribute to your team. Thank you for your time and consideration.

Best regards,
Sparsh
```

---

## 🔌 REST API

A FastAPI layer was built to expose the RAG pipeline as a REST endpoint.

### Live API Endpoint (Render)
You can test the API directly via POST request at:
`https://ai-email-generator-using-rag.onrender.com/generate-email`

### Run API Locally
```bash
uvicorn api:app --reload
```

### Endpoint

`POST /generate-email`

### Request Body
```json
{
  "sender_name": "Sparsh Gupta",
  "recipient_name": "HR Manager",
  "company_name": "ABC Technologies",
  "purpose": "Internship Request",
  "tone": "Professional",
  "length": "Medium",
  "key_points": ["Built RAG systems", "Strong in Python", "Passionate about AI"]
}
```

### Response
```json
{
  "success": true,
  "data": {
    "email": "Subject: Internship Inquiry - AI and Python Expertise\n\nDear HR Manager,\n\nI am writing to express my enthusiastic interest in internship opportunities at ABC Technologies, particularly within roles that leverage artificial intelligence. My academic and personal projects have provided me with practical experience in developing robust RAG (Retrieval-Augmented Generation) systems, a field I find incredibly dynamic and promising. I am confident that my foundational knowledge and hands-on experience in building these sophisticated AI architectures align well with the innovative work being done at your company.\n\nMy technical proficiency is strongly rooted in Python, a language I have utilized extensively for data manipulation, algorithm implementation, and the development of complex AI applications. I am passionate about the transformative potential of AI and am eager to contribute my skills to a forward-thinking organization like ABC Technologies. I am keen to learn from experienced professionals and gain invaluable real-world exposure in a challenging and rewarding environment.\n\nThank you for considering my application. I have attached my resume for your review and welcome the opportunity to discuss how my skills and passion for AI can benefit ABC Technologies.\n\nBest regards,\nSparsh Gupta"
  }
}
```
---

## 🔎 What Makes This Response Context-Aware?

- The system retrieves similar internship email templates from the FAISS vector database.
- Relevant tone and structure are injected into the prompt.
- Gemini 2.5 Flash Lite generates the final structured email.

---

## 🧪 Run Locally

### Clone Repository

```bash
git clone https://github.com/Sparsh2509/AI_Email_Generator_Using_Rag.git
cd AI_Email_Generator_Using_Rag
```

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root of project and add API keys. We use the Hugging Face Serverless Inference API to handle embeddings with zero local memory cost.

```env
GEMINI_API_KEY="google_gemini_token"
HF_TOKEN="huggingface_token"
```
> **Important:**Hugging Face token must have the **"Make calls to the serverless Inference API"** permission enabled.


### Run Streamlit App

```bash
streamlit run streamlit_app.py
```




