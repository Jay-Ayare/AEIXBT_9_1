import os
import requests
from dotenv import load_dotenv
from fastapi import APIRouter
from pydantic import BaseModel

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings as HFHuggingFaceEmbeddings

# Load environment variables from .env
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
print("🔐 API key prefix:", OPENROUTER_API_KEY[:10] if OPENROUTER_API_KEY else "None found")

if not OPENROUTER_API_KEY:
    raise ValueError("⚠️ OPENROUTER_API_KEY not found in .env file")

# Load FAISS vectorstore
persist_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../faiss_index"))
print(f"📂 Trying to load vectorstore from: {persist_directory}")

try:
    embedder = HFHuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
except Exception:
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

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
        # 🔍 Retrieve top-K chunks
        K = 4
        results = vectorstore.similarity_search(query, k=K)

        if not results:
            return {"answer": "No relevant information found."}

        combined_context = "\n\n".join([r.page_content for r in results])

        # 📜 Prompt tailored to environmental data
        prompt = f"""You are an expert at receiving data, analysing it thoroughly, and giving detailed responses, based only on the context fed to you.

        Use the context below — which contains excerpts from wildlife and environmental field reports — 
        to answer the user's question as informatively as possible. Reference facts from the context only, and do not make up data.

Context:
{combined_context}

Question: {query}
Answer:"""

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }

        body = {
            "model": "deepseek/deepseek-r1-0528:free",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

        # Debugging output
        print("🧾 Status Code:", response.status_code)
        print("🧾 Raw Response:", response.text)

        result = response.json()
        choices = result.get("choices")

        if not choices:
            return {"answer": "⚠️ No valid response from DeepSeek:\n" + response.text}

        answer = choices[0]["message"]["content"].strip()
        return {"answer": answer}

    except Exception as e:
        print("❌ Error:", e)
        return {"answer": f"⚠️ Internal error: {str(e)}"}
