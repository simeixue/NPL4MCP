# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/server.py
# module: src.semgrep_mcp.server
# qname: src.semgrep_mcp.server.safe_join
# lines: 77-105
def safe_join(base_dir: str, untrusted_path: str) -> str:
    """
    Joins a base directory with an untrusted relative path and ensures the final path
    doesn't escape the base directory.

    Args:
        base_dir: The base directory to join the untrusted path to
        untrusted_path: The untrusted relative path to join to the base directory
    """
    # Absolute, normalized path to the base directory
    base_path = Path(base_dir).resolve()

    # Handle empty path, current directory, or paths with only slashes
    if not untrusted_path or untrusted_path == "." or untrusted_path.strip("/") == "":
        return base_path.as_posix()

    # Ensure untrusted path is not absolute
    # This is soft validation, path traversal is checked later
    if Path(untrusted_path).is_absolute():
        raise ValueError("Untrusted path must be relative")

    # Join and normalize the untrusted path
    full_path = base_path / Path(untrusted_path)

    # Ensure the final path doesn't escape the base directory
    if not full_path == full_path.resolve():
        raise ValueError(f"Untrusted path escapes the base directory!: {untrusted_path}")

    return full_path.as_posix()