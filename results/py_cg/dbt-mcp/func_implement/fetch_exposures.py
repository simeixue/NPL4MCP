# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/client.py
# module: src.dbt_mcp.discovery.client
# qname: src.dbt_mcp.discovery.client.ExposuresFetcher.fetch_exposures
# lines: 493-518
    def fetch_exposures(self) -> list[dict]:
        has_next_page = True
        after_cursor: str | None = None
        all_edges: list[dict] = []

        while has_next_page:
            variables: dict[str, int | str] = {
                "environmentId": self.environment_id,
                "first": PAGE_SIZE,
            }
            if after_cursor:
                variables["after"] = after_cursor

            result = self.api_client.execute_query(
                GraphQLQueries.GET_EXPOSURES, variables
            )
            new_edges = self._parse_response_to_json(result)
            all_edges.extend(new_edges)

            page_info = result["data"]["environment"]["definition"]["exposures"][
                "pageInfo"
            ]
            has_next_page = page_info.get("hasNextPage", False)
            after_cursor = page_info.get("endCursor")

        return all_edges