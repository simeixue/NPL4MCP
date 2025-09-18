# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.check_workspace_initialized
# lines: 322-325
def check_workspace_initialized() -> None:
    """Check if workspace is initialized and raise error if not."""
    if not WORKSPACE_INITIALIZED:
        raise ValueError("ERROR: Workspace not initialized. Please call initialize_workspace() first with the FULL ABSOLUTE PATH to the directory where your notebook files are located.")