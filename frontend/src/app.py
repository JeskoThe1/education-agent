import streamlit as st
import os
from api_client import APIClient
from file_processor import process_file_by_path

st.set_page_config(page_title="Education System Analyzer", layout="wide")

# Ensure data directory exists
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw')
os.makedirs(DATA_DIR, exist_ok=True)

def main():
    st.title("Education System Analyzer")

    api_client = APIClient()

    # File upload
    uploaded_files = st.file_uploader("Choose files", type=["pdf", "doc", "docx", "txt"], accept_multiple_files=True)
    documents = []
    if uploaded_files:
        for file in uploaded_files:
            try:
                # Save the file
                file_path = os.path.join(DATA_DIR, file.name)
                with open(file_path, "wb") as f:
                    f.write(file.getbuffer())
                st.success(f"File {file.name} saved successfully!")
                
                # Process the file
                processed_docs = process_file_by_path(file_path)
                documents.extend(processed_docs)
                st.success(f"File {file.name} processed successfully!")
            except Exception as e:
                st.error(f"Failed to process file {file.name}. Error: {str(e)}")

    # Analysis type selection
    analysis_type = st.radio("Select Analysis Type", ["Analyze", "Compare"])

    # User query input
    if analysis_type == "Analyze":
        user_query = st.text_input("Enter your query about an education system:")
    else:
        user_query = st.text_input("Enter the education systems you want to compare (e.g., 'Compare Finland and Estonia'):")

    if st.button("Submit"):
        if user_query:
            if analysis_type == "Analyze":
                result = api_client.analyze_query(user_query, documents)
                st.subheader("Analysis Result")
                st.write(result)
            else:
                result = api_client.compare_countries(user_query)
                st.subheader("Comparative Analysis")
                st.write(result)

            # Option to download results
            st.download_button(
                label="Download results as TXT",
                data=result,
                file_name="analysis_results.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()