# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/client.py
# module: src.dbt_mcp.semantic_layer.client
# qname: src.dbt_mcp.semantic_layer.client.SemanticLayerFetcher._format_semantic_layer_error
# lines: 192-208
    def _format_semantic_layer_error(self, error: Exception) -> str:
        """Format semantic layer errors by cleaning up common error message patterns."""
        error_str = str(error)
        return (
            error_str.replace("QueryFailedError(", "")
            .rstrip(")")
            .lstrip("[")
            .rstrip("]")
            .lstrip('"')
            .rstrip('"')
            .replace("INVALID_ARGUMENT: [FlightSQL]", "")
            .replace("(InvalidArgument; Prepare)", "")
            .replace("(InvalidArgument; ExecuteQuery)", "")
            .replace("Failed to prepare statement:", "")
            .replace("com.dbt.semanticlayer.exceptions.DataPlatformException:", "")
            .strip()
        )