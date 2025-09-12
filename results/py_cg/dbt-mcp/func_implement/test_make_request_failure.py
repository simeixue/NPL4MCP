# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_make_request_failure
# lines: 66-74
def test_make_request_failure(mock_request, client):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "404 Not Found"
    )
    mock_request.return_value = mock_response

    with pytest.raises(AdminAPIError):
        client._make_request("GET", "/test/endpoint")