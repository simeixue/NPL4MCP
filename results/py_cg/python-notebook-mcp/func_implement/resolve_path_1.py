# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.resolve_path
# lines: 76-83
def resolve_path(path: str) -> str:
    """Resolve relative paths against the workspace directory."""
    if os.path.isabs(path):
        return path
    
    # Try to resolve against the workspace directory
    resolved_path = os.path.join(WORKSPACE_DIR, path)
    return resolved_path