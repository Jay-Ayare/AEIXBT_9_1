import os
import json
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import SentenceTransformersTokenTextSplitter
from langchain_community.vectorstores import FAISS

# Get the absolute path to the backend directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.dirname(BASE_DIR)

# Load cleaned TVL dataset
json_path = os.path.join(BACKEND_DIR, "DATA", "tvl_data.json")

if not os.path.exists(json_path):
    print(f"❌ TVL data file not found at {json_path}")
    print("Please run fetch_tvl_data.py first to generate the data.")
    exit(1)

with open(json_path, "r") as f:
    records = json.load(f)

# Updated embedding model
embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Chunking logic
splitter = SentenceTransformersTokenTextSplitter(
    model_name="all-MiniLM-L6-v2",
    chunk_size=256,
    chunk_overlap=32
)

docs = []
metadatas = []

for entry in records:
    context = (
        f"Project: {entry['project']}\n"
        f"Symbol: {entry['symbol']}\n"
        f"Category: {entry['category']}\n"
        f"Chain: {entry['chain']}\n"
        f"TVL: {entry['tvl']}\n"
        f"Description: {entry['description']}\n"
        f"Last Updated: {entry['last_updated']}"
    )

    chunks = splitter.split_text(context)

    print(f"\n📄 Project: {entry['project']}")
    print(f"✂️  Split into {len(chunks)} chunks")

    for chunk in chunks:
        docs.append(chunk)
        metadatas.append({"project": entry["project"], "category": entry["category"]})

# Save vector store
save_path = os.path.join(BACKEND_DIR, "faiss_index_tvl")
if not os.path.exists(save_path):
    os.makedirs(save_path)

vectorstore = FAISS.from_texts(docs, embedder, metadatas=metadatas)
vectorstore.save_local(save_path)

print(f"\n✅ Embedded {len(records)} entries into {len(docs)} chunks.")
print(f"📦 Vector store saved at: {save_path}") 