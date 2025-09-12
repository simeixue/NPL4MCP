# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.setup_method
# lines: 130-154
    def setup_method(self):
        # Clear any existing environment variables that might interfere
        env_vars_to_clear = [
            "DBT_HOST",
            "DBT_MCP_HOST",
            "DBT_PROD_ENV_ID",
            "DBT_ENV_ID",
            "DBT_DEV_ENV_ID",
            "DBT_USER_ID",
            "DBT_TOKEN",
            "DBT_PROJECT_DIR",
            "DBT_PATH",
            "DBT_CLI_TIMEOUT",
            "DISABLE_DBT_CLI",
            "DISABLE_SEMANTIC_LAYER",
            "DISABLE_DISCOVERY",
            "DISABLE_REMOTE",
            "DISABLE_ADMIN_API",
            "MULTICELL_ACCOUNT_PREFIX",
            "DBT_WARN_ERROR_OPTIONS",
            "DISABLE_TOOLS",
            "DBT_ACCOUNT_ID",
        ]
        for var in env_vars_to_clear:
            os.environ.pop(var, None)