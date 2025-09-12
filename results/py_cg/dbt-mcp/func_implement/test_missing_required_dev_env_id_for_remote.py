# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_missing_required_dev_env_id_for_remote
# lines: 253-265
    def test_missing_required_dev_env_id_for_remote(self):
        env_vars = {
            "DBT_HOST": "test.dbt.com",
            "DBT_PROD_ENV_ID": "123",
            "DBT_TOKEN": "test_token",
            "DBT_USER_ID": "789",
            "DISABLE_REMOTE": "false",
        }

        with pytest.raises(
            ValueError, match="DBT_DEV_ENV_ID environment variable is required"
        ):
            self._load_config_with_env(env_vars)