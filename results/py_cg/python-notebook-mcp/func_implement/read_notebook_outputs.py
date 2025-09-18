# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.read_notebook_outputs
# lines: 454-487
def read_notebook_outputs(filepath: str) -> List[Dict]:
    """
    Read all outputs from a notebook.
    
    Note: You must call initialize_workspace() first with your project directory.
    
    Args:
        filepath: Path to the notebook file
    
    Returns:
        List of all cell outputs
    """
    check_workspace_initialized()
    
    try:
        nb = get_notebook_content(filepath)
    except FileNotFoundError:
        nb = create_new_notebook(filepath)
        return []  # New notebook has no outputs
    
    outputs = []
    
    for i, cell in enumerate(nb.cells):
        if cell.cell_type == 'code' and hasattr(cell, 'outputs') and cell.outputs:
            cell_outputs = []
            for output in cell.outputs:
                cell_outputs.append(process_cell_output(output))
            
            outputs.append({
                'cell_index': i,
                'outputs': cell_outputs
            })
    
    return outputs