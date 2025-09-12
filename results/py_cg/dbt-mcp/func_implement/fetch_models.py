# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/client.py
# module: src.dbt_mcp.discovery.client
# qname: src.dbt_mcp.discovery.client.ModelsFetcher.fetch_models
# lines: 373-396
    def fetch_models(self, model_filter: ModelFilter | None = None) -> list[dict]:
        has_next_page = True
        after_cursor: str = ""
        all_edges: list[dict] = []
        while has_next_page and len(all_edges) < MAX_NUM_MODELS:
            variables = {
                "environmentId": self.environment_id,
                "after": after_cursor,
                "first": PAGE_SIZE,
                "modelsFilter": model_filter or {},
                "sort": {"field": "queryUsageCount", "direction": "desc"},
            }

            result = self.api_client.execute_query(GraphQLQueries.GET_MODELS, variables)
            all_edges.extend(self._parse_response_to_json(result))

            previous_after_cursor = after_cursor
            after_cursor = result["data"]["environment"]["applied"]["models"][
                "pageInfo"
            ]["endCursor"]
            if previous_after_cursor == after_cursor:
                has_next_page = False

        return all_edges