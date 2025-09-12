# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp_calculate_server/server.py
# module: server
# qname: server.handle_equation_solving
# lines: 133-143
def handle_equation_solving(expression, locals_dict):
    """Handle system of equations solving expressions"""
    try:
        # Compute result
        result = eval(expression, globals(), locals_dict)

        # Format result
        return format_result(result)

    except Exception as e:
        return f"Equation solving error: {e}"