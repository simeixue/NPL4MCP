# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.add_cell
# lines: 526-570
def add_cell(filepath: str, content: str, cell_type: str = "code", index: Optional[int] = None) -> str:
    """
    Add a new cell to a notebook.
    
    Note: You must call initialize_workspace() first with your project directory.
    
    Args:
        filepath: Path to the notebook file
        content: Content for the new cell
        cell_type: Type of cell ('code' or 'markdown')
        index: Position to insert the cell (None for append)
    
    Returns:
        Confirmation message
    """
    check_workspace_initialized()
    
    try:
        nb = get_notebook_content(filepath)
    except FileNotFoundError:
        nb = create_new_notebook(filepath)
    
    if cell_type.lower() == 'code':
        new_cell = new_code_cell(content)
    elif cell_type.lower() == 'markdown':
        new_cell = new_markdown_cell(content)
    else:
        raise ValueError(f"Invalid cell type: {cell_type}. Must be 'code' or 'markdown'")
    
    if index is None:
        nb.cells.append(new_cell)
        position = len(nb.cells) - 1
    else:
        if index < 0 or index > len(nb.cells):
            raise IndexError(f"Cell index out of range: {index}, notebook has {len(nb.cells)} cells")
        nb.cells.insert(index, new_cell)
        position = index
    
    try:
        resolved_path = resolve_path(filepath)
        with open(resolved_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        return f"Added {cell_type} cell at position {position} in {resolved_path}"
    except Exception as e:
        raise Exception(f"Failed to update notebook: {str(e)}")