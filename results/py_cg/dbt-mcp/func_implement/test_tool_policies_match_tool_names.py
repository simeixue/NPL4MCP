# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/tools/test_tool_policies.py
# module: tests.unit.tools.test_tool_policies
# qname: tests.unit.tools.test_tool_policies.test_tool_policies_match_tool_names
# lines: 39-47
def test_tool_policies_match_tool_names():
    policy_names = {policy.upper() for policy in tool_policies}
    tool_names = {tool.name for tool in ToolName}
    if tool_names != policy_names:
        raise ValueError(
            f"Tool name mismatch:\n"
            f"In tool names but not in policy: {tool_names - policy_names}\n"
            f"In policy but not in tool names: {policy_names - tool_names}"
        )