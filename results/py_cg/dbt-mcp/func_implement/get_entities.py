# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/client.py
# module: src.dbt_mcp.semantic_layer.client
# qname: src.dbt_mcp.semantic_layer.client.SemanticLayerFetcher.get_entities
# lines: 114-138
    def get_entities(
        self, metrics: list[str], search: str | None = None
    ) -> list[EntityToolResponse]:
        metrics_key = ",".join(sorted(metrics))
        if metrics_key not in self.entities_cache:
            entities_result = submit_request(
                self.config,
                {
                    "query": GRAPHQL_QUERIES["entities"],
                    "variables": {
                        "metrics": [{"name": m} for m in metrics],
                        "search": search,
                    },
                },
            )
            entities = [
                EntityToolResponse(
                    name=e.get("name"),
                    type=e.get("type"),
                    description=e.get("description"),
                )
                for e in entities_result["data"]["entitiesPaginated"]["items"]
            ]
            self.entities_cache[metrics_key] = entities
        return self.entities_cache[metrics_key]