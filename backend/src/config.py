import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # OpenAI API
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # LLM Models
    GPT4o = "gpt-4o-mini"
    GPTo1 = "o1-preview"
    GPT3_5 = "gpt-3.5-turbo-0125"
    
    # Vector Store
    CHROMA_PERSIST_DIRECTORY = "./chroma_db"
    
    # Data
    RAW_DATA_DIR = "./data/raw"
    PROCESSED_DATA_DIR = "./data/processed"
    
    # PDF Processing
    PDF_DIR = "./data/pdf"

config = Config()