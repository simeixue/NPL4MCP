# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/examples/openai_agent/main_streamable.py
# module: examples.openai_agent.main_streamable
# qname: examples.openai_agent.main_streamable.print_tool_call
# lines: 13-26
def print_tool_call(tool_name, params, color="yellow", show_params=True):
    # Define color codes for different colors
    # we could use a library like colorama but this avoids adding a dependency
    color_codes = {
        "grey": "\033[37m",
        "yellow": "\033[93m",
    }
    color_code_reset = "\033[0m"

    color_code = color_codes.get(color, color_codes["yellow"])
    msg = f"Calling the tool {tool_name}"
    if show_params:
        msg += f" with params {params}"
    print(f"{color_code}# {msg}{color_code_reset}")