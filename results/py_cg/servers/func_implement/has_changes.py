# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/scripts/release.py
# module: scripts.release
# qname: scripts.release.has_changes
# lines: 101-116
def has_changes(path: Path, git_hash: GitHash) -> bool:
    """Check if any files changed between current state and git hash"""
    try:
        output = subprocess.run(
            ["git", "diff", "--name-only", git_hash, "--", "."],
            cwd=path,
            check=True,
            capture_output=True,
            text=True,
        )

        changed_files = [Path(f) for f in output.stdout.splitlines()]
        relevant_files = [f for f in changed_files if f.suffix in [".py", ".ts"]]
        return len(relevant_files) >= 1
    except subprocess.CalledProcessError:
        return False