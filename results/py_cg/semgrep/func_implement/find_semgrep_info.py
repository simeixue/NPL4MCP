# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/utils.py
# module: src.semgrep_mcp.utilities.utils
# qname: src.semgrep_mcp.utilities.utils.find_semgrep_info
# lines: 64-120
def find_semgrep_info() -> tuple[str | None, str]:
    """
    Dynamically find semgrep in PATH or common installation directories
    Returns: Path to semgrep executable and version or (None, "unknown") if not found
    """
    # Common paths where semgrep might be installed
    common_paths = [
        "semgrep",  # Default PATH
        "/usr/local/bin/semgrep",
        "/usr/bin/semgrep",
        "/opt/homebrew/bin/semgrep",  # Homebrew on macOS
        "/opt/semgrep/bin/semgrep",
        "/home/linuxbrew/.linuxbrew/bin/semgrep",  # Homebrew on Linux
        "/snap/bin/semgrep",  # Snap on Linux
    ]

    if SEMGREP_PATH:
        common_paths.append(SEMGREP_PATH)

    # Add Windows paths if on Windows
    if os.name == "nt":
        app_data = os.environ.get("APPDATA", "")
        if app_data:
            common_paths.extend(
                [
                    os.path.join(app_data, "Python", "Scripts", "semgrep.exe"),
                    os.path.join(app_data, "npm", "semgrep.cmd"),
                ]
            )

    # Try each path
    for semgrep_path in common_paths:
        # For 'semgrep' (without path), check if it's in PATH
        if semgrep_path == "semgrep":
            try:
                process = subprocess.run(
                    [semgrep_path, "--version"], check=True, capture_output=True, text=True
                )
                return semgrep_path, process.stdout.strip()
            except (subprocess.SubprocessError, FileNotFoundError):
                continue

        # For absolute paths, check if the file exists before testing
        if os.path.isabs(semgrep_path):
            if not os.path.exists(semgrep_path):
                continue

            # Try executing semgrep at this path
            try:
                process = subprocess.run(
                    [semgrep_path, "--version"], check=True, capture_output=True, text=True
                )
                return semgrep_path, process.stdout.strip()
            except (subprocess.SubprocessError, FileNotFoundError):
                continue

    return None, "unknown"