# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_invalid_host_starting_with_metadata
# lines: 291-306
    def test_invalid_host_starting_with_metadata(self):
        env_vars = {
            "DBT_HOST": "metadata.test.dbt.com",
            "DBT_PROD_ENV_ID": "123",
            "DBT_TOKEN": "test_token",
            "DISABLE_DISCOVERY": "false",
            "DISABLE_DBT_CLI": "true",
            "DISABLE_SEMANTIC_LAYER": "true",
            "DISABLE_REMOTE": "true",
        }

        with pytest.raises(
            ValueError,
            match="DBT_HOST must not start with 'metadata' or 'semantic-layer'",
        ):
            self._load_config_with_env(env_vars)