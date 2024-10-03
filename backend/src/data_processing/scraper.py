from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import Html2TextTransformer
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config

class Scraper:
    def __init__(self, url="https://mon.gov.ua/tag/zagalna-serednya-osvita?&type=all&tag=zagalna-serednya-osvita"):
        self.loader = AsyncHtmlLoader([url])
        self.html2text = Html2TextTransformer()

    async def scrape(self):
        docs = self.loader.load()
        texts = self.html2text.transform_documents(docs)
        return texts