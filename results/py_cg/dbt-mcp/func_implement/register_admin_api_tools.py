# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/tools.py
# module: src.dbt_mcp.dbt_admin.tools
# qname: src.dbt_mcp.dbt_admin.tools.register_admin_api_tools
# lines: 277-288
def register_admin_api_tools(
    dbt_mcp: FastMCP,
    admin_config: AdminApiConfig,
    exclude_tools: Sequence[ToolName] = [],
) -> None:
    """Register dbt Admin API tools."""
    admin_client = DbtAdminAPIClient(admin_config)
    register_tools(
        dbt_mcp,
        create_admin_api_tool_definitions(admin_client, admin_config),
        exclude_tools,
    )