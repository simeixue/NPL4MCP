# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_invalid_environment_variable_types
# lines: 325-335
    def test_invalid_environment_variable_types(self):
        # Test invalid integer types
        env_vars = {
            "DBT_HOST": "test.dbt.com",
            "DBT_PROD_ENV_ID": "not_an_integer",
            "DBT_TOKEN": "test_token",
            "DISABLE_DISCOVERY": "false",
        }

        with pytest.raises(ValueError):
            self._load_config_with_env(env_vars)