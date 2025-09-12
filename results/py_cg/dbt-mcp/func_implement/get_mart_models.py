# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/tools.py
# module: src.dbt_mcp.discovery.tools
# qname: src.dbt_mcp.discovery.tools.create_discovery_tool_definitions.get_mart_models
# lines: 29-36
    def get_mart_models() -> list[dict] | str:
        try:
            mart_models = models_fetcher.fetch_models(
                model_filter={"modelingLayer": "marts"}
            )
            return [m for m in mart_models if m["name"] != "metricflow_time_spine"]
        except Exception as e:
            return str(e)