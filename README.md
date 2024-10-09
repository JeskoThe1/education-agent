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

1. In a new terminal, start the Streamlit app:
   ```
   cd frontend/src
   streamlit run app.py
   ```

2. Upload education-related documents and start analyzing!

## Contributing

We welcome contributions to the Education System Analyzer! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request


