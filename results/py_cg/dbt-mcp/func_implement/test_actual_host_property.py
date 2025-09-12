# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestDbtMcpSettings.test_actual_host_property
# lines: 98-111
    def test_actual_host_property(self):
        with patch.dict(os.environ, {"DBT_HOST": "host1.com"}):
            settings = DbtMcpSettings(_env_file=None)
            assert settings.actual_host == "host1.com"

        with patch.dict(os.environ, {"DBT_MCP_HOST": "host2.com"}):
            settings = DbtMcpSettings(_env_file=None)
            assert settings.actual_host == "host2.com"

        with patch.dict(
            os.environ, {"DBT_HOST": "host1.com", "DBT_MCP_HOST": "host2.com"}
        ):
            settings = DbtMcpSettings(_env_file=None)
            assert settings.actual_host == "host1.com"  # DBT_HOST takes precedence