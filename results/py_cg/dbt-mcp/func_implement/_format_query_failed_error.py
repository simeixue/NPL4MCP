# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/client.py
# module: src.dbt_mcp.semantic_layer.client
# qname: src.dbt_mcp.semantic_layer.client.SemanticLayerFetcher._format_query_failed_error
# lines: 262-268
    def _format_query_failed_error(self, query_error: Exception) -> QueryMetricsError:
        if isinstance(query_error, QueryFailedError):
            return QueryMetricsError(
                error=self._format_semantic_layer_error(query_error)
            )
        else:
            return QueryMetricsError(error=str(query_error))