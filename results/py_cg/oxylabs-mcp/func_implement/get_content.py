# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/utils.py
# module: src.oxylabs_mcp.utils
# qname: src.oxylabs_mcp.utils.get_content
# lines: 288-305
def get_content(
    response_json: dict[str, typing.Any],
    *,
    output_format: str,
    parse: bool = False,
) -> str:
    """Extract content from response and convert to a proper format."""
    content = response_json["results"][0]["content"]
    if parse and isinstance(content, dict):
        return json.dumps(content)
    if output_format == "html":
        return str(content)
    if output_format == "links":
        links = extract_links_with_text(str(content))
        return "\n".join(links)

    stripped_html = strip_html(str(content))
    return markdownify(stripped_html)  # type: ignore[no-any-return]