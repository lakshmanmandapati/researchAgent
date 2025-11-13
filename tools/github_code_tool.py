"""
Specialized GitHub Code Search Tool
"""

import requests
from crewai.tools import BaseTool


class GitHubCodeTool(BaseTool):
    name: str = "GitHub Code Tool"
    description: str = "Search code repositories directly on GitHub API for AI use cases."

    def _run(self, query: str) -> str:
        try:
            url = "https://api.github.com/search/repositories"
            resp = requests.get(
                url,
                params={"q": query, "sort": "stars", "order": "desc"},
                timeout=6,
                headers={"Accept": "application/vnd.github.v3+json"},
            )
            if resp.status_code != 200:
                return f"GitHub Search failed ({resp.status_code})"

            repos = resp.json().get("items", [])[:3]
            results = []
            for r in repos:
                results.append(
                    f"- **[{r['name']}]({r['html_url']})** ⭐ {r['stargazers_count']}\n"
                    f"  - {r.get('description','No description')}\n"
                )
            return "\n".join(results) if repos else "No GitHub repos found."
        except Exception as e:
            return f"GitHub error: {e}"


github_code_tool = GitHubCodeTool()