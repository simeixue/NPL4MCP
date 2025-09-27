# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_oos_tools.py
# module: tests.tools.test_oos_tools
# qname: tests.tools.test_oos_tools.test_create_client_exception
# lines: 90-94
def test_create_client_exception():
    with patch('alibaba_cloud_ops_mcp_server.tools.oos_tools.create_config', side_effect=Exception('fail')):
        with pytest.raises(Exception) as e:
            oos_tools.create_client('cn-test')
        assert 'fail' in str(e.value)