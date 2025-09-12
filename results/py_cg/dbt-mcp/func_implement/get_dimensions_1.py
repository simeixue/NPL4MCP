# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/tools.py
# module: src.dbt_mcp.semantic_layer.tools
# qname: src.dbt_mcp.semantic_layer.tools.create_sl_tool_definitions.get_dimensions
# lines: 44-50
    def get_dimensions(
        metrics: list[str], search: str | None = None
    ) -> list[DimensionToolResponse] | str:
        try:
            return semantic_layer_fetcher.get_dimensions(metrics=metrics, search=search)
        except Exception as e:
            return str(e)