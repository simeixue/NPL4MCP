# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/validation.py
# module: src.mcp_nefino.validation
# qname: src.mcp_nefino.validation.validate_date_format
# lines: 6-14
def validate_date_format(date_str: str | None) -> bool:
    """Validate that a date string is in YYYY-MM-DD format."""
    if not date_str:
        return True
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False