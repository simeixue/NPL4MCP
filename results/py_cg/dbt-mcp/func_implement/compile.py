# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_cli/tools.py
# module: src.dbt_mcp.dbt_cli.tools
# qname: src.dbt_mcp.dbt_cli.tools.create_dbt_cli_tool_definitions.compile
# lines: 105-106
    def compile() -> str:
        return _run_dbt_command(["compile"])