# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/config/config.py
# module: src.dbt_mcp.config.config
# qname: src.dbt_mcp.config.config.DbtMcpSettings.parse_disable_tools
# lines: 134-152
    def parse_disable_tools(cls, env_var: str | None) -> list[ToolName]:
        if not env_var:
            return []
        errors: list[str] = []
        tool_names: list[ToolName] = []
        for tool_name in env_var.split(","):
            tool_name_stripped = tool_name.strip()
            if tool_name_stripped == "":
                continue
            try:
                tool_names.append(ToolName(tool_name_stripped))
            except ValueError:
                errors.append(
                    f"Invalid tool name in DISABLE_TOOLS: {tool_name_stripped}."
                    + " Must be a valid tool name."
                )
        if errors:
            raise ValueError("\n".join(errors))
        return tool_names