# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/oauth/test_fastapi_app_pagination.py
# module: tests.unit.oauth.test_fastapi_app_pagination
# qname: tests.unit.oauth.test_fastapi_app_pagination.account
# lines: 18-26
def account():
    return DbtPlatformAccount(
        id=1,
        name="Account 1",
        locked=False,
        state=1,
        static_subdomain=None,
        vanity_subdomain=None,
    )