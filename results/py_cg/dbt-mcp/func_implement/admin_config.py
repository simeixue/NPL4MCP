# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.admin_config
# lines: 14-19
def admin_config():
    return AdminApiConfig(
        account_id=12345,
        headers={"Authorization": "Bearer test_token"},
        url="https://cloud.getdbt.com",
    )