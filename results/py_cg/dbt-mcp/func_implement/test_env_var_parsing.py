# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestDbtMcpSettings.test_env_var_parsing
# lines: 58-79
    def test_env_var_parsing(self):
        env_vars = {
            "DBT_HOST": "test.dbt.com",
            "DBT_PROD_ENV_ID": "123",
            "DBT_TOKEN": "test_token",
            "DBT_PROJECT_DIR": "/test/project",
            "DISABLE_DBT_CLI": "true",
            "DISABLE_TOOLS": "build,compile,docs",
        }

        with patch.dict(os.environ, env_vars):
            settings = DbtMcpSettings(_env_file=None)
            assert settings.dbt_host == "test.dbt.com"
            assert settings.dbt_prod_env_id == 123
            assert settings.dbt_token == "test_token"
            assert settings.dbt_project_dir == "/test/project"
            assert settings.disable_dbt_cli is True
            assert settings.disable_tools == [
                ToolName.BUILD,
                ToolName.COMPILE,
                ToolName.DOCS,
            ]