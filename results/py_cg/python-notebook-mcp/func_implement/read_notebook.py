# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.read_notebook
# lines: 369-388
def read_notebook(filepath: str) -> Dict:
    """
    Read the contents of a notebook.
    
    Note: You must call initialize_workspace() first with your project directory.
    
    Args:
        filepath: Path to the notebook file
    
    Returns:
        The notebook content
    """
    check_workspace_initialized()
    
    try:
        nb = get_notebook_content(filepath)
    except FileNotFoundError:
        nb = create_new_notebook(filepath)
    
    return notebook_to_dict(nb)