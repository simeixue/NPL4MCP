# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/client.py
# module: src.dbt_mcp.semantic_layer.client
# qname: src.dbt_mcp.semantic_layer.client.SemanticLayerFetcher.get_metrics_compiled_sql
# lines: 140-190
    def get_metrics_compiled_sql(
        self,
        metrics: list[str],
        group_by: list[GroupByParam] | None = None,
        order_by: list[OrderByParam] | None = None,
        where: str | None = None,
        limit: int | None = None,
    ) -> GetMetricsCompiledSqlResult:
        """
        Get compiled SQL for the given metrics and group by parameters using the SDK.

        Args:
            metrics: List of metric names to get compiled SQL for
            group_by: List of group by parameters (dimensions/entities with optional grain)
            order_by: List of order by parameters
            where: Optional SQL WHERE clause to filter results
            limit: Optional limit for number of results

        Returns:
            GetMetricsCompiledSqlResult with either the compiled SQL or an error
        """
        validation_error = self.validate_query_metrics_params(
            metrics=metrics,
            group_by=group_by,
        )
        if validation_error:
            return GetMetricsCompiledSqlError(error=validation_error)

        try:
            with self.sl_client.session():
                parsed_order_by: list[OrderBySpec] = (
                    self.get_order_bys(
                        order_by=order_by, metrics=metrics, group_by=group_by
                    )
                    if order_by is not None
                    else []
                )

                compiled_sql = self.sl_client.compile_sql(
                    metrics=metrics,
                    group_by=group_by,  # type: ignore
                    order_by=parsed_order_by,  # type: ignore
                    where=[where] if where else None,
                    limit=limit,
                    read_cache=True,
                )

                return GetMetricsCompiledSqlSuccess(sql=compiled_sql)

        except Exception as e:
            return self._format_get_metrics_compiled_sql_error(e)