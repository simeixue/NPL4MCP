# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.admin_config_with_prefix
# lines: 23-28
def admin_config_with_prefix():
    return AdminApiConfig(
        account_id=12345,
        headers={"Authorization": "Bearer test_token"},
        url="https://eu1.cloud.getdbt.com",
    )