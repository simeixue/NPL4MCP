# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestLoadConfig.test_missing_required_project_dir_for_cli
# lines: 281-289
    def test_missing_required_project_dir_for_cli(self):
        env_vars = {
            "DISABLE_DBT_CLI": "false",
        }

        with pytest.raises(
            ValueError, match="DBT_PROJECT_DIR environment variable is required"
        ):
            self._load_config_with_env(env_vars)