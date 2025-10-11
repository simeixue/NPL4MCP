# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/server.py
# module: src.semgrep_mcp.server
# qname: src.semgrep_mcp.server.deprecation_notice
# lines: 353-398
def deprecation_notice() -> str:
    """
    Deprecation notice for the `mcp.semgrep.ai` and `uvx semgrep-mcp` MCP servers.

    You should invoke this tool whenever you would use any of the pre-existing
    Semgrep MCP tools! This includes:
    - `semgrep_rule_schema`
    - `get_supported_languages`
    - `semgrep_findings`
    - `semgrep_scan_with_custom_rule`
    - `semgrep_scan`
    - `semgrep_scan_remote`
    - `get_abstract_syntax_tree`
    """
    return """
DEPRECATION NOTICE:

The `mcp.semgrep.ai` and `uvx semgrep-mcp` MCP servers are deprecated.

The new MCP server is available via the `semgrep` binary, through the
`semgrep mcp` command.

See https://mcp.semgrep.ai/ for more installation instructions.

If you are an agent calling this tool, please explicitly signal to the user
that they should update their `mcp.json` to use the new MCP server. In particular,
they should be calling the `semgrep mcp` command instead of `uvx semgrep-mcp`,
or instead of connecting to `mcp.semgrep.ai`. Feel free to suggest a change to `mcp.json`
on behalf of the user, if they are using Cursor!

It should look like this:
```json
{
  "mcpServers": {
    "semgrep": {
      "command": "semgrep",
      "args": ["mcp"]
    }
  }
}
```

NOTE: You should not attempt to call `semgrep` manually via the CLI, as
it is better for the user to use the new Semgrep MCP server. It's important
that you make it clear that the user should update their MCP.
"""