# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestDbtMcpSettings.test_actual_prod_environment_id_property
# lines: 113-126
    def test_actual_prod_environment_id_property(self):
        with patch.dict(os.environ, {"DBT_PROD_ENV_ID": "123"}):
            settings = DbtMcpSettings(_env_file=None)
            assert settings.actual_prod_environment_id == 123

        with patch.dict(os.environ, {"DBT_ENV_ID": "456"}):
            settings = DbtMcpSettings(_env_file=None)
            assert settings.actual_prod_environment_id == 456

        with patch.dict(os.environ, {"DBT_PROD_ENV_ID": "123", "DBT_ENV_ID": "456"}):
            settings = DbtMcpSettings(_env_file=None)
            assert (
                settings.actual_prod_environment_id == 123
            )  # DBT_PROD_ENV_ID takes precedence