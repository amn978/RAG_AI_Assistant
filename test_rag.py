from app.rag import ask_rag

print("Testing RAG...")

res = ask_rag("What is Python GIL?", doc_type="python")

print("\n=== ANSWER ===")
print(res["answer"])

print("\n=== SOURCES ===")
for s in res["sources"]:
    print(s)