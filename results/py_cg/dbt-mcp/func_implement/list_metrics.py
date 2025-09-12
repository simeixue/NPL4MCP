# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/client.py
# module: src.dbt_mcp.semantic_layer.client
# qname: src.dbt_mcp.semantic_layer.client.SemanticLayerFetcher.list_metrics
# lines: 68-82
    def list_metrics(self, search: str | None = None) -> list[MetricToolResponse]:
        metrics_result = submit_request(
            self.config,
            {"query": GRAPHQL_QUERIES["metrics"], "variables": {"search": search}},
        )
        return [
            MetricToolResponse(
                name=m.get("name"),
                type=m.get("type"),
                label=m.get("label"),
                description=m.get("description"),
                metadata=(m.get("config") or {}).get("meta", ""),
            )
            for m in metrics_result["data"]["metricsPaginated"]["items"]
        ]