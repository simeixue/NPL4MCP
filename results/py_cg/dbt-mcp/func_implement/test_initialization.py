# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/integration/initialization/test_initialization.py
# module: tests.integration.initialization.test_initialization
# qname: tests.integration.initialization.test_initialization.test_initialization
# lines: 8-16
def test_initialization():
    with patch("dbt_mcp.config.config.load_config", return_value=mock_config):
        result = asyncio.run(create_dbt_mcp(mock_config))

    assert result is not None
    assert hasattr(result, "usage_tracker")

    tools = asyncio.run(result.list_tools())
    assert isinstance(tools, list)