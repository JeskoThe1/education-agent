from langchain_community.tools.tavily_search import TavilySearchResults
from ..config import TAVILY_API_KEY

def get_web_search_tool():
    return TavilySearchResults(api_key=TAVILY_API_KEY)

def perform_web_search(query):
    search_tool = get_web_search_tool()
    results = search_tool.run(query)
    return results