"""
Trusted Search Tool - Proper Tavily API with Trusted Sources
"""

import os
import requests
from crewai.tools import BaseTool
from typing import List, ClassVar

class TrustedSearchTool(BaseTool):
    name: str = "Trusted Search Tool"
    description: str = "Search limited to authoritative domains (Reuters, Bloomberg, FT, NYT, WSJ, etc.)"

    trusted_sites: ClassVar[List[str]] = [
        "reuters.com",
        "bloomberg.com",
        "ft.com",
        "nytimes.com",
        "wsj.com",
        "bbc.com",
        "cnn.com",
        "starbucks.com"  # official newsroom
    ]

    def _run(self, query: str) -> str:
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            return "❌ Tavily API key missing."

        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
        results = []

        try:
            # loop through trusted sites
            for site in self.trusted_sites:
                payload = {"query": f"site:{site} {query}", "max_results": 3}
                resp = requests.post("https://api.tavily.com/search", headers=headers, json=payload, timeout=10)

                if resp.status_code == 200:
                    for r in resp.json().get("results", []):
                        results.append(
                            f"- **[{r.get('title','No Title')}]({r.get('url','')})** ({site})\n"
                            f"  - {(r.get('content','') or '')[:150]}...\n"
                        )

            if not results:
                return "⚠️ No results found even on trusted domains."

            return "### Trusted Results:\n\n" + "\n".join(results)

        except Exception as e:
            return f"❌ Trusted search error: {e}"


trusted_search_tool = TrustedSearchTool()