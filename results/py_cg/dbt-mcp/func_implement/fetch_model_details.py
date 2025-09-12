# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/client.py
# module: src.dbt_mcp.discovery.client
# qname: src.dbt_mcp.discovery.client.ModelsFetcher.fetch_model_details
# lines: 398-414
    def fetch_model_details(
        self, model_name: str | None = None, unique_id: str | None = None
    ) -> dict:
        model_filters = self._get_model_filters(model_name, unique_id)
        variables = {
            "environmentId": self.environment_id,
            "modelsFilter": model_filters,
            "first": 1,
        }
        result = self.api_client.execute_query(
            GraphQLQueries.GET_MODEL_DETAILS, variables
        )
        raise_gql_error(result)
        edges = result["data"]["environment"]["applied"]["models"]["edges"]
        if not edges:
            return {}
        return edges[0]["node"]