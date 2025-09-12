# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/tools/test_tool_names.py
# module: tests.unit.tools.test_tool_names
# qname: tests.unit.tools.test_tool_names.test_tool_names_no_duplicates
# lines: 47-49
def test_tool_names_no_duplicates():
    """Test that there are no duplicate tool names in the enum."""
    assert len(ToolName.get_all_tool_names()) == len(set(ToolName.get_all_tool_names()))