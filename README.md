# Education System Analyzer

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Documentation](#api-documentation)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The Education System Analyzer is a sophisticated tool designed to analyze and compare education systems from different countries. It leverages advanced natural language processing techniques and machine learning models to provide insightful analysis based on official education documents and user queries.

## Features

- Document Analysis: Upload and analyze education-related documents (PDF, DOC, DOCX, TXT)
- Custom Queries: Ask specific questions about education systems
- Country Comparison: Compare education systems of multiple countries
- Vector Store Integration: Efficient storage and retrieval of document embeddings
- User-friendly Interface: Built with Streamlit for easy interaction

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/education-analysis-project.git
   cd education-analysis-project
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add the following:
   ```
    OPENAI_API_KEY=sk...
    TAVILY_API_KEY=tvly...
    NEO4J_URI=neo4j...
    NEO4J_USERNAME=...
    NEO4J_PASSWORD=...
   ```

## Usage

1. Start the API server:
   ```
   cd api
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

2. In a new terminal, start the Streamlit app:
   ```
   cd frontend/src
   streamlit run app.py
   ```
   
3. Or you may do two previous operations in one go:
   ```
   docker compose up --build
   ```
   But then don't forget to change base url in frontend/src/api_client.py with "http://api:8000"
   
5. Open your web browser and navigate to `http://localhost:8501`

6. Upload education-related documents and start analyzing!

## API Documentation

### Analyze Endpoint

- **URL**: `/analyze`
- **Method**: POST
- **Body**:
  ```json
  {
    "query": "string",
    "documents": [
      {
        "page_content": "string",
        "metadata": {}
      }
    ]
  }
  ```
- **Response**:
  ```json
  {
    "result": "string"
  }
  ```

### Compare Endpoint

- **URL**: `/compare`
- **Method**: POST
- **Body**:
  ```json
  {
    "query": "string"
  }
  ```
- **Response**:
  ```json
  {
    "result": "string"
  }
  ```
  
## 🚀 Deployment

### Prerequisites

- AWS CLI installed and configured with appropriate permissions
- Docker and Docker Compose installed

### Deploying to AWS

1. Update the variables in `deploy.sh` with your AWS account details:
   ```bash
   AWS_ACCOUNT_ID="your-aws-account-id"
   AWS_REGION="your-aws-region"
   ```

2. Ensure you have created an ECS cluster and service in your AWS account.

3. Run the deployment script:
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

4. The script will build the Docker images, push them to Amazon ECR, update the ECS task definition, and deploy the new version to your ECS service.

5. Once the deployment is complete, you can access your application using the public DNS of your ECS service's load balancer.

## Contributing

We welcome contributions to the Education System Analyzer! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request


