# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/bump_version.py
# module: scripts.bump_version
# qname: scripts.bump_version.update_version_py
# lines: 43-50
def update_version_py(file_path: Path, new_version: str) -> None:
    """Update version in version.py."""
    content = file_path.read_text()
    # Update version pattern in version.py
    new_content = re.sub(
        r'__version__\s*=\s*["\'][\d.]+["\']', f'__version__ = "{new_version}"', content
    )
    file_path.write_text(new_content)