from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import ask_rag

app = FastAPI(title="RAG AI Assistant")

class Query(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "RAG AI Assistant is running"}

@app.post("/ask")
def ask(query: Query):
    return ask_rag(query.question)
