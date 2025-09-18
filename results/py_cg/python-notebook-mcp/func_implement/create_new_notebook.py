# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.create_new_notebook
# lines: 96-115
def create_new_notebook(filepath: str, title: str = "New Notebook") -> dict:
    """Create a new notebook file if it doesn't exist."""
    resolved_path = resolve_path(filepath)
    
    # Create directory if it doesn't exist
    directory = os.path.dirname(resolved_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    
    # Create a new notebook
    nb = new_notebook()
    nb.cells.append(new_markdown_cell(f"# {title}"))
    nb.cells.append(new_code_cell("# Your code here"))
    
    # Write the notebook to file
    with open(resolved_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    print(f"Created new notebook at: {resolved_path}")
    return nb