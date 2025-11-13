"""
Specialized Kaggle Dataset Tool
"""

import requests
from crewai.tools import BaseTool


class KaggleDatasetTool(BaseTool):
    name: str = "Kaggle Dataset Tool"
    description: str = "Search datasets directly via Kaggle API."

    def _run(self, query: str) -> str:
        try:
            url = f"https://www.kaggle.com/api/v1/datasets/list"
            headers = {"User-Agent": "Mozilla"}  # if kaggle requires login, adjust with creds
            resp = requests.get(url, params={"search": query}, headers=headers, timeout=6)

            if resp.status_code != 200:
                return f"Kaggle Search failed ({resp.status_code})"

            results = []
            for ds in resp.json()[:3]:
                results.append(
                    f"- **[{ds['title']}]({'https://www.kaggle.com/datasets/'+ds['ref']})**\n"
                    f"  - Size: {ds.get('size','Unknown')} - {ds.get('licenses','N/A')}\n"
                )

            return "\n".join(results) if results else "No Kaggle datasets found."
        except Exception as e:
            return f"Kaggle error: {e}"


kaggle_dataset_tool = KaggleDatasetTool()