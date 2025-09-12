# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_missing_required_token_error
# lines: 242-251
    def test_missing_required_token_error(self):
        env_vars = {
            "DBT_HOST": "test.dbt.com",
            "DBT_PROD_ENV_ID": "123",
        }

        with pytest.raises(
            ValueError, match="DBT_TOKEN environment variable is required"
        ):
            self._load_config_with_env(env_vars)