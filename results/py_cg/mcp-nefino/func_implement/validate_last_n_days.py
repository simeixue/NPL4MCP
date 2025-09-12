# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/validation.py
# module: src.mcp_nefino.validation
# qname: src.mcp_nefino.validation.validate_last_n_days
# lines: 44-62
def validate_last_n_days(days: int | None) -> tuple[bool, str | None]:
    """Validate last_n_days parameter.

    Args:
        days: Number of days to look back

    Returns:
        Tuple of (is_valid, error_message)
    """
    if days is None:
        return True, None

    if not isinstance(days, int):
        return False, "last_n_days must be an integer"

    if days < 0:
        return False, "last_n_days must be zero or positive"

    return True, None