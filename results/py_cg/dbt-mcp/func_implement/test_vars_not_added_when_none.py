# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_cli/test_tools.py
# module: tests.unit.dbt_cli.test_tools
# qname: tests.unit.dbt_cli.test_tools.test_vars_not_added_when_none
# lines: 299-316
def test_vars_not_added_when_none(monkeypatch: MonkeyPatch, mock_process, mock_fastmcp):
    mock_calls = []

    def mock_popen(args, **kwargs):
        mock_calls.append(args)
        return mock_process

    monkeypatch.setattr("subprocess.Popen", mock_popen)

    fastmcp, tools = mock_fastmcp
    register_dbt_cli_tools(fastmcp, mock_dbt_cli_config)
    build_tool = tools["build"]

    build_tool()  # Non-explicit

    assert mock_calls
    args_list = mock_calls[0]
    assert "--vars" not in args_list