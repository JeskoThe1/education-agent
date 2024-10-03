import requests

class APIClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url

    def analyze_query(self, query, documents=None):
        endpoint = f"{self.base_url}/analyze"
        
        # Convert Document objects to dictionaries
        serialized_documents = None
        if documents:
            serialized_documents = [
                {
                    "page_content": doc.page_content,
                    "metadata": doc.metadata
                }
                for doc in documents
            ]
        
        data = {"query": query, "documents": serialized_documents}
        response = requests.post(endpoint, json=data)
        return response.json()["result"]

    def compare_countries(self, query):
        endpoint = f"{self.base_url}/compare"
        data = {"query": query}
        response = requests.post(endpoint, json=data)
        return response.json()["result"]