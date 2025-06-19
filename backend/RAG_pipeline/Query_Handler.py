# backend/RAG_pipeline/Query_Handler.py

import os
from fastapi import APIRouter
from pydantic import BaseModel

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings as HFHuggingFaceEmbeddings

# Calculate absolute path to faiss_index relative to this file
persist_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../faiss_index"))
print(f"📂 Trying to load vectorstore from: {persist_directory}")

# Load embedding model (try new import first)
try:
    embedder = HFHuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
except Exception:
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load vectorstore from the persistent directory
vectorstore = FAISS.load_local(persist_directory, embedder, allow_dangerous_deserialization=True)

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/chat")
async def chat_handler(request: QueryRequest):
    query = request.query.strip()
    if not query:
        return {"answer": "⚠️ Query cannot be empty."}

    try:
        # Perform similarity search, return top 1 chunk
        results = vectorstore.similarity_search(query, k=1)
        top_chunk = results[0].page_content if results else "No relevant chunk found."
        return {"answer": top_chunk}
    except Exception as e:
        print("❌ Error:", e)
        return {"answer": f"⚠️ Internal error: {str(e)}"}
