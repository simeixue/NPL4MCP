# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/server.py
# module: src.semgrep_mcp.server
# qname: src.semgrep_mcp.server.get_semgrep_scan_args
# lines: 196-215
def get_semgrep_scan_args(temp_dir: str, config: str | None = None) -> list[str]:
    """
    Builds command arguments for semgrep scan

    Args:
        temp_dir: Path to temporary directory containing the files
        config: Optional Semgrep configuration (e.g. "auto" or absolute path to rule file)

    Returns:
        List of command arguments
    """

    # Build command arguments and just run semgrep scan
    # if no config is provided to allow for either the default "auto"
    # or whatever the logged in config is
    args = ["scan", "--json", "--experimental"]  # avoid the extra exec
    if config:
        args.extend(["--config", config])
    args.append(temp_dir)
    return args