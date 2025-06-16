# backend/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def ask_question(request: Request):
    data = await request.json()
    query = data.get("query")
    print(f"Received query: {query}", flush=True)
    return {"answer": f"You asked: {query}"}


