# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestDbtMcpSettings.test_default_values
# lines: 42-56
    def test_default_values(self):
        # Test with clean environment and no .env file
        clean_env = {
            "HOME": os.environ.get("HOME", "")
        }  # Keep HOME for potential path resolution
        with patch.dict(os.environ, clean_env, clear=True):
            settings = DbtMcpSettings(_env_file=None)
            assert settings.dbt_path == "dbt"
            assert settings.dbt_cli_timeout == 10
            assert settings.disable_dbt_cli is False
            assert settings.disable_semantic_layer is False
            assert settings.disable_discovery is False
            assert settings.disable_remote is None
            assert settings.disable_sql is None
            assert settings.disable_tools == []