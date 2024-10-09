import streamlit as st
from analyzer import analyze_query
from document_processor import upload_files

st.set_page_config(page_title="Education System Analyzer", layout="wide")

def main():
    st.title("Education System Analyzer")

    upload_files()

    user_query = st.text_input("Enter your question about education systems:")
    
    if st.button("Analyze"):
        if not user_query:
            st.warning("Please enter a question to analyze.")
        else:
            with st.spinner("Analyzing..."):
                result = analyze_query(user_query)
            
            if result:
                st.subheader("Analysis Result")
                st.write(result)

                st.download_button(
                    label="Download results as TXT",
                    data=result,
                    file_name="analysis_results.txt",
                    mime="text/plain"
                )

if __name__ == "__main__":
    main()