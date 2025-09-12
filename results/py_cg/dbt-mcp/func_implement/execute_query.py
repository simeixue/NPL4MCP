# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/client.py
# module: src.dbt_mcp.discovery.client
# qname: src.dbt_mcp.discovery.client.MetadataAPIClient.execute_query
# lines: 328-334
    def execute_query(self, query: str, variables: dict) -> dict:
        response = requests.post(
            url=self.url,
            json={"query": query, "variables": variables},
            headers=self.headers,
        )
        return response.json()