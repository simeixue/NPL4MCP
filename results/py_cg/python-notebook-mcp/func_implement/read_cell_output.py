# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.read_cell_output
# lines: 490-523
def read_cell_output(filepath: str, cell_index: int) -> List[Dict]:
    """
    Read output from a specific cell.
    
    Note: You must call initialize_workspace() first with your project directory.
    
    Args:
        filepath: Path to the notebook file
        cell_index: Index of the cell
    
    Returns:
        The cell's output
    """
    check_workspace_initialized()
    
    try:
        nb = get_notebook_content(filepath)
    except FileNotFoundError:
        nb = create_new_notebook(filepath)
        return []  # New notebook has no outputs
    
    if cell_index < 0 or cell_index >= len(nb.cells):
        raise IndexError(f"Cell index out of range: {cell_index}, notebook has {len(nb.cells)} cells")
    
    cell = nb.cells[cell_index]
    
    if cell.cell_type != 'code' or not hasattr(cell, 'outputs') or not cell.outputs:
        return []
    
    outputs = []
    for output in cell.outputs:
        outputs.append(process_cell_output(output))
    
    return outputs