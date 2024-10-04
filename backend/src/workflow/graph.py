from langgraph.graph import END, StateGraph
from typing_extensions import TypedDict
from typing import List, Any
from .nodes import (
    retrieve_from_vectorstore,
    retrieve_from_graph,
    check_relevance,
    web_search,
    generate,
    check_hallucination
)


class GraphState(TypedDict):
    question: str
    generation: str
    vector_documents: List[Any]
    graph_result: str
    web_results: str
    hallucination: str
    final_answer: str
    retriever: Any
    graph_rag_chain: Any


def create_workflow():
    workflow = StateGraph(GraphState)
    
    workflow.add_node("retrieve_from_vectorstore", retrieve_from_vectorstore)
    workflow.add_node("retrieve_from_graph", retrieve_from_graph)
    workflow.add_node("check_relevance", check_relevance)
    workflow.add_node("web_search", web_search)
    workflow.add_node("generate", generate)
    workflow.add_node("check_hallucination", check_hallucination)
    
    workflow.set_entry_point("retrieve_from_vectorstore")
    
    workflow.add_edge("retrieve_from_vectorstore", "retrieve_from_graph")
    workflow.add_edge("retrieve_from_graph", "check_relevance")
    
    workflow.add_conditional_edges(
        "check_relevance",
        lambda x: x['web_search'],
        {
            "yes": "web_search",
            "no": "generate"
        }
    )
    
    workflow.add_edge("web_search", "generate")
    workflow.add_edge("generate", "check_hallucination")
    
    workflow.add_conditional_edges(
        "check_hallucination",
        lambda x: x["hallucination"],
        {
            False: END,
            True: "generate"
        }
    )
    
    return workflow.compile()