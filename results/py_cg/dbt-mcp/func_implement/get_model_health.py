# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/tools.py
# module: src.dbt_mcp.discovery.tools
# qname: src.dbt_mcp.discovery.tools.create_discovery_tool_definitions.get_model_health
# lines: 68-74
    def get_model_health(
        model_name: str | None = None, unique_id: str | None = None
    ) -> list[dict] | str:
        try:
            return models_fetcher.fetch_model_health(model_name, unique_id)
        except Exception as e:
            return str(e)