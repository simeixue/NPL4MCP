# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_missing_required_host_error
# lines: 218-228
    def test_missing_required_host_error(self):
        env_vars = {
            "DBT_PROD_ENV_ID": "123",
            "DBT_TOKEN": "test_token",
            "DISABLE_SEMANTIC_LAYER": "false",
        }

        with pytest.raises(
            ValueError, match="DBT_HOST environment variable is required"
        ):
            self._load_config_with_env(env_vars)