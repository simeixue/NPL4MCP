# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_case_insensitive_environment_variables
# lines: 571-584
    def test_case_insensitive_environment_variables(self):
        # pydantic_settings should handle case insensitivity based on config
        env_vars = {
            "dbt_host": "test.dbt.com",  # lowercase
            "DBT_PROD_ENV_ID": "123",  # uppercase
            "dbt_token": "test_token",  # lowercase
            "DISABLE_DISCOVERY": "false",
            "DISABLE_DBT_CLI": "true",
            "DISABLE_SEMANTIC_LAYER": "true",
            "DISABLE_REMOTE": "true",
        }

        config = self._load_config_with_env(env_vars)
        assert config.tracking_config.host == "test.dbt.com"