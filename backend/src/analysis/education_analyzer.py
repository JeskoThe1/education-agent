from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.llm_interface import LLMInterface
from utils.helpers import save_to_text
from rag.vectorstore import VectorStore

class EducationAnalyzer:
    def __init__(self):
        self.llm = LLMInterface().get_llm()
        self.retriever = VectorStore().get_retriever()
        self.prompt = PromptTemplate(
            input_variables=["country", "context"],
            template="""
            You are an expert in education systems. Your task is to analyze the education system of {country} based strictly on the following information provided:
            {context}

            In context you will be provided with metadata of the context, with contains sourse, page. Try to make references to that text in your analysis as much as possible. Reference should be in format: [Document: page].
            Important: Do not fabricate or infer any data that is not explicitly mentioned in the provided context. Your analysis should be grounded in the given information only. If any details are missing, indicate so without making assumptions.

            Provide the analysis in the following format:
            1. PISA results (if included in the context)
            2. Useful experience for Ukraine
            3. Mission and vision (if included in the context)
            4. Current development strategies
            5. Key features of the education system
            6. Key competencies
            7. General description of the education system's product
            8. Outcomes of this educational system in terms of soft skills. Format the outcomes as a table with 3 columns: how it is formed, the outcome itself, and its generalized name.
            
            Example table (for Finnish Educational System):
            Learning Approach  | Outcome                                                | General Category
            ------------------------------------------------------------------------------------------
            Inquiry-Based Learning: Finnish education encourages students to ask         | Graduates who can analyze complex situations, generate innovative solutions, and think independently. | Critical Thinking and Problem-Solving Skills
            questions, think critically, and engage in problem-solving activities.
            Creative Thinking: Emphasis on open-ended tasks and projects fosters          | Graduates skilled in generating creative solutions.                | Innovation and Creativity
            creativity and innovation.
            Self-Directed Learning: Students are given autonomy to pursue their           | Individuals committed to lifelong learning and adaptable to new     | Lifelong Learning Attitude
            interests, promoting intrinsic motivation.                                    | learning opportunities.
            
            Remember: Do not invent any information. Use only the data given in the context.
            """
        )

    def analyze_country(self, country):
        docs = self.retriever.get_relevant_documents(country)
        context = "\n".join([
            json.dumps({
                "content": doc.page_content,
                "metadata": doc.metadata
            }) for doc in docs
        ])
        chain = self.prompt | self.llm | StrOutputParser()
        return chain.invoke({"country": country, "context": context})