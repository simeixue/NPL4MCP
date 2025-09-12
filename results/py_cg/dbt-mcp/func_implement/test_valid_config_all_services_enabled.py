# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_valid_config_all_services_enabled
# lines: 172-200
    def test_valid_config_all_services_enabled(self):
        env_vars = {
            "DBT_HOST": "test.dbt.com",
            "DBT_PROD_ENV_ID": "123",
            "DBT_DEV_ENV_ID": "456",
            "DBT_USER_ID": "789",
            "DBT_ACCOUNT_ID": "123",
            "DBT_TOKEN": "test_token",
            "DBT_PROJECT_DIR": "/test/project",
            "DISABLE_SEMANTIC_LAYER": "false",
            "DISABLE_DISCOVERY": "false",
            "DISABLE_REMOTE": "false",
            "DISABLE_ADMIN_API": "false",
        }

        config = self._load_config_with_env(env_vars)

        assert config.tracking_config.host == "test.dbt.com"
        assert config.tracking_config.prod_environment_id == 123
        assert config.sql_config is not None
        assert config.sql_config.host == "test.dbt.com"
        assert config.dbt_cli_config is not None
        assert config.discovery_config is not None
        assert config.semantic_layer_config is not None
        assert config.admin_api_config is not None
        assert config.admin_api_config.url == "https://test.dbt.com"
        assert config.admin_api_config.headers == {"Authorization": "Bearer test_token"}
        assert config.admin_api_config.account_id == 123
        assert config.admin_api_config.prod_environment_id == 123