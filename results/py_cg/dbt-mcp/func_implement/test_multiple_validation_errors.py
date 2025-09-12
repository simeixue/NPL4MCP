# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_multiple_validation_errors
# lines: 536-553
    def test_multiple_validation_errors(self):
        # Test that multiple validation errors are collected and reported
        env_vars = {
            "DISABLE_DISCOVERY": "false",
            "DISABLE_REMOTE": "false",
            "DISABLE_DBT_CLI": "false",
        }

        with pytest.raises(ValueError) as exc_info:
            self._load_config_with_env(env_vars)

        error_message = str(exc_info.value)
        assert "DBT_HOST environment variable is required" in error_message
        assert "DBT_PROD_ENV_ID environment variable is required" in error_message
        assert "DBT_TOKEN environment variable is required" in error_message
        assert "DBT_DEV_ENV_ID environment variable is required" in error_message
        assert "DBT_USER_ID environment variable is required" in error_message
        assert "DBT_PROJECT_DIR environment variable is required" in error_message