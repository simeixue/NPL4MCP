# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/alibabacloud/test_api_meta_client.py
# module: tests.alibabacloud.test_api_meta_client
# qname: tests.alibabacloud.test_api_meta_client.test_get_ref_api_meta_valid_path
# lines: 279-302
def test_get_ref_api_meta_valid_path(mock_pop_api, mock_std):
    # 模拟 get_response_from_pop_api 返回包含 defs/A 的结构
    mock_pop_api.return_value = {
        'defs': {
            'A': {
                'properties': {
                    'prop1': {'type': 'string'},
                    'prop2': {'type': 'integer'}
                }
            }
        }
    }

    # 调用 get_ref_api_meta，传入 $ref 指向 #/defs/A
    result = api_meta_client.ApiMetaClient.get_ref_api_meta({'$ref': '#/defs/A'}, 'ecs', '2014-05-26')

    # 验证返回结果是否与 defs/A 的结构一致
    expected = {
        'properties': {
            'prop1': {'type': 'string'},
            'prop2': {'type': 'integer'}
        }
    }
    assert result == expected