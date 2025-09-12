# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/client.py
# module: src.dbt_mcp.semantic_layer.client
# qname: src.dbt_mcp.semantic_layer.client.SemanticLayerClientProtocol.query
# lines: 35-43
    def query(
        self,
        metrics: list[str],
        group_by: list[GroupByParam | str] | None = None,
        limit: int | None = None,
        order_by: list[str | OrderByGroupBy | OrderByMetric] | None = None,
        where: list[str] | None = None,
        read_cache: bool = True,
    ) -> pa.Table: ...