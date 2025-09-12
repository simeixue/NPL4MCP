# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/tools.py
# module: src.dbt_mcp.semantic_layer.tools
# qname: src.dbt_mcp.semantic_layer.tools.create_sl_tool_definitions.query_metrics
# lines: 60-80
    def query_metrics(
        metrics: list[str],
        group_by: list[GroupByParam] | None = None,
        order_by: list[OrderByParam] | None = None,
        where: str | None = None,
        limit: int | None = None,
    ) -> str:
        try:
            result = semantic_layer_fetcher.query_metrics(
                metrics=metrics,
                group_by=group_by,
                order_by=order_by,
                where=where,
                limit=limit,
            )
            if isinstance(result, QueryMetricsSuccess):
                return result.result
            else:
                return result.error
        except Exception as e:
            return str(e)