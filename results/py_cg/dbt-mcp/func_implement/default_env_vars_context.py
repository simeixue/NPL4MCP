# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/env_vars.py
# module: tests.env_vars
# qname: tests.env_vars.default_env_vars_context
# lines: 29-45
def default_env_vars_context(override_env_vars: dict[str, str] | None = None):
    with env_vars_context(
        {
            "DBT_HOST": "http://localhost:8000",
            "DBT_PROD_ENV_ID": "1234",
            "DBT_TOKEN": "5678",
            "DBT_PROJECT_DIR": "tests/fixtures/dbt_project",
            "DBT_PATH": "dbt",
            "DBT_DEV_ENV_ID": "5678",
            "DBT_USER_ID": "9012",
            "DBT_CLI_TIMEOUT": "10",
            "DBT_ACCOUNT_ID": "12345",
            "DISABLE_TOOLS": "",
        }
        | (override_env_vars or {})
    ):
        yield