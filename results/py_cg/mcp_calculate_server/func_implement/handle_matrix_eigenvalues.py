# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp_calculate_server/server.py
# module: server
# qname: server.handle_matrix_eigenvalues
# lines: 145-165
def handle_matrix_eigenvalues(expression, locals_dict):
    """Handle matrix eigenvalue calculation expressions"""
    try:
        # Extract matrix expression
        matrix_expr = expression.split(".eigen")[0]
        operation = "eigenvals" if "eigenvals" in expression else "eigenvects"

        # Compute matrix
        matrix = eval(matrix_expr, globals(), locals_dict)

        # Compute eigenvalues or eigenvectors
        if operation == "eigenvals":
            result = matrix.eigenvals()
        else:
            result = matrix.eigenvects()

        # Format result
        return format_result(result)

    except Exception as e:
        return f"Matrix eigenvalue calculation error: {e}"