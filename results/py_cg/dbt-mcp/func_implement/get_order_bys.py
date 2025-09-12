# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/client.py
# module: src.dbt_mcp.semantic_layer.client
# qname: src.dbt_mcp.semantic_layer.client.SemanticLayerFetcher.get_order_bys
# lines: 270-295
    def get_order_bys(
        self,
        order_by: list[OrderByParam],
        metrics: list[str],
        group_by: list[GroupByParam] | None = None,
    ) -> list[OrderBySpec]:
        result: list[OrderBySpec] = []
        queried_group_by = {g.name: g for g in group_by} if group_by else {}
        queried_metrics = set(metrics)
        for o in order_by:
            if o.name in queried_metrics:
                result.append(OrderByMetric(name=o.name, descending=o.descending))
            elif o.name in queried_group_by:
                selected_group_by = queried_group_by[o.name]
                result.append(
                    OrderByGroupBy(
                        name=selected_group_by.name,
                        descending=o.descending,
                        grain=selected_group_by.grain,
                    )
                )
            else:
                raise ValueError(
                    f"Order by `{o.name}` not found in metrics or group by"
                )
        return result