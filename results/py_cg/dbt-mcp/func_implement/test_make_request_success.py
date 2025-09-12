# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_make_request_success
# lines: 51-62
def test_make_request_success(mock_request, client):
    mock_response = Mock()
    mock_response.json.return_value = {"data": "test"}
    mock_response.raise_for_status.return_value = None
    mock_request.return_value = mock_response

    result = client._make_request("GET", "/test/endpoint")

    assert result == {"data": "test"}
    mock_request.assert_called_once_with(
        "GET", "https://cloud.getdbt.com/test/endpoint", headers=client.headers
    )