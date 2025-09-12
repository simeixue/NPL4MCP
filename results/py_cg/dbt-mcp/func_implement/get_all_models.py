# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/tools.py
# module: src.dbt_mcp.discovery.tools
# qname: src.dbt_mcp.discovery.tools.create_discovery_tool_definitions.get_all_models
# lines: 38-42
    def get_all_models() -> list[dict] | str:
        try:
            return models_fetcher.fetch_models()
        except Exception as e:
            return str(e)