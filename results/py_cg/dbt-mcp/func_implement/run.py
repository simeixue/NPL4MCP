# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_cli/tools.py
# module: src.dbt_mcp.dbt_cli.tools
# qname: src.dbt_mcp.dbt_cli.tools.create_dbt_cli_tool_definitions.run
# lines: 130-147
    def run(
        selector: str | None = Field(
            default=None, description=get_prompt("dbt_cli/args/selectors")
        ),
        is_full_refresh: bool | None = Field(
            default=None, description=get_prompt("dbt_cli/args/full_refresh")
        ),
        vars: str | None = Field(
            default=None, description=get_prompt("dbt_cli/args/vars")
        ),
    ) -> str:
        return _run_dbt_command(
            ["run"],
            selector,
            is_selectable=True,
            is_full_refresh=is_full_refresh,
            vars=vars,
        )