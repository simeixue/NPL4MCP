# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/utils.py
# module: src.oxylabs_mcp.utils
# qname: src.oxylabs_mcp.utils.extract_links_with_text
# lines: 245-285
def extract_links_with_text(html: str, base_url: str | None = None) -> list[str]:
    """Extract links with their display text from HTML.

    Args:
        html (str): The input HTML string.
        base_url (str | None): Base URL to use for converting relative URLs to absolute.
                             If None, relative URLs will remain as is.

    Returns:
        list[str]: List of links in format [Display Text] URL

    """
    html_tree = fromstring(html)
    links = []

    for link in html_tree.xpath("//a[@href]"):  # type: ignore[union-attr]
        href = link.get("href")  # type: ignore[union-attr]
        text = link.text_content().strip()  # type: ignore[union-attr]

        if href and text:
            # Skip empty or whitespace-only text
            if not text:
                continue

            # Skip anchor links
            if href.startswith("#"):
                continue

            # Skip javascript links
            if href.startswith("javascript:"):
                continue

            # Make relative URLs absolute if base_url is provided
            if base_url and href.startswith("/"):
                # Remove trailing slash from base_url if present
                base = base_url.rstrip("/")
                href = f"{base}{href}"

            links.append(f"[{text}] {href}")

    return links