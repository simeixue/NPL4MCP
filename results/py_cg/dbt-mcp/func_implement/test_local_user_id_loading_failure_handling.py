# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_local_user_id_loading_failure_handling
# lines: 442-455
    def test_local_user_id_loading_failure_handling(self):
        env_vars = {
            "HOME": "/fake/home",
            "DISABLE_DBT_CLI": "true",
            "DISABLE_SEMANTIC_LAYER": "true",
            "DISABLE_DISCOVERY": "true",
            "DISABLE_REMOTE": "true",
            "DISABLE_ADMIN_API": "true",
        }

        with patch.dict(os.environ, env_vars):
            with patch("pathlib.Path.exists", return_value=False):
                config = self._load_config_with_env(env_vars)
                assert config.tracking_config.local_user_id is None