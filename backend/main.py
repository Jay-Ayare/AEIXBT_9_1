# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from RAG_pipeline.Query_Handler import router as query_router

app = FastAPI()

# Allow frontend at localhost:3000 to access this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(query_router)
