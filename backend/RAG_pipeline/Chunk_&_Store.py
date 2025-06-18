from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import json

# Load JSON
with open("backend/DATA/animal_reports.json", "r") as f:
    data = json.load(f)

# Embedding Model
embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Chunking
splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=256, chunk_overlap=0)  # ~2 sentences

docs = []
metadatas = []

for entry in data:
    description = entry["description"]
    era = entry["name"].split()[-1]  # example: "report from 2024" → "2024"
    
    chunks = splitter.split_text(description)
    
    for chunk in chunks:
        docs.append(chunk)
        metadatas.append({"era": era})

# Store in FAISS
vectorstore = FAISS.from_texts(docs, embedder, metadatas=metadatas)

# Save for future use
vectorstore.save_local("faiss_index")

print(f"✅ Loaded {len(data)} entries from the JSON file.")
print(f"✅ Created {len(docs)} chunks with metadata.")
print(f"📦 Vector store saved at: faiss_index")
