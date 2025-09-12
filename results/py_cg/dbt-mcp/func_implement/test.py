# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_cli/tools.py
# module: src.dbt_mcp.dbt_cli.tools
# qname: src.dbt_mcp.dbt_cli.tools.create_dbt_cli_tool_definitions.test
# lines: 149-157
    def test(
        selector: str | None = Field(
            default=None, description=get_prompt("dbt_cli/args/selectors")
        ),
        vars: str | None = Field(
            default=None, description=get_prompt("dbt_cli/args/vars")
        ),
    ) -> str:
        return _run_dbt_command(["test"], selector, is_selectable=True, vars=vars)