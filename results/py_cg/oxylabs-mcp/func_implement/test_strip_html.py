# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/unit/test_utils.py
# module: tests.unit.test_utils
# qname: tests.unit.test_utils.test_strip_html
# lines: 42-51
def test_strip_html(html_input: str, expected_output: str):
    with (
        open(TEST_FIXTURES + html_input, "r", encoding="utf-8") as input_file,
        open(TEST_FIXTURES + expected_output, "r", encoding="utf-8") as output_file,
    ):
        input_html = input_file.read()
        expected_html = output_file.read()

        actual_output = strip_html(input_html)
        assert actual_output == expected_html