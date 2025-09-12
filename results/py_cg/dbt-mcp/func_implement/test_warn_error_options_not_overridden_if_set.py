# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_warn_error_options_not_overridden_if_set
# lines: 404-421
    def test_warn_error_options_not_overridden_if_set(self):
        env_vars = {
            "DBT_WARN_ERROR_OPTIONS": "custom_options",
            "DISABLE_DBT_CLI": "true",
            "DISABLE_SEMANTIC_LAYER": "true",
            "DISABLE_DISCOVERY": "true",
            "DISABLE_REMOTE": "true",
            "DISABLE_ADMIN_API": "true",
        }

        # For this test, we need to call load_config directly to see environment side effects
        with patch.dict(os.environ, env_vars, clear=True):
            with patch("dbt_mcp.config.config.DbtMcpSettings") as mock_settings_class:
                settings_instance = DbtMcpSettings(_env_file=None)
                mock_settings_class.return_value = settings_instance
                load_config()

                assert os.environ["DBT_WARN_ERROR_OPTIONS"] == "custom_options"