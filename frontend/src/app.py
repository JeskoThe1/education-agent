import streamlit as st
from api_client import APIClient

st.set_page_config(page_title="Education System Analyzer", layout="wide")

def upload_file(api_client):
    uploaded_file = st.file_uploader("Choose a file (optional)", type=["pdf", "txt", "doc", "docx"])
    if uploaded_file:
        with st.spinner("Uploading and processing file..."):
            response = api_client.upload_document(uploaded_file)
        
        if response.get("success"):
            st.success(f"File {uploaded_file.name} uploaded and processed successfully!")
        else:
            st.error(f"Failed to process document. Error: {response.get('error')}")

def analyze_query(api_client, query):
    if not query:
        st.warning("Please enter a question to analyze.")
        return

    with st.spinner("Analyzing..."):
        result = api_client.analyze_query(query)
    
    st.subheader("Analysis Result")
    st.write(result)

    st.download_button(
        label="Download results as TXT",
        data=result,
        file_name="analysis_results.txt",
        mime="text/plain"
    )

def main():
    st.title("Education System Analyzer")

    api_client = APIClient()

    upload_file(api_client)

    user_query = st.text_input("Enter your question about education systems:")
    
    if st.button("Analyze"):
        analyze_query(api_client, user_query)

if __name__ == "__main__":
    main()