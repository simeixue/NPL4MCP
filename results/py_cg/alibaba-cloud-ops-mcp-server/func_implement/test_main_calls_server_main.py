# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/test_init.py
# module: tests.test_init
# qname: tests.test_init.test_main_calls_server_main
# lines: 5-8
def test_main_calls_server_main():
    with patch('alibaba_cloud_ops_mcp_server.server.main', new_callable=AsyncMock) as mock_main:
        alibaba_cloud_ops_mcp_server.main()
        mock_main.assert_awaited_once()