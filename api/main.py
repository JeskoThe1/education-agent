from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.src.analysis.education_analyzer import EducationAnalyzer
from backend.src.analysis.comparative_analysis import ComparativeAnalysis
from backend.src.rag.vectorstore import VectorStore
from backend.src.data_processing.preprocessor import Preprocessor
from backend.src.config import Config
from langchain_core.documents import Document

app = FastAPI()

class SerializedDocument(BaseModel):
    page_content: str
    metadata: dict

class AnalyzeRequest(BaseModel):
    query: str
    documents: Optional[List[SerializedDocument]] = None

class CompareRequest(BaseModel):
    query: str

config = Config()
education_analyzer = EducationAnalyzer()
comparative_analyzer = ComparativeAnalysis()
vectorstore = VectorStore()
preprocessor = Preprocessor()

@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    try:
        if request.documents:
            documents = [Document(page_content=doc.page_content, metadata=doc.metadata) for doc in request.documents]
            vectorstore.add_documents(documents)
        
        result = education_analyzer.analyze_country(request.query)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/compare")
async def compare(request: CompareRequest):
    try:
        result = comparative_analyzer.compare_countries(request.query)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)