# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_remote_requirements
# lines: 457-487
    def test_remote_requirements(self):
        # Test that remote_config is only created when remote tools are enabled
        # and all required fields are present
        env_vars = {
            "DBT_HOST": "test.dbt.com",
            "DBT_PROD_ENV_ID": "123",
            "DBT_TOKEN": "test_token",
            "DISABLE_REMOTE": "true",
            "DISABLE_DBT_CLI": "true",
            "DISABLE_SEMANTIC_LAYER": "true",
            "DISABLE_DISCOVERY": "true",
            "DISABLE_ADMIN_API": "true",
        }

        config = self._load_config_with_env(env_vars)
        # Remote config should not be created when remote tools are disabled
        assert config.sql_config is None

        # Test remote requirements (needs user_id and dev_env_id too)
        env_vars.update(
            {
                "DBT_USER_ID": "789",
                "DBT_DEV_ENV_ID": "456",
                "DISABLE_REMOTE": "false",
            }
        )

        config = self._load_config_with_env(env_vars)
        assert config.sql_config is not None
        assert config.sql_config.user_id == 789
        assert config.sql_config.dev_environment_id == 456