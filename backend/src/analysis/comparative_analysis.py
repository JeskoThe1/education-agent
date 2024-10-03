from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.llm_interface import LLMInterface

class ComparativeAnalysis:
    def __init__(self):
        self.llm = LLMInterface().get_llm()
        self.prompt = PromptTemplate(
            input_variables=["countries_data"],
            template="""
            Compare the education systems of the following countries:
            {countries_data}
            
            Provide a comparative analysis focusing on:
            1. Similarities and differences in PISA results
            2. Common and unique key features
            3. Overlap in key competencies
            """
        )
        self.chain = self.prompt | self.llm | StrOutputParser()

    def compare_countries(self, country_analyses):
        countries_data = "\n\n".join([
            f"Country: {country}\n{analysis}"
            for country, analysis in country_analyses.items()
        ])
        result = self.chain.invoke({"countries_data":countries_data})
        return result