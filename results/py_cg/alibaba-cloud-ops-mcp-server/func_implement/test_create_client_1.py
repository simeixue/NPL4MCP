# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_client
# lines: 372-377
def test_create_client(mock_client, mock_create_config):
    from alibaba_cloud_ops_mcp_server.tools import api_tools
    mock_create_config.return_value = MagicMock()
    mock_client.return_value = 'client_obj'
    result = api_tools.create_client('ecs', 'cn-hangzhou')
    assert result == 'client_obj'