from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain_core.documents import Document
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config

class Preprocessor:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )

    def process_text(self, text, metadata=None):
        chunks = self.text_splitter.split_text(text)
        return [Document(page_content=chunk, metadata=metadata) for chunk in chunks]

    def process_pdf(self, pdf_path):
        loader = PyPDFLoader(pdf_path)
        pages = loader.load_and_split()
        return self.text_splitter.split_documents(pages)

    def process_doc(self, doc_path):
        loader = Docx2txtLoader(doc_path)
        pages = loader.load_and_split()
        return self.text_splitter.split_documents(pages)

    def process_txt(self, txt_path):
        loader = TextLoader(txt_path)
        documents = loader.load()
        return self.text_splitter.split_documents(documents)

    def process_all_pdfs(self):
        all_docs = []
        for filename in os.listdir(config.PDF_DIR):
            if filename.endswith(".pdf"):
                file_path = os.path.join(config.PDF_DIR, filename)
                all_docs.extend(self.process_pdf(file_path))
        return all_docs