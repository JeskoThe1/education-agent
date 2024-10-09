import streamlit as st
from database_setup import get_resources

def analyze(question: str):
    vectorstore, graph, graph_rag_chain, workflow = get_resources()
    try:
        initial_state = {
            "question": question,
            "retriever": vectorstore.as_retriever(),
            "graph_rag_chain": graph_rag_chain
        }
        result = None
        for output in workflow.stream(initial_state):
            for key, value in output.items():
                st.write(f"Finished running: {key}")
        result = value["generation"]
        return result.content
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

def analyze_query(query: str):
    return analyze(query)