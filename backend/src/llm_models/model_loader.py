from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI
from ..config import LOCAL_LLM, GPT4_MODEL, OPENAI_API_KEY

def get_local_llm():
    return ChatOllama(model=LOCAL_LLM, temperature=0)

def get_openai_llm():
    return ChatOpenAI(model=GPT4_MODEL, temperature=0, openai_api_key=OPENAI_API_KEY)