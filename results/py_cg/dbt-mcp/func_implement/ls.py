# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_cli/tools.py
# module: src.dbt_mcp.dbt_cli.tools
# qname: src.dbt_mcp.dbt_cli.tools.create_dbt_cli_tool_definitions.ls
# lines: 111-125
    def ls(
        selector: str | None = Field(
            default=None, description=get_prompt("dbt_cli/args/selectors")
        ),
        resource_type: list[str] | None = Field(
            default=None,
            description=get_prompt("dbt_cli/args/resource_type"),
        ),
    ) -> str:
        return _run_dbt_command(
            ["list"],
            selector,
            resource_type=resource_type,
            is_selectable=True,
        )