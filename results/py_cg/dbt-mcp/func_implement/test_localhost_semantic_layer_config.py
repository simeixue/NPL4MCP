# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_localhost_semantic_layer_config
# lines: 367-381
    def test_localhost_semantic_layer_config(self):
        env_vars = {
            "DBT_HOST": "localhost:8080",
            "DBT_PROD_ENV_ID": "123",
            "DBT_TOKEN": "test_token",
            "DISABLE_SEMANTIC_LAYER": "false",
            "DISABLE_DBT_CLI": "true",
            "DISABLE_DISCOVERY": "true",
            "DISABLE_REMOTE": "true",
        }

        config = self._load_config_with_env(env_vars)

        assert config.semantic_layer_config.url.startswith("http://")
        assert "localhost:8080" in config.semantic_layer_config.url