# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/client.py
# module: src.dbt_mcp.semantic_layer.client
# qname: src.dbt_mcp.semantic_layer.client.SemanticLayerFetcher._format_get_metrics_compiled_sql_error
# lines: 210-216
    def _format_get_metrics_compiled_sql_error(
        self, compile_error: Exception
    ) -> GetMetricsCompiledSqlError:
        """Format get compiled SQL errors using the shared error formatter."""
        return GetMetricsCompiledSqlError(
            error=self._format_semantic_layer_error(compile_error)
        )