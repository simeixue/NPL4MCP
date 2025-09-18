# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.initialize_workspace
# lines: 269-320
def initialize_workspace(directory: str) -> str:
    """
    IMPORTANT: Call this first! Initialize the workspace directory for this session.
    
    This must be called before using any other tools to ensure notebooks are created
    in the correct location. You must provide a FULL ABSOLUTE PATH to your project folder
    where notebooks should be stored. Do not use relative paths.
    
    Args:
        directory: The FULL ABSOLUTE PATH to set as the workspace (required)
        
    Returns:
        Confirmation message with list of any notebooks found
    
    Raises:
        ValueError: If directory is not provided, doesn't exist, is not a directory, or is a relative path
    """
    global WORKSPACE_DIR, WORKSPACE_INITIALIZED
    
    if not directory or not directory.strip():
        raise ValueError("ERROR: You must provide a directory path. Please provide the FULL ABSOLUTE PATH to your project directory where notebook files are located.")
    
    # Convert Unix-style paths to Windows format
    directory = convert_unix_path(directory)
    
    # Check for relative paths
    if directory in [".", "./"] or directory.startswith("./") or directory.startswith("../"):
        raise ValueError("ERROR: Relative paths like '.' or './' are not allowed. Please provide the FULL ABSOLUTE PATH to your project directory.")
    
    # Check if directory exists
    if not os.path.exists(directory):
        raise ValueError(f"ERROR: Directory does not exist: {directory}")
    
    # Check if it's a directory
    if not os.path.isdir(directory):
        raise ValueError(f"ERROR: Not a directory: {directory}")
    
    # Set the workspace directory
    WORKSPACE_DIR = directory
    WORKSPACE_INITIALIZED = True
    print(f"Workspace initialized at: {WORKSPACE_DIR}")
    
    # List the notebooks in the workspace to confirm
    notebooks = []
    for path in Path(WORKSPACE_DIR).rglob('*.ipynb'):
        notebooks.append(os.path.relpath(path, WORKSPACE_DIR))
    
    if notebooks:
        notebook_list = "\n- " + "\n- ".join(notebooks)
        return f"Workspace initialized at: {WORKSPACE_DIR}\nNotebooks found:{notebook_list}"
    else:
        return f"Workspace initialized at: {WORKSPACE_DIR}\nNo notebooks found."