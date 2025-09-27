# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/utils.py
# module: src.oxylabs_mcp.utils
# qname: src.oxylabs_mcp.utils._OxylabsClientWrapper.scrape
# lines: 152-167
    async def scrape(self, payload: dict[str, typing.Any]) -> dict[str, typing.Any]:
        await self._ctx.info(f"Create job with params: {json.dumps(payload)}")

        response = await self._client.post(settings.OXYLABS_SCRAPER_URL, json=payload)
        response_json: dict[str, typing.Any] = response.json()

        if response.status_code == status.HTTP_201_CREATED:
            await self._ctx.info(
                f"Job info: "
                f"job_id={response_json['job']['id']} "
                f"job_status={response_json['job']['status']}"
            )

        response.raise_for_status()

        return response_json