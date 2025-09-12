# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/tools.py
# module: src.dbt_mcp.semantic_layer.tools
# qname: src.dbt_mcp.semantic_layer.tools.create_sl_tool_definitions.get_metrics_compiled_sql
# lines: 82-102
    def get_metrics_compiled_sql(
        metrics: list[str],
        group_by: list[GroupByParam] | None = None,
        order_by: list[OrderByParam] | None = None,
        where: str | None = None,
        limit: int | None = None,
    ) -> str:
        try:
            result = semantic_layer_fetcher.get_metrics_compiled_sql(
                metrics=metrics,
                group_by=group_by,
                order_by=order_by,
                where=where,
                limit=limit,
            )
            if isinstance(result, GetMetricsCompiledSqlSuccess):
                return result.sql
            else:
                return result.error
        except Exception as e:
            return str(e)