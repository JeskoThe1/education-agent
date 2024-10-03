# Education System Analyzer

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [API Documentation](#api-documentation)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

The Education System Analyzer is a sophisticated tool designed to analyze and compare education systems from different countries. It leverages advanced natural language processing techniques and machine learning models to provide insightful analysis based on official education documents and user queries.

## Features

- Document Analysis: Upload and analyze education-related documents (PDF, DOC, DOCX, TXT)
- Custom Queries: Ask specific questions about education systems
- Country Comparison: Compare education systems of multiple countries
- Vector Store Integration: Efficient storage and retrieval of document embeddings
- User-friendly Interface: Built with Streamlit for easy interaction

## Project Structure

```
education_analysis_project/
├── backend/
│   ├── src/
│   │   ├── analysis/
│   │   │   ├── education_analyzer.py
│   │   │   └── comparative_analysis.py
│   │   ├── data_processing/
│   │   │   └── preprocessor.py
│   │   ├── storage/
│   │   │   └── vectorstore.py
│   │   ├── config.py
│   │   └── main.py
│   └── tests/
├── frontend/
│   ├── src/
│   │   ├── app.py
│   │   ├── api_client.py
│   └── └── file_processor.py
├── api/
│   ├── main.p
├── data/
│   ├── raw/
│   └── processed/
├── requirements.txt
├── docker-compose.yml
└── README.md
```

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
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Start the API server:
   ```
   cd api
   uvicorn main:app --reload
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

## Contributing

We welcome contributions to the Education System Analyzer! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
