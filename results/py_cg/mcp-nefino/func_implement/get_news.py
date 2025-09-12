# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/client.py
# module: src.mcp_nefino.client
# qname: src.mcp_nefino.client.NefinoClient.get_news
# lines: 28-66
    async def get_news(
        self,
        place_id: str,
        place_type: str,
        range_or_recency: str | None = None,
        last_n_days: int | None = None,
        date_range_begin: str | None = None,
        date_range_end: str | None = None,
        news_topics: list[str] | None = None,
    ) -> dict[str, Any]:
        """Get news items for a place with optional filtering."""
        headers = {"Authorization": f"Bearer {self.token}"}

        payload = {
            "place_id": place_id,
            "place_type": place_type,
        }

        # Add optional parameters if provided
        if range_or_recency:
            payload["range_or_recency"] = range_or_recency
        if last_n_days:
            payload["last_n_days"] = last_n_days
        if date_range_begin:
            payload["date_range_begin"] = date_range_begin
        if date_range_end:
            payload["date_range_end"] = date_range_end
        if news_topics:
            payload["news_topics"] = news_topics

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/get_news", headers=headers, json=payload
            ) as response:
                if response.status != 200:
                    text = await response.text()
                    raise Exception(f"Error: {response.status} - {text}")
                
                return await response.json()