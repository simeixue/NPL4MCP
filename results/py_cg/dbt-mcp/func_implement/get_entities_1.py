# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/tools.py
# module: src.dbt_mcp.semantic_layer.tools
# qname: src.dbt_mcp.semantic_layer.tools.create_sl_tool_definitions.get_entities
# lines: 52-58
    def get_entities(
        metrics: list[str], search: str | None = None
    ) -> list[EntityToolResponse] | str:
        try:
            return semantic_layer_fetcher.get_entities(metrics=metrics, search=search)
        except Exception as e:
            return str(e)