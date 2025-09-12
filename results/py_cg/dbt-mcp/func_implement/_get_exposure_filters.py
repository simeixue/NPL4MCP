# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/client.py
# module: src.dbt_mcp.discovery.client
# qname: src.dbt_mcp.discovery.client.ExposuresFetcher._get_exposure_filters
# lines: 520-530
    def _get_exposure_filters(
        self, exposure_name: str | None = None, unique_ids: list[str] | None = None
    ) -> dict[str, list[str]]:
        if unique_ids:
            return {"uniqueIds": unique_ids}
        elif exposure_name:
            raise ValueError(
                "ExposureFilter only supports uniqueIds. Please use unique_ids parameter instead of exposure_name."
            )
        else:
            raise ValueError("unique_ids must be provided for exposure filtering")