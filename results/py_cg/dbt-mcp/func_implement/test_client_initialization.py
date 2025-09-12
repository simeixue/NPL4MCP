# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.test_client_initialization
# lines: 41-47
def test_client_initialization(client):
    assert client.config.account_id == 12345
    assert client.config.headers == {"Authorization": "Bearer test_token"}
    assert client.config.url == "https://cloud.getdbt.com"
    assert client.headers["Authorization"] == "Bearer test_token"
    assert client.headers["Content-Type"] == "application/json"
    assert client.headers["Accept"] == "application/json"