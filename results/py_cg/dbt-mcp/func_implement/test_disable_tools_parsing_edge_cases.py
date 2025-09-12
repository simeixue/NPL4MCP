# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/config/test_config.py
# module: tests.unit.config.test_config
# qname: tests.unit.config.test_config.TestDbtMcpSettings.test_disable_tools_parsing_edge_cases
# lines: 81-96
    def test_disable_tools_parsing_edge_cases(self):
        test_cases = [
            ("build,compile,docs", [ToolName.BUILD, ToolName.COMPILE, ToolName.DOCS]),
            (
                "build, compile , docs",
                [ToolName.BUILD, ToolName.COMPILE, ToolName.DOCS],
            ),
            ("build,,docs", [ToolName.BUILD, ToolName.DOCS]),
            ("", []),
            ("run", [ToolName.RUN]),
        ]

        for input_val, expected in test_cases:
            with patch.dict(os.environ, {"DISABLE_TOOLS": input_val}):
                settings = DbtMcpSettings(_env_file=None)
                assert settings.disable_tools == expected