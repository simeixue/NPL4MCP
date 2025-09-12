# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_cli/binary_type.py
# module: src.dbt_mcp.dbt_cli.binary_type
# qname: src.dbt_mcp.dbt_cli.binary_type.detect_binary_type
# lines: 10-43
def detect_binary_type(file_path: str) -> BinaryType:
    """
    Detect the type of dbt binary (dbt Core, Fusion, or dbt Cloud CLI) by inspecting the binary content.
    Based on the logic from insp.py for minimal detection of pip-installed Python, Go, and Rust.

    Args:
        file_path: Path to the dbt executable

    Returns:
        BinaryType: The detected binary type

    Raises:
        Exception: If the binary file cannot be read or accessed
    """
    try:
        with open(file_path, "rb") as f:
            content = f.read(1024 * 1024)
    except Exception as e:
        raise Exception(f"Cannot read binary file {file_path}: {e}")

    # Python: Check shebang or Python-specific strings (dbt Core)
    if content.startswith(b"#!/") and b"python" in content[:100].lower():
        return BinaryType.DBT_CORE

    # Windows Python executables from pip (dbt Core)
    if b"__main__.py" in content or b"PYTHONPATH" in content:
        return BinaryType.DBT_CORE

    # Go build ID (dbt Cloud CLI)
    if b"Go build ID:" in content:
        return BinaryType.DBT_CLOUD_CLI

    # Default to Fusion for everything else (Rust)
    return BinaryType.FUSION