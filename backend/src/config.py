import os
from dotenv import load_dotenv
import streamlit as st 

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
NEO4J_URI = st.secrets["NEO4J_URI"]
NEO4J_USERNAME = st.secrets["NEO4J_USERNAME"]
NEO4J_PASSWORD = st.secrets["NEO4J_PASSWORD"]

LOCAL_LLM = "llama3.1"
GPT4_MODEL = "gpt-4o-mini"
MILVUS_URI = "./milvus/milvus_example.db"

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY
os.environ["NEO4J_URI"] = NEO4J_URI
os.environ["NEO4J_USERNAME"] = NEO4J_USERNAME
os.environ["NEO4J_PASSWORD"] = NEO4J_PASSWORD

