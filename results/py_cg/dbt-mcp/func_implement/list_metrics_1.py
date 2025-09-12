# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/tools.py
# module: src.dbt_mcp.semantic_layer.tools
# qname: src.dbt_mcp.semantic_layer.tools.create_sl_tool_definitions.list_metrics
# lines: 38-42
    def list_metrics(search: str | None = None) -> list[MetricToolResponse] | str:
        try:
            return semantic_layer_fetcher.list_metrics(search=search)
        except Exception as e:
            return str(e)