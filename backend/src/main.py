from rag.vectorstore import setup_vectorstore
from graph_database.neo4j_manager import setup_graph_database, create_graph_qa_chain
from workflow.graph import create_workflow

def main():
    vectorstore = setup_vectorstore()
    graph = setup_graph_database()
    graph_qa_chain = create_graph_qa_chain(graph)
    app = create_workflow(vectorstore, graph_qa_chain)
    
    inputs = {"question": "Compare the education systems of Finland and Estonia"}
    for output in app.stream(inputs):
        for key, value in output.items():
            print(f"Finished running: {key}:")
        if "final_answer" in value:
            print("Final Answer:", value["final_answer"])

if __name__ == "__main__":
    main()