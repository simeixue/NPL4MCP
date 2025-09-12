# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/tools.py
# module: src.dbt_mcp.discovery.tools
# qname: src.dbt_mcp.discovery.tools.register_discovery_tools
# lines: 174-183
def register_discovery_tools(
    dbt_mcp: FastMCP,
    config: DiscoveryConfig,
    exclude_tools: Sequence[ToolName] = [],
) -> None:
    register_tools(
        dbt_mcp,
        create_discovery_tool_definitions(config),
        exclude_tools,
    )