# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_disable_flags_combinations
# lines: 489-534
    def test_disable_flags_combinations(self):
        base_env = {
            "DBT_HOST": "test.dbt.com",
            "DBT_PROD_ENV_ID": "123",
            "DBT_TOKEN": "test_token",
            "DBT_PROJECT_DIR": "/test",
        }

        test_cases = [
            # Only CLI enabled
            {
                "DISABLE_DBT_CLI": "false",
                "DISABLE_SEMANTIC_LAYER": "true",
                "DISABLE_DISCOVERY": "true",
                "DISABLE_REMOTE": "true",
            },
            # Only semantic layer enabled
            {
                "DISABLE_DBT_CLI": "true",
                "DISABLE_SEMANTIC_LAYER": "false",
                "DISABLE_DISCOVERY": "true",
                "DISABLE_REMOTE": "true",
            },
            # Multiple services enabled
            {
                "DISABLE_DBT_CLI": "false",
                "DISABLE_SEMANTIC_LAYER": "false",
                "DISABLE_DISCOVERY": "false",
                "DISABLE_REMOTE": "true",
            },
        ]

        for disable_flags in test_cases:
            env_vars = {**base_env, **disable_flags}
            config = self._load_config_with_env(env_vars)

            # Verify configs are created only when services are enabled
            assert (config.dbt_cli_config is not None) == (
                disable_flags["DISABLE_DBT_CLI"] == "false"
            )
            assert (config.semantic_layer_config is not None) == (
                disable_flags["DISABLE_SEMANTIC_LAYER"] == "false"
            )
            assert (config.discovery_config is not None) == (
                disable_flags["DISABLE_DISCOVERY"] == "false"
            )