# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_cms_tools.py
# module: tests.tools.test_cms_tools
# qname: tests.tools.test_cms_tools.test_create_client_exception
# lines: 76-80
def test_create_client_exception():
    with patch('alibaba_cloud_ops_mcp_server.tools.cms_tools.create_config', side_effect=Exception('fail')):
        with pytest.raises(Exception) as e:
            cms_tools.create_client('cn-test')
        assert 'fail' in str(e.value)