# AI Use Case Generator

Multi-agent system that researches companies and generates AI transformation proposals with datasets and implementation roadmaps.

## What it does

Input a company name → Get a full AI strategy report including:
- Industry analysis and competitive intelligence
- 10-12 prioritized AI use cases with ROI estimates
- Kaggle datasets and GitHub repos for each use case
- Phased implementation roadmap

Built with CrewAI orchestrating 4 specialized agents that work sequentially.

## Quick Start

```bash
git clone https://github.com/lakshmanmandapati/researchAgent.git
cd research-agent
pip install -r requirements.txt
```

Create `.env` file:
```
GEMINI_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
KAGGLE_USERNAME=your_username
KAGGLE_KEY=your_key
```

Run:
```bash
python run.py
# Opens at http://localhost:8501
```

## How it works

Four agents run sequentially, each feeding context to the next:

**1. Research Agent** (`research_agent.py`)
- Determines B2B vs B2C business model
- Pulls market size, CAGR, AI adoption trends via Tavily
- Analyzes competitors' AI initiatives
- Outputs: `{company}_research.md`

**2. Use Case Agent** (`usecase_agent.py`)
- Generates 10-12 AI use cases tailored to business model
- Each includes: problem statement, technical approach, ROI estimate, complexity
- Categorizes into Quick Wins / Strategic / Transformational
- Outputs: `{company}_usecases.md`

**3. Dataset Agent** (`dataset_agent.py`)
- Maps Kaggle datasets to each use case
- Finds GitHub repos with implementation code
- Includes quality scores and direct links
- Outputs: `{company}_resources.md`

**4. Proposal Agent** (`proposal_agent.py`)
- Synthesizes everything into executive report
- Adds implementation roadmap with specific phases
- Formats as markdown with clickable references
- Outputs: `{company}_proposal.md`

## Project Structure

```
research-agent/
├── agents/
│   ├── research_agent.py      # Industry/company research
│   ├── usecase_agent.py        # AI use case generation
│   ├── dataset_agent.py        # Dataset curation
│   └── proposal_agent.py       # Final report synthesis
├── config/
│   ├── crew.py                 # CrewAI orchestration
│   └── tasks.py                # Task definitions
├── tools/
│   ├── tavily_tool.py          # Web search wrapper
│   ├── kaggle_tool.py          # Kaggle API integration
│   ├── github_code_tool.py     # GitHub repo search
│   ├── dataset_tool.py         # Multi-platform dataset search
│   ├── trusted_search_tool.py  # Filtered domain search
│   └── filemanager_tool.py     # Output file handling
├── main.py                     # Streamlit UI
├── run.py                      # Launch script
└── outputs/                    # Generated reports
```

## Stack

- **CrewAI** - Agent orchestration framework
- **Gemini 2.0 Flash** - LLM for all agents (via Google AI)
- **Tavily API** - Web search for research
- **Kaggle API** - Dataset discovery
- **GitHub API** - Code repository search
- **Streamlit** - Web interface

## Configuration

Each agent uses Gemini 2.0 Flash with different temperatures:
- Research: 0.2 (factual)
- Use Case: 0.3 (creative but grounded)
- Dataset: 0.25 (precise)
- Proposal: 0.3 (synthesizes well)

Sequential process ensures context flows: Research → Use Cases → Datasets → Proposal

## Output Format

Final proposal includes:
1. Executive Summary (key recommendations + quantified impact)
2. Market Research (industry size, trends, competitors)
3. AI Use Case Portfolio (10-12 prioritized use cases)
4. Dataset & Resources (Kaggle/GitHub links per use case)
5. Implementation Roadmap (3-phase timeline)
6. References (all sources cited)

All outputs saved to `outputs/` directory as markdown files.

## Notes

- Uses `crewai` memory for context sharing between agents
- GitHub Actions workflow mentioned in old README doesn't exist yet
- Agents have `allow_delegation=False` to prevent infinite loops
- File manager tool prevents output truncation issues