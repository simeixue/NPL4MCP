# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/tools/test_tool_policies.py
# module: tests.unit.tools.test_tool_policies
# qname: tests.unit.tools.test_tool_policies.test_tool_policies_no_duplicates
# lines: 50-52
def test_tool_policies_no_duplicates():
    """Test that there are no duplicate tool names in the policy."""
    assert len(tool_policies) == len(set(tool_policies.keys()))