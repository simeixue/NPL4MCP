# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/bump_version.py
# module: scripts.bump_version
# qname: scripts.bump_version.update_chart_yaml
# lines: 70-77
def update_chart_yaml(file_path: Path, new_version: str) -> None:
    """Update version in Chart.yaml."""
    content = file_path.read_text()
    # Update version: ...
    new_content = re.sub(r"version:\s*[\d.]+", f"version: {new_version}", content)
    # Update appVersion: ...
    new_content = re.sub(r'appVersion:\s*"[^"]*"', f'appVersion: "{new_version}"', new_content)
    file_path.write_text(new_content)