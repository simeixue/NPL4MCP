# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/dbt_admin/test_client.py
# module: tests.unit.dbt_admin.test_client
# qname: tests.unit.dbt_admin.test_client.client
# lines: 32-33
def client(admin_config):
    return DbtAdminAPIClient(admin_config)