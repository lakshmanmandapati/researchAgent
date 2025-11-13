"""
Crew Configuration
"""

import os
from crewai import Crew, Process, LLM
from agents.research_agent import research_agent
from agents.usecase_agent import usecase_agent
from agents.dataset_agent import dataset_agent
from agents.proposal_agent import proposal_agent
from config.tasks import TaskConfig
from dotenv import load_dotenv

load_dotenv()

class AIUseCaseGenerationCrew:
    def __init__(self, company):
        self.company = company
        self.task_config = TaskConfig()

        self.research_task = self.task_config.create_research_task(research_agent, company)
        self.usecase_task = self.task_config.create_usecase_task(usecase_agent, company)
        self.dataset_task = self.task_config.create_dataset_task(dataset_agent, company)
        self.proposal_task = self.task_config.create_proposal_task(proposal_agent, company)

        self.usecase_task.context = [self.research_task]
        self.dataset_task.context = [self.usecase_task]
        self.proposal_task.context = [
            self.research_task, self.usecase_task, self.dataset_task
        ]

    def create(self):
        """Initialize Crew with all agents and tasks"""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Missing GEMINI_API_KEY in environment variables")

        return Crew(
            agents=[research_agent, usecase_agent, dataset_agent, proposal_agent],
            tasks=[self.research_task, self.usecase_task, self.dataset_task, self.proposal_task],
            process=Process.sequential,
            verbose=True,
            output_log_file=f"outputs/{self.company.lower().replace(' ','_')}_log.txt",
            llm=LLM(
                model="gemini/gemini-2.0-flash",
                api_key=api_key,
                temperature=0.35
            )
        )

    def kickoff(self):
        """Run the full workflow"""
        return self.create().kickoff()


def create_ai_usecase_crew(company_name: str) -> AIUseCaseGenerationCrew:
    """Factory function to create AIUseCaseGenerationCrew instance"""
    return AIUseCaseGenerationCrew(company_name)


def _detect_business_model(self, company: str) -> str:
    """Helper to provide business model context to agents"""
    b2c_indicators = ["retail", "consumer", "brand", "marketplace", "gaming"]
    b2b_indicators = ["software", "enterprise", "consulting", "services", "platform"]
    
    return "B2B/B2C classification will be determined by research agent"