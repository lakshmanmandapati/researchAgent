"""
Dataset Agent - Optimized (with Kaggle + GitHub tools)
"""

from crewai import Agent, LLM
from tools.kaggle_tool import kaggle_dataset_tool
from tools.github_code_tool import github_code_tool
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = LLM(
    model="gemini/gemini-2.0-flash", api_key=gemini_api_key, temperature=0.25
)

dataset_agent = Agent(
    name="Dataset Curator",
    role="Data engineer specializing in dataset evaluation and curation",
    goal="For every AI use case, map Kaggle datasets and GitHub code repos to ensure completeness.",
    backstory="7+ year data engineer with expertise in dataset quality assessment",
    verbose=True,
    memory=True,
    tools=[kaggle_dataset_tool, github_code_tool],  # ✅ specialized tools
    allow_delegation=False,
    system_message=(
        "DATASET & RESOURCE CURATION:\n"
        "Loop through **every use case** provided.\n"
        "For each use case output:\n"
        "1. KAGGLE DATASETS (via Kaggle API)\n"
        "   - [Dataset Name](URL), size, quality score\n"
        "2. GITHUB REPOSITORIES (via GitHub API)\n"
        "   - [Repo Name](URL), stars, description\n"
        "3. Note any data preparation requirements\n"
        "Do not skip any use case. Ensure coverage for all."
    ),
    llm=llm,
)