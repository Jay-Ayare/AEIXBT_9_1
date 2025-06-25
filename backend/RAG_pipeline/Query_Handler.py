import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Updated LangChain imports
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

# Fixed OpenRouter ChatOpenAI import
from langchain_community.chat_models import ChatOpenAI

load_dotenv()  # Load .env variables

router = APIRouter()

# Get the absolute path to the backend directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.dirname(BASE_DIR)

# Updated embedding model
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Fixed paths for FAISS indexes
faiss_index_path = os.path.join(BACKEND_DIR, "faiss_index")
faiss_index_tvl_path = os.path.join(BACKEND_DIR, "faiss_index_tvl")

# Check if FAISS indexes exist before loading
if not os.path.exists(faiss_index_path):
    raise FileNotFoundError(f"FAISS index not found at {faiss_index_path}. Please run the chunking scripts first.")

if not os.path.exists(faiss_index_tvl_path):
    raise FileNotFoundError(f"FAISS TVL index not found at {faiss_index_tvl_path}. Please run the TVL chunking script first.")

# Load FAISS indexes for off-chain and on-chain data
faiss_index = FAISS.load_local(faiss_index_path, embeddings=embedding, allow_dangerous_deserialization=True)
faiss_index_tvl = FAISS.load_local(faiss_index_tvl_path, embeddings=embedding, allow_dangerous_deserialization=True)

# Setup OpenRouter ChatOpenAI model
llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.3,
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
)

# Prompt templates
prompt_template_offchain = """
You are a Web3 analyst summarizing public sentiment.

Use the context to provide a Sentiment Analysis based on off-chain sources (X, blogs, news, etc.)

If no sentiment data is available, say so.

Context:
{context}

Question:
{question}

Answer:
"""

prompt_template_onchain = """
You are a Web3 analyst analyzing blockchain activity.

Use the context to provide a Technical Performance report based on on-chain data (TVL, gas, governance votes, etc.)

If no relevant on-chain data is available, say so.

Context:
{context}

Question:
{question}

Answer:
"""

prompt_offchain = PromptTemplate(template=prompt_template_offchain, input_variables=["context", "question"])
prompt_onchain = PromptTemplate(template=prompt_template_onchain, input_variables=["context", "question"])

chain_offchain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt_offchain)
chain_onchain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt_onchain)


class QueryPayload(BaseModel):
    query: str


@router.post("/chat")
async def query_route(payload: QueryPayload):
    try:
        query = payload.query

        # Embed the query
        embedded_query = embedding.embed_query(query)

        # Retrieve similar docs from off-chain and on-chain indexes
        docs_offchain = faiss_index.similarity_search_by_vector(embedded_query, k=3)
        docs_onchain = faiss_index_tvl.similarity_search_by_vector(embedded_query, k=3)

        # Run QA chains
        response_off = chain_offchain.invoke({"input_documents": docs_offchain, "question": query})
        response_on = chain_onchain.invoke({"input_documents": docs_onchain, "question": query})

        # Combine output
        final_response = f"""
🔍 Sentiment Analysis (Off-chain):

{response_off['output_text'].strip()}

📊 Technical Performance (On-chain):

{response_on['output_text'].strip()}
"""

        return {"response": final_response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Exception during query processing: {str(e)}")