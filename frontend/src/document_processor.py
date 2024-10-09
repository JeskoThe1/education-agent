import os
import streamlit as st
from database_setup import get_resources
from backend.src.data_processing.preprocessor import preprocess_document
from backend.src.rag.vectorstore import add_documents_to_vectorstore
from backend.src.graph_database.neo4j_manager import add_graph_documents

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def upload_document(file):
    vectorstore, graph, _, _ = get_resources()
    try:
        file_path = os.path.join(UPLOAD_DIR, file.name)
        with open(file_path, "wb") as buffer:
            buffer.write(file.getvalue())
        
        documents = preprocess_document(file_path)
        add_documents_to_vectorstore(vectorstore, documents)
        add_graph_documents(documents)
        
        return True, f"File {file.name} processed and added to the database"
    except Exception as e:
        return False, str(e)

def upload_files():
    uploaded_files = st.file_uploader("Choose files (optional)", type=["pdf", "txt", "doc", "docx"], accept_multiple_files=True)
    if uploaded_files:
        with st.spinner("Uploading and processing files..."):
            for uploaded_file in uploaded_files:
                success, message = upload_document(uploaded_file)
                if success:
                    st.success(message)
                else:
                    st.error(f"Failed to process document {uploaded_file.name}. Error: {message}")