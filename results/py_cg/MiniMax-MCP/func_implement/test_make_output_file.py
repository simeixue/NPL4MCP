# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/tests/test_utils.py
# module: tests.test_utils
# qname: tests.test_utils.test_make_output_file
# lines: 21-27
def test_make_output_file():
    tool = "test"
    text = "hello world"
    output_path = Path("/tmp")
    result = build_output_file(tool, text, output_path, "mp3")
    assert result.name.startswith("test_hello")
    assert result.suffix == ".mp3"