# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.temp_dir
# lines: 7-9
def temp_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)