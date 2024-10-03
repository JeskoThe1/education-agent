from langchain_openai import ChatOpenAI
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config

class LLMInterface:
    def __init__(self, model_name=config.GPT4o):
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=0.2,
            openai_api_key=config.OPENAI_API_KEY
        )

    def get_llm(self):
        return self.llm

    def generate_response(self, prompt):
        return self.llm.predict(prompt)