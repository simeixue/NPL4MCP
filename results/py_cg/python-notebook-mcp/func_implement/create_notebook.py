# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.create_notebook
# lines: 345-366
def create_notebook(filepath: str, title: str = "New Notebook") -> str:
    """
    Create a new Jupyter notebook.
    
    Note: You must call initialize_workspace() first with your project directory.
    
    Args:
        filepath: Path where the notebook should be created
        title: Title for the notebook (used in the first markdown cell)
    
    Returns:
        Path to the created notebook
    """
    check_workspace_initialized()
    
    resolved_path = resolve_path(filepath)
    
    if os.path.exists(resolved_path):
        return f"Notebook already exists at {resolved_path}"
    
    create_new_notebook(filepath, title)
    return f"Created notebook at {resolved_path}"