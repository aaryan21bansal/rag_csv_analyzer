import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "rag_csv_db")

VECTOR_DB = os.getenv("VECTOR_DB", "faiss") 

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "huggingface")  
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
