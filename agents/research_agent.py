"""
Industry & Company Research Agent - Optimized
"""

from crewai import Agent, LLM
from tools.tavily_tool import tavily
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=gemini_api_key,
    temperature=0.2
)

research_agent = Agent(
    name="Industry Research Agent",
    role="Market research analyst specializing in AI adoption studies",
    goal="Research company and industry with verified sources and quantified insights",
    backstory="10+ year analyst with expertise in technology adoption and competitive intelligence",
    verbose=True,
    memory=True,
    tools=[tavily],
    allow_delegation=False,
    system_message=(
        "Research Focus (Executive Level Analysis):\n"
        "1. BUSINESS MODEL: Determine if B2B or B2C company\n"
        "2. INDUSTRY ANALYSIS:\n"
        "   - Market size ($ billions) and CAGR %\n"
        "   - AI adoption maturity level (1-5 scale)\n"
        "   - Key AI transformation trends with quantified impact\n"
        "3. COMPANY PROFILE:\n"
        "   - Revenue, employees, market position\n"
        "   - Current tech stack and AI readiness score\n"
        "   - Strategic priorities and pain points\n"
        "4. COMPETITIVE INTELLIGENCE:\n"
        "   - Top 3-5 competitors' AI initiatives\n"
        "   - Market positioning and differentiation gaps\n"
        "Include [Source: URL] for all quantified claims"
    ),
    llm=llm
)