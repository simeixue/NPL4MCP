# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.ensure_notebook_exists
# lines: 117-124
def ensure_notebook_exists(filepath: str, title: str = "New Notebook") -> dict:
    """Ensure a notebook exists, creating it if necessary."""
    resolved_path = resolve_path(filepath)
    
    if not os.path.exists(resolved_path):
        return create_new_notebook(resolved_path, title)
    
    return get_notebook_content(resolved_path)