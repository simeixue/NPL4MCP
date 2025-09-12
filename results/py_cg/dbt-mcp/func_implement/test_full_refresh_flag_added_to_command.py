# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.test_full_refresh_flag_added_to_command
# lines: 253-272
def test_full_refresh_flag_added_to_command(
    monkeypatch: MonkeyPatch, mock_process, mock_fastmcp, command_name
):
    mock_calls = []

    def mock_popen(args, **kwargs):
        mock_calls.append(args)
        return mock_process

    monkeypatch.setattr("subprocess.Popen", mock_popen)

    fastmcp, tools = mock_fastmcp
    register_dbt_cli_tools(fastmcp, mock_dbt_cli_config)
    tool = tools[command_name]

    tool(is_full_refresh=True)

    assert mock_calls
    args_list = mock_calls[0]
    assert "--full-refresh" in args_list