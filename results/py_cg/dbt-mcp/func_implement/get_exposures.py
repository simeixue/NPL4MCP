# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/tools.py
# module: src.dbt_mcp.discovery.tools
# qname: src.dbt_mcp.discovery.tools.create_discovery_tool_definitions.get_exposures
# lines: 76-80
    def get_exposures() -> list[dict] | str:
        try:
            return exposures_fetcher.fetch_exposures()
        except Exception as e:
            return str(e)