# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.convert_unix_path
# lines: 46-61
def convert_unix_path(path: str) -> str:
    """Convert Unix-style paths like /d/Projects to Windows-style paths (only on Windows)."""
    # Only perform conversion on Windows
    if sys.platform != 'win32':
        return path
        
    import re
    # Match pattern like /d/Projects/... or /c/Users/...
    match = re.match(r'^/([a-zA-Z])(/.*)?$', path)
    if match:
        drive_letter = match.group(1)
        remaining_path = match.group(2) or ''
        # Convert to Windows path (D:\\Projects\\...)
        windows_path = remaining_path.replace('/', '\\')
        return f"{drive_letter.upper()}:{windows_path}"
    return path