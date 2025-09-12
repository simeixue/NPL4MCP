# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/client.py
# module: src.dbt_mcp.semantic_layer.client
# qname: src.dbt_mcp.semantic_layer.client.SemanticLayerFetcher.validate_query_metrics_params
# lines: 218-259
    def validate_query_metrics_params(
        self, metrics: list[str], group_by: list[GroupByParam] | None
    ) -> str | None:
        errors = []
        available_metrics_names = [m.name for m in self.list_metrics()]
        metric_misspellings = get_misspellings(
            targets=metrics,
            words=available_metrics_names,
            top_k=5,
        )
        for metric_misspelling in metric_misspellings:
            recommendations = (
                " Did you mean: " + ", ".join(metric_misspelling.similar_words) + "?"
            )
            errors.append(
                f"Metric {metric_misspelling.word} not found."
                + (recommendations if metric_misspelling.similar_words else "")
            )

        if errors:
            return f"Errors: {', '.join(errors)}"

        available_group_by = [d.name for d in self.get_dimensions(metrics)] + [
            e.name for e in self.get_entities(metrics)
        ]
        group_by_misspellings = get_misspellings(
            targets=[g.name for g in group_by or []],
            words=available_group_by,
            top_k=5,
        )
        for group_by_misspelling in group_by_misspellings:
            recommendations = (
                " Did you mean: " + ", ".join(group_by_misspelling.similar_words) + "?"
            )
            errors.append(
                f"Group by {group_by_misspelling.word} not found."
                + (recommendations if group_by_misspelling.similar_words else "")
            )

        if errors:
            return f"Errors: {', '.join(errors)}"
        return None