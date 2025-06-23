from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings as HFHuggingFaceEmbeddings
from langchain.text_splitter import SentenceTransformersTokenTextSplitter
import json
import os

# Embedding model
try:
    embedder = HFHuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
except Exception as e:
    print("⚠️ Falling back to older embedding import due to:", e)
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load JSON dataset
json_path = "backend/DATA/daos_info.json"
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

# Handle 'web3_data'
for entry in data.get("web3_data", []):
    text = f"""
    Project: {entry['project']} ({entry['type']})
    Token: {entry['token']}
    Latest Update: {entry['latest_update']}
    
    Governance: {entry['updates'].get('governance', '')}
    Technical: {entry['updates'].get('technical', '')}
    Financial: {entry['updates'].get('financial', '')}
    Sustainability: {entry['updates'].get('sustainability', '')}
    
    Market Cap: {entry['metrics'].get('market_cap', 'N/A')}
    Token Price: {entry['metrics'].get('token_price', 'N/A')}
    Circulating Supply: {entry['metrics'].get('circulating_supply', 'N/A')}
    Governance Participation: {entry['metrics'].get('governance_participation', 'N/A')}
    """
    chunks = splitter.split_text(text.strip())

    print(f"\n📄 Project: {entry['project']}")
    print(f"✂️  Split into {len(chunks)} chunks")
    for i, chunk in enumerate(chunks, 1):
        print(f"  Chunk {i}: {chunk[:80]}...")

    for chunk in chunks:
        docs.append(chunk)
        metadatas.append({"project": entry["project"], "type": entry["type"]})

# Handle 'market_analytics' if present
analytics = data.get("market_analytics", {})
if analytics:
    summary = f"""
    Total TVL: {analytics.get('total_value_locked')}
    Stablecoin Market Cap: {analytics.get('stablecoin_market_cap')}

    Governance Trends:
    - Average Voter Turnout: {analytics.get('governance_trends', {}).get('average_voter_turnout')}
    - Proposal Success Rate: {analytics.get('governance_trends', {}).get('proposal_success_rate')}

    Sustainability Metrics:
    - Projects with Eco Initiatives: {analytics.get('sustainability_metrics', {}).get('projects_with_eco_initiatives')}
    - Carbon Offset Investments: {analytics.get('sustainability_metrics', {}).get('carbon_offset_investments')}
    """
    chunks = splitter.split_text(summary.strip())

    print(f"\n📊 Market Analytics")
    print(f"✂️  Split into {len(chunks)} chunks")
    for i, chunk in enumerate(chunks, 1):
        print(f"  Chunk {i}: {chunk[:80]}...")

    for chunk in chunks:
        docs.append(chunk)
        metadatas.append({"project": "Market Analytics", "type": "Macro"})

# Save vectorstore
vectorstore = FAISS.from_texts(docs, embedder, metadatas=metadatas)

persist_directory = "faiss_index"
if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)

vectorstore.save_local(persist_directory)

print(f"\n✅ Loaded {len(data['web3_data'])} Web3 project entries.")
print(f"✅ Created {len(docs)} total chunks with metadata.")
print(f"📦 Vector store saved at: {persist_directory}")
