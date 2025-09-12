# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/validation.py
# module: src.mcp_nefino.validation
# qname: src.mcp_nefino.validation.validate_date_range
# lines: 17-41
def validate_date_range(
    begin_date: str | None, end_date: str | None
) -> tuple[bool, str | None]:
    """Validate a date range.

    Args:
        begin_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not begin_date or not end_date:
        return True, None

    try:
        begin = datetime.strptime(begin_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        if begin > end:
            return False, "Begin date must be before or equal to end date"

        return True, None
    except ValueError:
        return False, "Dates must be in YYYY-MM-DD format"