# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_legacy_env_id_support
# lines: 555-569
    def test_legacy_env_id_support(self):
        # Test that DBT_ENV_ID still works for backward compatibility
        env_vars = {
            "DBT_HOST": "test.dbt.com",
            "DBT_ENV_ID": "123",  # Using legacy variable
            "DBT_TOKEN": "test_token",
            "DISABLE_DISCOVERY": "false",
            "DISABLE_DBT_CLI": "true",
            "DISABLE_SEMANTIC_LAYER": "true",
            "DISABLE_REMOTE": "true",
        }

        config = self._load_config_with_env(env_vars)
        assert config.tracking_config.prod_environment_id == 123
        assert config.discovery_config.environment_id == 123