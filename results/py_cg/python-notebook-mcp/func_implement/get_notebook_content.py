# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.get_notebook_content
# lines: 85-94
def get_notebook_content(filepath: str) -> dict:
    """Read a notebook file and return its content."""
    resolved_path = resolve_path(filepath)
    
    if not os.path.exists(resolved_path):
        raise FileNotFoundError(f"Notebook file not found: {resolved_path}")
    
    with open(resolved_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    return nb