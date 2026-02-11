🧠 RAG AI Assistant (Recruiter-Based Knowledge System)

A Retrieval-Augmented Generation (RAG) powered AI assistant that provides accurate, context-aware answers from custom documents using vector search and local LLM inference.

Built for interview preparation, recruiter systems, technical knowledge bases, and enterprise documentation Q&A.

🚀 Features:

🔍 Semantic Search using FAISS vector database

🧠 RAG Pipeline (Retrieval + LLM Generation)

🤖 Local LLM Inference using Ollama (tinyllama)

📄 PDF / Document Ingestion

🧬 HuggingFace Embeddings (all-MiniLM-L6-v2)

⚡ FastAPI Backend

🧱 Modular architecture

📚 Source-based answers with references

🔐 No hallucination policy (context-only answering)

🏠 Fully local system (no cloud dependency)

📡 API-based architecture (production-ready)

🎯 Problem Statement:

Recruiters, students, and professionals face problems like:

Scattered learning resources

Time wasted searching PDFs and notes

Inaccurate AI answers (hallucinations)

No context-based responses

Lack of personalized knowledge systems

💡 Reason Behind Building This System

To create:

A trusted AI assistant

That answers only from verified documents

Provides source-backed answers

Works offline

Is recruiter-friendly

Is interview-prep focused

Is enterprise scalable

🧩 Solution:

This project uses:

RAG (Retrieval-Augmented Generation)

Meaning:

User asks a question

System searches vector database

Retrieves relevant document chunks

Builds context

LLM answers only from that context

Returns answer + sources

✅ No hallucination
✅ No fake answers
✅ No guessing
✅ No external knowledge injection

🧱 System Architecture:
User Query
   ↓
FastAPI API
   ↓
FAISS Vector Search
   ↓
Relevant Docs Retrieved
   ↓
Context Builder
   ↓
RAG Prompt
   ↓
Local LLM (TinyLlama via Ollama)
   ↓
Answer + Sources

🛠️ Tech Stack:

Python

FastAPI

LangChain

FAISS

Ollama

TinyLlama

HuggingFace Transformers

SentenceTransformers

Vector Embeddings

🌍 Real-World Applications:

🎓 Interview Preparation System

🧑‍💼 Recruiter Knowledge Assistant

🏢 Enterprise Knowledge Base

📚 Document Q&A System

🧠 AI Study Assistant

🧾 Compliance Document Search

📑 Legal/Medical Document Search

🏫 Academic Assistant

📊 Research Assistant

🧑‍🏫 Training System

🧪 API Example:

POST /ask
{
  "question": "What is Python GIL?"
}
Response:
{
  "answer": "...",
  "sources": [
    {
      "source": "data/docs/python_interview_notes.pdf",
      "page": 6
    }
  ]
}

📁 Project Structure:

Rag_AI_Assistant/
│
├── app/
│   ├── main.py
│   ├── rag.py
│   ├── prompts.py
│
├── data/
│   ├── docs/
│
├── models/          # ignored in git
├── vector_store/    # ignored in git
│
├── test_rag.py
├── README.md
├── requirements.txt
├── .gitignore

⚙️ Setup Instructions:

pip install -r requirements.txt
ollama pull tinyllama
uvicorn app.main:app --reload

PDF Parsing

RAG Architecture
