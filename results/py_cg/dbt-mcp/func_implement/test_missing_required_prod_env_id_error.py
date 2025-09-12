# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_missing_required_prod_env_id_error
# lines: 230-240
    def test_missing_required_prod_env_id_error(self):
        env_vars = {
            "DBT_HOST": "test.dbt.com",
            "DBT_TOKEN": "test_token",
            "DISABLE_DISCOVERY": "false",
        }

        with pytest.raises(
            ValueError, match="DBT_PROD_ENV_ID environment variable is required"
        ):
            self._load_config_with_env(env_vars)