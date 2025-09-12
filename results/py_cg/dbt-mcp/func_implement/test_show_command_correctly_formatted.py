# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.test_show_command_correctly_formatted
# lines: 194-222
def test_show_command_correctly_formatted(
    monkeypatch: MonkeyPatch, mock_process, mock_fastmcp
):
    # Mock Popen
    mock_calls = []

    def mock_popen(args, **kwargs):
        mock_calls.append(args)
        return mock_process

    monkeypatch.setattr("subprocess.Popen", mock_popen)

    # Setup
    mock_fastmcp_obj, tools = mock_fastmcp
    register_dbt_cli_tools(mock_fastmcp_obj, mock_dbt_cli_config)
    show_tool = tools["show"]

    # Execute
    show_tool(sql_query="SELECT * FROM my_model")

    # Verify
    assert mock_calls
    args_list = mock_calls[0]
    assert args_list[0].endswith("dbt")
    assert args_list[1] == "--no-use-colors"
    assert args_list[2] == "show"
    assert args_list[3] == "--inline"
    assert args_list[4] == "SELECT * FROM my_model"
    assert args_list[5] == "--favor-state"