# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/client.py
# module: src.dbt_mcp.semantic_layer.client
# qname: src.dbt_mcp.semantic_layer.client.SemanticLayerFetcher.query_metrics
# lines: 297-340
    def query_metrics(
        self,
        metrics: list[str],
        group_by: list[GroupByParam] | None = None,
        order_by: list[OrderByParam] | None = None,
        where: str | None = None,
        limit: int | None = None,
    ) -> QueryMetricsResult:
        validation_error = self.validate_query_metrics_params(
            metrics=metrics,
            group_by=group_by,
        )
        if validation_error:
            return QueryMetricsError(error=validation_error)

        try:
            query_error = None
            with self.sl_client.session():
                # Catching any exception within the session
                # to ensure it is closed properly
                try:
                    parsed_order_by: list[OrderBySpec] = (
                        self.get_order_bys(
                            order_by=order_by, metrics=metrics, group_by=group_by
                        )
                        if order_by is not None
                        else []
                    )
                    query_result = self.sl_client.query(
                        metrics=metrics,
                        # TODO: remove this type ignore once this PR is merged: https://github.com/dbt-labs/semantic-layer-sdk-python/pull/80
                        group_by=group_by,  # type: ignore
                        order_by=parsed_order_by,  # type: ignore
                        where=[where] if where else None,
                        limit=limit,
                    )
                except Exception as e:
                    query_error = e
            if query_error:
                return self._format_query_failed_error(query_error)
            json_result = query_result.to_pandas().to_json(orient="records", indent=2)
            return QueryMetricsSuccess(result=json_result or "")
        except Exception as e:
            return self._format_query_failed_error(e)