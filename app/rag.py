from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from app.prompts import RAG_PROMPT

# =========================
# CONFIG
# =========================
VECTOR_DB_PATH = "data/vector_store"   # ✅ single source of truth

# =========================
# EMBEDDINGS
# =========================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =========================
# LLM
# =========================
llm = OllamaLLM(
    model="tinyllama",
    temperature=0.2
)

# =========================
# LOAD VECTOR STORE (ONCE)
# =========================
db = FAISS.load_local(
    VECTOR_DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

# =========================
# RAG FUNCTION
# =========================
def ask_rag(question: str, doc_type: str = "python"):

    # Search
    results = db.similarity_search(question, k=6)

    # -----------------------------
    # FIX 2: HARD FILTER BY DOC TYPE
    # -----------------------------
    filtered_docs = []
    for doc in results:
        src = doc.metadata.get("source", "").lower()

        if doc_type == "python" and "python" in src:
            filtered_docs.append(doc)

        elif doc_type == "aws" and "aws" in src:
            filtered_docs.append(doc)

    # Fallback if filter removes everything
    if not filtered_docs:
        filtered_docs = results

    # =========================
    # BUILD CONTEXT
    # =========================
    context = "\n\n".join([doc.page_content for doc in filtered_docs])

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    # =========================
    # LLM CALL
    # =========================
    response = llm.invoke(prompt)

    # =========================
    # RESPONSE FORMAT
    # =========================
    return {
        "answer": response,
        "sources": [
            {
                "source": doc.metadata.get("source"),
                "page": doc.metadata.get("page")
            }
            for doc in filtered_docs
        ]
    }