# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/client.py
# module: src.dbt_mcp.discovery.client
# qname: src.dbt_mcp.discovery.client.MetadataAPIClient.__init__
# lines: 324-326
    def __init__(self, *, url: str, headers: dict[str, str]):
        self.url = url
        self.headers = headers