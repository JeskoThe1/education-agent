import asyncio
from utils.helpers import save_to_json, load_from_json, save_to_text
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config
from data_processing.scraper import Scraper
from data_processing.preprocessor import Preprocessor
from rag.vectorstore import VectorStore
from analysis.education_analyzer import EducationAnalyzer
from analysis.comparative_analysis import ComparativeAnalysis


async def main():
    # Initialize components
    scraper = Scraper()
    preprocessor = Preprocessor()
    vectorstore = VectorStore()
    education_analyzer = EducationAnalyzer()
    comparative_analyzer = ComparativeAnalysis()

    # Scrape and process data
    # scraped_data = await scraper.scrape()
    # processed_data = preprocessor.process_text("\n".join([doc.page_content for doc in scraped_data]))
    pdf_data = preprocessor.process_all_pdfs()

    # Add data to vector store
    # vectorstore.add_texts(processed_data)
    vectorstore.add_documents(pdf_data)

    # Analyze education systems
    countries = ["Finland", "Estonia", "Poland"]
    analyses = {}
    for country in countries:
        analysis = education_analyzer.analyze_country(country)
        save_to_json(analysis, f"{country.lower()}_analysis.json")
        save_to_text(analysis, f"{country.lower()}_analysis.txt")
        analyses[country] = analysis

    # Perform comparative analysis
    comparison = comparative_analyzer.compare_countries(analyses)
    save_to_json(comparison, "comparative_analysis.json")

    print("Analysis complete. Results saved in the outputs directory.")

if __name__ == "__main__":
    asyncio.run(main())