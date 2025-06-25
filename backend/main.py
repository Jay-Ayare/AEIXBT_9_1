import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from RAG_pipeline.Query_Handler import router as query_router

load_dotenv()  # Load environment variables from .env file

app = FastAPI(title="AEIXBT RAG API")

# Enable CORS for local dev or your frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to AEIXBT RAG backend"}
