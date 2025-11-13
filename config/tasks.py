"""
Optimized Task Configuration
"""

import os
from crewai import Task

class TaskConfig:
    @staticmethod
    def _ensure_output_dir():
        os.makedirs("outputs", exist_ok=True)

    @staticmethod
    def create_research_task(research_agent, company_name: str):
        TaskConfig._ensure_output_dir()
        return Task(
            description=(
                f"Conduct executive-level research for {company_name}:\n"
                f"1. BUSINESS MODEL: Identify if {company_name} is B2B or B2C company\n"
                f"2. INDUSTRY ANALYSIS: Market size ($B), CAGR, AI adoption trends\n"
                f"3. COMPANY ANALYSIS: Revenue, positioning, tech readiness for {company_name}\n"
                f"4. COMPETITIVE LANDSCAPE: Top players' AI strategies in {company_name}'s market\n"
                f"Quantify everything - market size, growth rates, adoption metrics\n"
                f"Include [Source: URL] for all major claims"
            ),
            expected_output=(
                "Strategic research report with:\n"
                "- B2B/B2C classification (or state 'No trusted info found')\n"
                "- Market analysis (size, CAGR, trends) with sources if available\n"
                "- Company profile with AI readiness score\n"
                "- Competitor AI initiatives\n"
                "⚠️ If any section lacks info from trusted sources, explicitly note it."
            ),
            agent=research_agent,
            output_file=f"outputs/{company_name.lower().replace(' ', '_')}_research.md",
        )

    @staticmethod
    def create_usecase_task(usecase_agent, company_name: str):
        TaskConfig._ensure_output_dir()
        return Task(
            description=(
                f"Generate 10-12 strategic AI use cases for {company_name}:\n"
                f"1. Use business model (B2B/B2C) from research to tailor use cases\n"
                f"2. Create detailed use cases with exact structure:\n"
                f"   - Problem Statement, AI Solution, Business Benefits\n"
                f"   - Estimated ROI (% or $ savings), Complexity, Industry Example\n"
                f"3. Categorize into: Quick Wins, Strategic Initiatives, Transformational\n"
                f"4. Cover: Predictive Analytics, NLP/GenAI, Computer Vision, Automation\n"
                f"Make each use case a mini-business case for {company_name}"
            ),
            expected_output=(
                f"AI Use Case Portfolio for {company_name}:\n"
                f"- 10-12 detailed use cases with full business case structure\n"
                f"- Clear prioritization: Quick Wins/Strategic/Transformational\n"
                f"- Quantified ROI estimates for each use case\n"
                f"- Industry examples and implementation complexity\n"
                f"- Tailored to {company_name}'s business model and industry"
            ),
            agent=usecase_agent,
            output_file=f"outputs/{company_name.lower().replace(' ', '_')}_usecases.md",
        )

    @staticmethod
    def create_dataset_task(dataset_agent, company_name: str):
        TaskConfig._ensure_output_dir()
        return Task(
            description=(
                f"Find datasets and resources for {company_name} AI use cases:\n"
                f"1. Map specific datasets to each use case identified\n"
                f"2. Search Kaggle, HuggingFace, GitHub for relevant resources\n"
                f"3. For each resource provide: [Title](URL), quality score, description\n"
                f"4. Include pre-trained models, APIs, and code repositories\n"
                f"5. Organize by use case priority (Quick Wins first)\n"
                f"Focus on resources most relevant to {company_name}'s industry"
            ),
            expected_output=(
                f"Resource Asset Collection for {company_name}:\n"
                f"- Datasets mapped to specific use cases with quality scores\n"
                f"- Pre-trained models and commercial APIs\n"
                f"- Code repositories with implementation examples\n"
                f"- All resources with clickable links and descriptions\n"
                f"- Organized by use case priority tier"
            ),
            agent=dataset_agent,
            output_file=f"outputs/{company_name.lower().replace(' ', '_')}_resources.md",
        )

    @staticmethod
    def create_proposal_task(proposal_agent, company_name: str):
        TaskConfig._ensure_output_dir()
        return Task(
            description=(
                f"Create executive AI Transformation Proposal for {company_name}:\n"
                f"Synthesize all research, use cases, and resources into professional report:\n"
                f"1. Executive Summary with key recommendations\n"
                f"2. Market Research & Industry Analysis (quantified)\n"
                f"3. AI Use Case Portfolio (prioritized with ROI)\n"
                f"4. Dataset & Resource Assets (organized by use case)\n"
                f"5. Implementation Roadmap (specific phases with named use cases)\n"
                f"6. References (all sources with clickable links)\n"
                f"Quality must match top-tier strategy consultant standards"
            ),
            expected_output=(
                f"EXECUTIVE AI TRANSFORMATION PROPOSAL for {company_name}:\n"
                f"- Professional executive summary with quantified impact\n"
                f"- Market analysis with industry insights and trends\n"
                f"- 10-12 prioritized use cases with business cases\n"
                f"- Resource recommendations mapped to use cases\n"
                f"- Phased implementation roadmap with specific use case timelines\n"
                f"- Complete reference list with sources\n"
                f"- Executive presentation quality with proper formatting"
            ),
            agent=proposal_agent,
            output_file=f"outputs/{company_name.lower().replace(' ', '_')}_proposal.md",
        )