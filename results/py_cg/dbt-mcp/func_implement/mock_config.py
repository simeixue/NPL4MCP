# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_tools.py
# module: tests.unit.dbt_admin.test_tools
# qname: tests.unit.dbt_admin.test_tools.mock_config
# lines: 23-30
def mock_config(mock_admin_config):
    from tests.mocks.config import mock_tracking_config

    return Config(
        tracking_config=mock_tracking_config,
        admin_api_config=mock_admin_config,
        disable_tools=[],
    )