# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/unit/test_utils.py
# module: tests.unit.test_utils
# qname: tests.unit.test_utils.test_extract_links_with_text
# lines: 65-70
def test_extract_links_with_text(html_input: str, expected_output: str):
    with (open(TEST_FIXTURES + html_input, "r", encoding="utf-8") as input_file,):
        input_html = input_file.read()

        links = extract_links_with_text(input_html)
        assert "\n".join(links) == expected_output