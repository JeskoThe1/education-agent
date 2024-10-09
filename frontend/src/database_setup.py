import streamlit as st
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from backend.src.rag.vectorstore import setup_vectorstore
from backend.src.graph_database.neo4j_manager import setup_graph_database, create_graph_rag_chain
from backend.src.workflow.graph import create_workflow

@st.cache_resource
def init_resources():
    vectorstore = setup_vectorstore()
    graph = setup_graph_database()
    graph_rag_chain = create_graph_rag_chain(graph)
    workflow = create_workflow()
    return vectorstore, graph, graph_rag_chain, workflow

def get_resources():
    return init_resources()