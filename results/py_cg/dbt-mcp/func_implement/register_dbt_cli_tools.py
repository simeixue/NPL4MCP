# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_cli/tools.py
# module: src.dbt_mcp.dbt_cli.tools
# qname: src.dbt_mcp.dbt_cli.tools.register_dbt_cli_tools
# lines: 266-275
def register_dbt_cli_tools(
    dbt_mcp: FastMCP,
    config: DbtCliConfig,
    exclude_tools: Sequence[ToolName] = [],
) -> None:
    register_tools(
        dbt_mcp,
        create_dbt_cli_tool_definitions(config),
        exclude_tools,
    )