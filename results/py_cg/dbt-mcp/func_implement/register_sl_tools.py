# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/tools.py
# module: src.dbt_mcp.semantic_layer.tools
# qname: src.dbt_mcp.semantic_layer.tools.register_sl_tools
# lines: 158-174
def register_sl_tools(
    dbt_mcp: FastMCP,
    config: SemanticLayerConfig,
    exclude_tools: Sequence[ToolName] = [],
) -> None:
    register_tools(
        dbt_mcp,
        create_sl_tool_definitions(
            config,
            SyncSemanticLayerClient(
                environment_id=config.prod_environment_id,
                auth_token=config.service_token,
                host=config.host,
            ),
        ),
        exclude_tools,
    )