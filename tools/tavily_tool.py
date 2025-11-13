"""
Tavily Search Tool Wrapper
"""

from crewai_tools import TavilySearchTool
import os
from dotenv import load_dotenv

load_dotenv()

class TavilyTool:
    def __init__(self):
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            raise ValueError("Missing TAVILY_API_KEY")
        self.tool = TavilySearchTool(
            api_key=api_key,
            search_depth="advanced",
            max_results=5,
            include_raw_content=False,
            include_images=False
        )

    def search_industry(self, query: str):
        return self.tool.run(f"industry analysis market research {query} 2024")

    def search_ai_use_cases(self, industry: str):
        return self.tool.run(f"AI ML GenAI applications in {industry} industry 2024")

    def search_competitors(self, company: str, industry: str):
        return self.tool.run(f"{company} competitors market positioning {industry}")


tavily = TavilyTool().tool

