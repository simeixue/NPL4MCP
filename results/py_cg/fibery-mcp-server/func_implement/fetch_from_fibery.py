# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.fetch_from_fibery
# lines: 136-174
    async def fetch_from_fibery(
        self,
        url: str,
        method: str = "GET",
        json_data: Any = None,
        params: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        Generic function to fetch data from Fibery API

        Args:
            url: API endpoint path
            method: HTTP method
            params: Query parameters
            json_data: JSON body of the request

        Returns:
            Response data and metadata
        """

        base_url = f"https://{self.__fibery_host}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.__fibery_api_token}",
        }

        async with httpx.AsyncClient(base_url=base_url, headers=headers, timeout=30.0) as client:
            if method == "GET":
                response = await client.get(url, params=params)
            elif method == "POST":
                response = await client.post(url, json=json_data, params=params)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()

            return {
                "data": response.json() if response.content else None,
            }