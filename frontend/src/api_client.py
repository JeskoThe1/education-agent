import requests

class APIClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url

    def analyze_query(self, query):
        """
        Send a query to the API for analysis.
        
        Args:
            query (str): The question to be analyzed.
        
        Returns:
            str: The analysis result.
        """
        endpoint = f"{self.base_url}/analyze"
        response = requests.post(endpoint, json={"question": query})
        print(response)
        if response.status_code == 200:
            return response.json()["result"]
        else:
            raise Exception(f"Error in analyze_query: {response.text}")

    def upload_document(self, file):
        """
        Upload a document to the API for processing.
        
        Args:
            file (file object): The file to be uploaded.
        
        Returns:
            dict: A dictionary containing the success status and a message.
        """
        endpoint = f"{self.base_url}/upload_document"
        files = {"file": (file.name, file, file.type)}
        response = requests.post(endpoint, files=files)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error in upload_document: {response.text}")