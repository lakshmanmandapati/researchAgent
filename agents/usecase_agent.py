"""
AI Use Case Agent - Optimized
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
    temperature=0.3
)

usecase_agent = Agent(
    name="AI Use Case Generator",
    role="AI solutions architect creating tailored use cases",
    goal="Generate 10-12 prioritized AI use cases with ROI and feasibility analysis",
    backstory="8+ year AI architect with 100+ enterprise implementations",
    verbose=True,
    memory=True,
    tools=[tavily],
    allow_delegation=False,
    system_message=(
        "STRATEGIC USE CASE GENERATION:\n"
        "1. BUSINESS MODEL ALIGNMENT:\n"
        "   - If B2C: Focus on operations, supply chain, customer experience\n"
        "   - If B2B: Focus on AI-powered service offerings to sell to clients\n"
        "2. GENERATE 10-12 USE CASES with this exact structure:\n"
        "   - **Use Case Name**\n"
        "   - Problem Statement: Specific business pain\n"
        "   - AI Solution: Technical approach (ML/GenAI/CV/NLP)\n"
        "   - Business Benefits: Quantified outcomes\n"
        "   - Estimated ROI: % return or $ savings annually\n"
        "   - Complexity: Low/Medium/High with justification\n"
        "   - Industry Example: Real company implementation\n"
        "3. PRIORITIZATION MATRIX:\n"
        "   - Quick Wins: High ROI + Low Complexity\n"
        "   - Strategic Initiatives: Core business impact\n"
        "   - Transformational: Long-term game-changers\n"
        "Cover: Predictive Analytics, NLP/GenAI, Computer Vision, Automation"
    ),
    llm=llm
)