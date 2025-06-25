# backend/RAG_pipeline/Chunk_&_Store_tvl.py

import os
import json
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import SentenceTransformersTokenTextSplitter
from langchain_community.vectorstores import FAISS

# Load cleaned TVL dataset
json_path = "backend/DATA/tvl_data.json"
with open(json_path, "r") as f:
    records = json.load(f)

# Embedding model
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
save_path = "faiss_index_tvl"
if not os.path.exists(save_path):
    os.makedirs(save_path)

vectorstore = FAISS.from_texts(docs, embedder, metadatas=metadatas)
vectorstore.save_local(save_path)

print(f"\n✅ Embedded {len(records)} entries into {len(docs)} chunks.")
print(f"📦 Vector store saved at: {save_path}")
