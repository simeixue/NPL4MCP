# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/scripts/release.py
# module: scripts.release
# qname: scripts.release.gen_version
# lines: 119-122
def gen_version() -> Version:
    """Generate version based on current date"""
    now = datetime.datetime.now()
    return Version(f"{now.year}.{now.month}.{now.day}")