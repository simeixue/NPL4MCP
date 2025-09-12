# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_empty_environment_variables
# lines: 337-348
    def test_empty_environment_variables(self):
        env_vars = {
            "DBT_HOST": "",
            "DBT_PROD_ENV_ID": "123",
            "DBT_TOKEN": "test_token",
            "DISABLE_DISCOVERY": "false",
        }

        with pytest.raises(
            ValueError, match="DBT_HOST environment variable is required"
        ):
            self._load_config_with_env(env_vars)