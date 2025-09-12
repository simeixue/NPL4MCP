# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.client_with_prefix
# lines: 37-38
def client_with_prefix(admin_config_with_prefix):
    return DbtAdminAPIClient(admin_config_with_prefix)