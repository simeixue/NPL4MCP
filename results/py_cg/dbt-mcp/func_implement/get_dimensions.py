# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/client.py
# module: src.dbt_mcp.semantic_layer.client
# qname: src.dbt_mcp.semantic_layer.client.SemanticLayerFetcher.get_dimensions
# lines: 84-112
    def get_dimensions(
        self, metrics: list[str], search: str | None = None
    ) -> list[DimensionToolResponse]:
        metrics_key = ",".join(sorted(metrics))
        if metrics_key not in self.dimensions_cache:
            dimensions_result = submit_request(
                self.config,
                {
                    "query": GRAPHQL_QUERIES["dimensions"],
                    "variables": {
                        "metrics": [{"name": m} for m in metrics],
                        "search": search,
                    },
                },
            )
            dimensions = []
            for d in dimensions_result["data"]["dimensionsPaginated"]["items"]:
                dimensions.append(
                    DimensionToolResponse(
                        name=d.get("name"),
                        type=d.get("type"),
                        description=d.get("description"),
                        label=d.get("label"),
                        granularities=d.get("queryableGranularities")
                        + d.get("queryableTimeGranularities"),
                    )
                )
            self.dimensions_cache[metrics_key] = dimensions
        return self.dimensions_cache[metrics_key]