# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.assert_text_content_response
# lines: 81-93
def assert_text_content_response(
    result: List[Any], expected_content: str = None
) -> str:
    """Common assertions for text content responses"""
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].type == "text"

    text = result[0].text
    if expected_content:
        assert expected_content in text

    return text