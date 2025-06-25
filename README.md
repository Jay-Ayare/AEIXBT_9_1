
# 🛰️ AEIXBT: Web3 Sustainability Intelligence

**AEIXBT** is a dual-layer RAG (Retrieval-Augmented Generation) system that evaluates the **sustainability** of Web3 tokens and DAOs by analyzing both **on-chain** and **off-chain** data.

Built with ❤️ by [@Jay-Ayare](https://github.com/Jay-Ayare)

---

## 🚀 MVP_1: Dual Source Sustainability Reports

AEIXBT provides **split-screen intelligence** on any Web3 token:
- 🧠 **Sentiment Analysis** from blogs, social platforms, and public media (**off-chain**)
- 🧮 **Technical Performance** based on TVL, chain activity, and protocol data (**on-chain**)

### 🧪 Example Output
```

🔍 Sentiment Analysis (Off-chain):
Public outlook on Uniswap remains positive due to its latest v4 upgrade.
Community engagement is rising, especially after governance proposals.

📊 Technical Performance (On-chain):
TVL has stabilized around \$4.2B.
Governance votes show strong community support for LP reward adjustments.

```

---

## 🛠️ Tech Stack

| Layer        | Tech                         |
|--------------|------------------------------|
| Frontend     | React + TailwindCSS          |
| Backend      | FastAPI                      |
| Vector Store | FAISS                        |
| LLMs         | OpenRouter (`gpt-4o-mini`)   |
| Embeddings   | HuggingFace: `MiniLM-L6-v2`  |
| Preprocessing| SentenceTransformers         |

---

## 📁 Project Structure

```

AEIXBT\_9\_1/
├── backend/
│   ├── main.py
│   ├── .env                         # \[User-defined OpenRouter API key]
│   ├── RAG\_pipeline/
│   │   ├── Query\_Handler.py         # Combines on-chain + off-chain results
│   │   ├── Chunk\_&*Store.py         # For off-chain data (future: X scraping)
│   │   ├── Chunk*&\_Store\_tvl.py     # For on-chain TVL data
│   │   ├── fetch\_tvl\_data.py        # Grabs TVL from public API
│   ├── DATA/
│   │   └── tvl\_data.json            # On-chain TVL data
│   ├── faiss\_index/                 # Off-chain vector DB
│   └── faiss\_index\_tvl/            # On-chain vector DB
│
├── frontend/
│   └── src/
│       └── App.js                   # Minimal terminal-style UI
│
└── README.md

````

---

## ⚙️ Setup Instructions

### 🔐 Prerequisites
- Python 3.8+
- Node.js + npm
- API key from [OpenRouter](https://openrouter.ai)

### 🧩 Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

**.env file** in `backend/`:

```
OPENROUTER_API_KEY=sk-or-your-key-here
```

Run preprocessing:

```bash
python RAG_pipeline/fetch_tvl_data.py
python RAG_pipeline/Chunk_&_Store_tvl.py
# (Add Chunk_&_Store.py later for off-chain vector store)
```

Run the FastAPI server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

### 💻 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Make sure the `POST` request in `App.js` targets:

```js
http://localhost:8000/api/chat
```

---

## ✨ Features

* [x] Dual source vector search (on-chain + off-chain)
* [x] Live OpenRouter-based RAG querying
* [x] Terminal-style React UI
* [x] Token sentiment + TVL performance explained
* [ ] 🔜 X (Twitter) scraping + preprocessing
* [ ] 🔜 DAO vote stats, treasury inflow/outflow
* [ ] 🔜 Company leaderboard with sustainability scores

---

## 👥 Contributing

Pull requests and forks welcome!

### Suggestions?

Open an [issue](https://github.com/Jay-Ayare/AEIXBT_9_1/issues) or start a discussion.

---

## 📜 License

MIT License © 2025 Jay Ayare
This project uses OpenRouter for AI access and public APIs for DeFi analytics.

---

> *AEIXBT is your lens into the future of sustainable Web3 — powered by intelligence, not hype.*

```

---

Let me know if you want:
- A visual banner/logo for GitHub
- A walkthrough video script
- A one-liner for LinkedIn launch
- SEO-optimized site content (for eventual deployment)
```
