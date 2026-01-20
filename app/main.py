from fastapi import FastAPI
from pydantic import BaseModel
from openai import AzureOpenAI
import os

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Azure AI Chatbot is running! Visit /docs to see API endpoints."}

# Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Request model
class ChatRequest(BaseModel):
    message: str

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}

# Chat endpoint
@app.post("/chat")
def chat(req: ChatRequest):
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {"role": "system", "content": "You are a helpful cloud assistant."},
            {"role": "user", "content": req.message}
        ]
    )
    return {"reply": response.choices[0].message.content}

