from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings as HFHuggingFaceEmbeddings
from langchain.text_splitter import SentenceTransformersTokenTextSplitter
import json
import os

# Embedding Model (prefer new import if available)
try:
    embedder = HFHuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
except Exception as e:
    print("⚠️ Falling back to older embedding import due to:", e)
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load JSON dataset
json_path = "backend/DATA/animal_reports_expanded.json"
with open(json_path, "r") as f:
    data = json.load(f)

# Initialize chunker
splitter = SentenceTransformersTokenTextSplitter(
    model_name="all-MiniLM-L6-v2",
    chunk_size=256,
    chunk_overlap=32
)

docs = []
metadatas = []

for entry in data:
    description = entry["description"]
    era = entry["name"].split()[-1]

    chunks = splitter.split_text(description)
    
    print(f"\n📄 Entry: {entry['name']}")
    print(f"✂️  Split into {len(chunks)} chunks")
    for i, chunk in enumerate(chunks, 1):
        print(f"  Chunk {i}: {chunk[:80]}...")

    for chunk in chunks:
        docs.append(chunk)
        metadatas.append({"era": era})

# Create vectorstore and save locally
vectorstore = FAISS.from_texts(docs, embedder, metadatas=metadatas)

persist_directory = "faiss_index"
if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)

vectorstore.save_local(persist_directory)

print(f"\n✅ Loaded {len(data)} entries from the JSON file.")
print(f"✅ Created {len(docs)} chunks with metadata.")
print(f"📦 Vector store saved at: {persist_directory}")