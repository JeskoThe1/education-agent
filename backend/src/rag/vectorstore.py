from langchain_milvus import Milvus
from langchain_openai import OpenAIEmbeddings
from ..config import MILVUS_URI, OPENAI_API_KEY
import os

def setup_vectorstore():
    os.makedirs(os.path.dirname(MILVUS_URI), exist_ok=True)
    return Milvus(
        embedding_function=OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY),
        connection_args={"uri": MILVUS_URI},
        collection_name="education_documents",
        auto_id=True
    )

def add_documents_to_vectorstore(vectorstore, documents):
    vectorstore.add_documents(documents)
