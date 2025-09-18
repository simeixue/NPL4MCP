# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.edit_cell
# lines: 418-451
def edit_cell(filepath: str, cell_index: int, content: str) -> str:
    """
    Edit a specific cell in a notebook.
    
    Note: You must call initialize_workspace() first with your project directory.
    
    Args:
        filepath: Path to the notebook file
        cell_index: Index of the cell to edit
        content: New content for the cell
    
    Returns:
        Confirmation message
    """
    check_workspace_initialized()
    
    try:
        nb = get_notebook_content(filepath)
    except FileNotFoundError:
        nb = create_new_notebook(filepath)
    
    if cell_index < 0 or cell_index >= len(nb.cells):
        raise IndexError(f"Cell index out of range: {cell_index}, notebook has {len(nb.cells)} cells")
    
    cell = nb.cells[cell_index]
    cell['source'] = content
    
    try:
        resolved_path = resolve_path(filepath)
        with open(resolved_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        return f"Updated cell {cell_index} in {resolved_path}"
    except Exception as e:
        raise Exception(f"Failed to update notebook: {str(e)}")