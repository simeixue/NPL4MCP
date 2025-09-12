# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/tools.py
# module: src.dbt_mcp.discovery.tools
# qname: src.dbt_mcp.discovery.tools.create_discovery_tool_definitions.get_exposure_details
# lines: 82-88
    def get_exposure_details(
        exposure_name: str | None = None, unique_ids: list[str] | None = None
    ) -> list[dict] | str:
        try:
            return exposures_fetcher.fetch_exposure_details(exposure_name, unique_ids)
        except Exception as e:
            return str(e)