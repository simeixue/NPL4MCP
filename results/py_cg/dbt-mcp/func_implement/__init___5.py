# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/client.py
# module: src.dbt_mcp.discovery.client
# qname: src.dbt_mcp.discovery.client.ModelsFetcher.__init__
# lines: 342-344
    def __init__(self, api_client: MetadataAPIClient, environment_id: int):
        self.api_client = api_client
        self.environment_id = environment_id