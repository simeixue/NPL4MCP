# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig._load_config_with_env
# lines: 156-170
    def _load_config_with_env(self, env_vars):
        """Helper method to load config with test environment variables, avoiding .env file interference"""
        with (
            patch.dict(os.environ, env_vars),
            patch("dbt_mcp.config.config.DbtMcpSettings") as mock_settings_class,
            patch(
                "dbt_mcp.config.config.detect_binary_type",
                return_value=BinaryType.DBT_CORE,
            ),
        ):
            # Create a real instance with test values, but without .env file loading
            with patch.dict(os.environ, env_vars, clear=True):
                settings_instance = DbtMcpSettings(_env_file=None)
            mock_settings_class.return_value = settings_instance
            return load_config()