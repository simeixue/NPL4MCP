# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/client.py
# module: src.dbt_mcp.dbt_admin.client
# qname: src.dbt_mcp.dbt_admin.client.DbtAdminAPIClient.__init__
# lines: 21-26
    def __init__(self, config: AdminApiConfig):
        self.config = config
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        } | config.headers