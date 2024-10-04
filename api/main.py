import os
import sys
from fastapi import FastAPI, HTTPException, UploadFile, File

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pydantic import BaseModel
from backend.src.rag.vectorstore import setup_vectorstore, add_documents_to_vectorstore
from backend.src.graph_database.neo4j_manager import setup_graph_database, add_graph_documents, create_graph_rag_chain
from backend.src.workflow.graph import create_workflow
from backend.src.data_processing.preprocessor import preprocess_document

app = FastAPI()

class AnalyzeRequest(BaseModel):
    question: str

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

vectorstore = setup_vectorstore()
graph = setup_graph_database()
graph_rag_chain = create_graph_rag_chain(graph)
workflow = create_workflow()

@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    try:
        print(request)
        initial_state = {
            "question": request.question,
            "retriever": vectorstore.as_retriever(),                        
            "graph_rag_chain": graph_rag_chain       
        }
        result = None
        for output in workflow.stream(initial_state):
            for key, value in output.items():
                print(f"Finished running: {key}:")
        result = value["generation"]
        return {"result": result.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload_document")
async def upload_document(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        
        documents = preprocess_document(file_path)
        add_documents_to_vectorstore(vectorstore, documents)
        add_graph_documents(graph, documents)
        
        return {"success": True, "message": f"File {file.filename} processed and added to the database"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))