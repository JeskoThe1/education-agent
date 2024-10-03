from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config


class VectorStore:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = Chroma(
            persist_directory=config.CHROMA_PERSIST_DIRECTORY,
            embedding_function=self.embeddings
        )

    def add_texts(self, texts):
        self.vectorstore.add_texts(texts)

    def add_documents(self, documents):
        self.vectorstore.add_documents(documents)

    def similarity_search(self, query, k=4):
        return self.vectorstore.similarity_search(query, k=k)
    
    def get_retriever(self, k=4):
        return self.vectorstore.as_retriever(search_kwargs={"k": k})