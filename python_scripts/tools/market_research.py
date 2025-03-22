from typing import Any

import aiohttp
from fastapi.responses import StreamingResponse as FastAPIStreamingResponse
from loguru import logger

from reworkd_platform.settings import settings
from reworkd_platform.web.api.agent.stream_mock import stream_string
from reworkd_platform.web.api.agent.tools.reason import Reason
from reworkd_platform.web.api.agent.tools.tool import Tool
from reworkd_platform.web.api.agent.tools.utils import summarize_with_sources, CitedSnippet
from reworkd_platform.schemas.user import UserBase
from reworkd_platform.db.crud.oauth import OAuthCrud

class MarketResearch(Tool):
    description = (
        "Conduct market research to identify target audiences, analyze competitors, "
        "and discover market trends for marketing campaigns.\n"
    )
    public_description = "Research market trends, target audiences, and competitors."
    arg_description = "The specific market, product, audience, or competitor to research."
    image_url = "/tools/market-research.png"

    @staticmethod
    def available() -> bool:
        return settings.serp_api_key is not None and settings.serp_api_key != ""

    async def call(
        self, goal: str, task: str, input_str: str, user: UserBase, oauth_crud: OAuthCrud, *args: Any, **kwargs: Any
    ) -> FastAPIStreamingResponse:
        try:
            # First, search for market trends
            market_trends = await self._search_market_trends(input_str)
            
            # Then, search for target audience information
            audience_info = await self._search_target_audience(input_str)
            
            # Finally, search for competitor analysis
            competitor_info = await self._search_competitors(input_str)
            
            # Combine all research results
            combined_results = market_trends + audience_info + competitor_info
            
            if len(combined_results) == 0:
                return stream_string("No relevant market research information was found", True)
            
            return summarize_with_sources(self.model, self.language, goal, task, combined_results)
            
        except Exception as e:
            logger.exception(f"Error in market research: {str(e)}")
            return await Reason(self.model, self.language).call(
                goal, task, input_str, user, oauth_crud, *args, **kwargs
            )

    async def _search_market_trends(self, query: str) -> list[CitedSnippet]:
        """Search for market trends related to the query"""
        search_term = f"{query} market trends analysis recent data"
        return await self._perform_search(search_term)

    async def _search_target_audience(self, query: str) -> list[CitedSnippet]:
        """Search for target audience information related to the query"""
        search_term = f"{query} target audience demographics preferences"
        return await self._perform_search(search_term)

    async def _search_competitors(self, query: str) -> list[CitedSnippet]:
        """Search for competitor information related to the query"""
        search_term = f"{query} competitors market analysis strategy"
        return await self._perform_search(search_term)

    async def _perform_search(self, search_term: str) -> list[CitedSnippet]:
        """Perform a search using the SERP API and return formatted results"""
        headers = {
            "X-API-KEY": settings.serp_api_key or "",
            "Content-Type": "application/json",
        }
        params = {
            "q": search_term,
        }

        snippets = []
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    "https://google.serper.dev/search", headers=headers, params=params
                ) as response:
                    response.raise_for_status()
                    search_results = await response.json()
                    
                    # Process answer box if available
                    if search_results.get("answerBox"):
                        answer_box = search_results.get("answerBox", {})
                        answer_values = []
                        
                        if answer_box.get("answer"):
                            answer_values.append(answer_box.get("answer"))
                        elif answer_box.get("snippet"):
                            answer_values.append(answer_box.get("snippet").replace("\n", " "))
                        elif answer_box.get("snippetHighlighted"):
                            answer_values.append(", ".join(answer_box.get("snippetHighlighted")))
                        
                        if answer_values:
                            snippets.append(
                                CitedSnippet(
                                    len(snippets) + 1,
                                    "\n".join(answer_values),
                                    f"https://www.google.com/search?q={search_term.replace(' ', '+')}",
                                )
                            )
                    
                    # Process organic search results
                    k = 3  # Limit results per search type
                    for i, result in enumerate(search_results.get("organic", [])[:k]):
                        texts = []
                        link = ""
                        if "snippet" in result:
                            texts.append(result["snippet"])
                        if "link" in result:
                            link = result["link"]
                        for attribute, value in result.get("attributes", {}).items():
                            texts.append(f"{attribute}: {value}.")
                        snippets.append(CitedSnippet(len(snippets) + 1, "\n".join(texts), link))
                        
        except Exception as e:
            logger.exception(f"Error in search: {str(e)}")
            
        return snippets
