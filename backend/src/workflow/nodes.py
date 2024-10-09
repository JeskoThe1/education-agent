from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from ..prompts.prompt_template import (
    retrieval_grader_prompt, 
    education_analysis_prompt, 
    hallucination_check_prompt
)
from ..llm_models.model_loader import get_local_llm, get_openai_llm
from ..web_search.search import perform_web_search

local_llm = get_local_llm()
openai_llm = get_openai_llm()

retrieval_grader = retrieval_grader_prompt | openai_llm | JsonOutputParser()
education_analyzer = education_analysis_prompt | openai_llm 
hallucination_checker = hallucination_check_prompt | openai_llm | JsonOutputParser()

def retrieve_from_vectorstore(state):
    print("---RETRIEVE FROM VECTOR STORE---")
    question = state["question"]
    documents = state["retriever"].invoke(question)
    print(documents)
    return {"vector_documents": documents, "question": question}

def retrieve_from_graph(state):
    print("---RETRIEVE FROM GRAPH---")
    question = state["question"]
    graph_qa_chain = state["graph_rag_chain"]
    graph_result = graph_qa_chain.invoke({"query": question})['result']
    print(graph_result)
    return {"graph_result": graph_result, "question": question}

def check_relevance(state):
    print("---CHECK RELEVANCE---")
    question = state["question"]
    vector_documents = state.get("vector_documents", [])
    graph_result = state.get("graph_result", "")

    vector_text = "\n".join([doc.page_content for doc in vector_documents]) if len(vector_documents) else " "

    graph_text = "\n".join(graph_result) if len(graph_result) else " "

    combined_context = f"Vector Text:\n{vector_text}\n\nGraph Text:\n{graph_text}"
    
    relevance_score = retrieval_grader.invoke({
        "question": question,
        "document": combined_context
    })

    grade = relevance_score['score']
    if grade.lower() == "yes":
        print("---GRADE: DOCUMENTS ARE RELEVANT---")
        web_search = "no"
    else:
        print("---GRADE: DOCUMENTS ARE NOT RELEVANT---")
        web_search = "yes"
    return {"question": question, "web_search": web_search}

def web_search(state):
    print("---WEB SEARCH---")
    question = state["question"]
    search_results = perform_web_search(question)
    print(search_results)
    return {"web_results": search_results, "question": question}

def generate(state):
    print("---GENERATE---")
    question = state["question"]
    vector_documents = state.get("vector_documents", [])
    graph_result = state.get("graph_result", "")
    web_results = state.get("web_results", "")

    context = ""
        
    if vector_documents:
        context += "Vector Results:\n"
        for i, doc in enumerate(vector_documents, 1):
            context += f"Document {i}:\n"
            context += f"Content: {doc.page_content}\n"
            context += f"Metadata: Page {doc.metadata.get('page', 'N/A')}, Source: {doc.metadata.get('source', 'N/A')}\n\n"

    if graph_result:
        context += "Graph Results:\n" + "\n".join(graph_result) + "\n\n"

    if web_results:
        context += "Web Search Results:\n"
        for i, result in enumerate(web_results, 1):
            context += f"Result {i}:\n"
            context += f"Content: {result['content']}\n"
            context += f"URL: {result.get('url', 'N/A')}\n\n"  

    generation = education_analyzer.invoke({
        "question": question,
        "context": context
    })
    
    return {
        "question": question,
        "generation": generation,
        "vector_documents": vector_documents,
        "graph_result": graph_result,
        "web_results": web_results,
    }

def check_hallucination(state):
    print("---CHECK HALLUCINATIONS---")
    generation = state["generation"]
    vector_documents = state["vector_documents"]
    graph_result = state["graph_result"]
    web_results = state.get("web_results", "")
    
    context = "\n".join([doc.page_content for doc in vector_documents]) if len(vector_documents) else " "
    context += "\nGraph Results:\n" + "\n".join(graph_result)
    if web_results:
        context += "\nWeb Search Results:\n" + "\n".join([d["content"] for d in web_results])
    
    result = hallucination_checker.invoke({
        "generation": generation,
        "context": context
    })
    
    return {"generation": generation, "hallucination": result["hallucination"]}
