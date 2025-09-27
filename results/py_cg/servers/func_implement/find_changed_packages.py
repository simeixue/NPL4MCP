# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/scripts/release.py
# module: scripts.release
# qname: scripts.release.find_changed_packages
# lines: 125-131
def find_changed_packages(directory: Path, git_hash: GitHash) -> Iterator[Package]:
    for path in directory.glob("*/package.json"):
        if has_changes(path.parent, git_hash):
            yield NpmPackage(path.parent)
    for path in directory.glob("*/pyproject.toml"):
        if has_changes(path.parent, git_hash):
            yield PyPiPackage(path.parent)