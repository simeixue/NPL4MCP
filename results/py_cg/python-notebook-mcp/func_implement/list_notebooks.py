# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.list_notebooks
# lines: 328-342
def list_notebooks(directory: str = ".") -> List[str]:
    """
    List all notebook files in the specified directory.
    
    Note: You must call initialize_workspace() first.
    """
    check_workspace_initialized()
    
    resolved_directory = resolve_path(directory)
    notebook_files = []
    
    for path in Path(resolved_directory).rglob('*.ipynb'):
        notebook_files.append(str(path))
    
    return notebook_files