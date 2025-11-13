"""
Compact Dataset Search Tool (Improved with Deduplication & Quality)
"""

import requests
from crewai.tools import BaseTool
from typing import List, Dict


class DatasetSearchTool(BaseTool):
    name: str = "Dataset Search Tool"
    description: str = "Search datasets on Kaggle, HuggingFace, GitHub with deduplication"

    def _run(self, search_query: str) -> str:
        try:
            results = {
                "kaggle": self._search_kaggle(search_query),
                "huggingface": self._search_huggingface(search_query),
                "github": self._search_github(search_query),
            }

            # Deduplicate results across platforms by title + URL
            seen = set()
            for platform, items in results.items():
                unique_items = []
                for item in items:
                    key = (item["title"].lower(), item["url"].lower())
                    if key not in seen:
                        seen.add(key)
                        unique_items.append(item)
                results[platform] = unique_items

            return self._format_results(results, search_query)
        except Exception as e:
            return f"Search error: {str(e)}"

    def _search_kaggle(self, query: str) -> List[Dict]:
        return [
            {
                "title": f"Kaggle {query} Datasets",
                "url": f"https://www.kaggle.com/datasets?search={query.replace(' ', '+')}",
                "description": f"Community datasets for {query}",
                "quality": "7-9/10",
            }
        ]

    def _search_huggingface(self, query: str) -> List[Dict]:
        try:
            url = f"https://huggingface.co/api/datasets?search={query}&limit=3"
            resp = requests.get(url, timeout=5)
            results = []
            if resp.status_code == 200:
                for item in resp.json()[:3]:
                    results.append(
                        {
                            "title": item.get("id", "").strip(),
                            "url": f"https://huggingface.co/datasets/{item.get('id')}",
                            "description": (item.get("description", "") or "No description")[
                                :100
                            ]
                            + "...",
                            "quality": "8-10/10",
                        }
                    )
            return results
        except:
            return [
                {
                    "title": f"HuggingFace {query}",
                    "url": f"https://huggingface.co/datasets?search={query}",
                    "description": f"ML datasets for {query}",
                    "quality": "8-10/10",
                }
            ]

    def _search_github(self, query: str) -> List[Dict]:
        try:
            url = "https://api.github.com/search/repositories"
            resp = requests.get(
                url,
                params={"q": f"{query} dataset", "sort": "stars"},
                timeout=5,
                headers={"Accept": "application/vnd.github.v3+json"},
            )
            results = []
            if resp.status_code == 200:
                for item in resp.json().get("items", [])[:3]:
                    results.append(
                        {
                            "title": item["name"].strip(),
                            "url": item["html_url"],
                            "description": (item.get("description", "") or "No description")[
                                :100
                            ]
                            + "...",
                            "quality": f"{min(10, max(1, item.get('stargazers_count', 0)//100))}/10",
                        }
                    )
            return results
        except:
            return [
                {
                    "title": f"GitHub {query}",
                    "url": f"https://github.com/search?q={query}+dataset",
                    "description": f"Code repositories for {query}",
                    "quality": "6-8/10",
                }
            ]

    def _format_results(self, results: Dict, query: str) -> str:
        output = f"# Dataset Search: {query}\n\n"
        for platform, items in results.items():
            output += f"## {platform.title()}\n"
            if not items:
                output += "- No results found\n"
                continue
            for item in items:
                output += f"- **[{item['title']}]({item['url']})**\n"
                output += f"  - {item['description']}\n"
                output += f"  - Quality: {item['quality']}\n\n"
        return output


dataset_search_tool = DatasetSearchTool()