# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/scripts/release.py
# module: scripts.release
# qname: scripts.release.generate_version
# lines: 179-182
def generate_version() -> int:
    # Detect package type
    click.echo(gen_version())
    return 0