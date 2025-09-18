# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.read_cell
# lines: 391-415
def read_cell(filepath: str, cell_index: int) -> Dict:
    """
    Read a specific cell from a notebook.
    
    Note: You must call initialize_workspace() first with your project directory.
    
    Args:
        filepath: Path to the notebook file
        cell_index: Index of the cell to read
    
    Returns:
        The cell content
    """
    check_workspace_initialized()
    
    try:
        nb = get_notebook_content(filepath)
    except FileNotFoundError:
        nb = create_new_notebook(filepath)
    
    if cell_index < 0 or cell_index >= len(nb.cells):
        raise IndexError(f"Cell index out of range: {cell_index}, notebook has {len(nb.cells)} cells")
    
    cell = nb.cells[cell_index]
    return cell_to_dict(cell)