# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_multicell_account_prefix_configurations
# lines: 350-365
    def test_multicell_account_prefix_configurations(self):
        env_vars = {
            "DBT_HOST": "test.dbt.com",
            "DBT_PROD_ENV_ID": "123",
            "DBT_TOKEN": "test_token",
            "MULTICELL_ACCOUNT_PREFIX": "prefix",
            "DISABLE_DISCOVERY": "false",
            "DISABLE_SEMANTIC_LAYER": "false",
            "DISABLE_DBT_CLI": "true",
            "DISABLE_REMOTE": "true",
        }

        config = self._load_config_with_env(env_vars)

        assert "prefix.metadata.test.dbt.com" in config.discovery_config.url
        assert config.semantic_layer_config.host == "prefix.semantic-layer.test.dbt.com"