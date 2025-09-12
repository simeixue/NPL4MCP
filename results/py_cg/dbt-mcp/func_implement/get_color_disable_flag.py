# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_cli/binary_type.py
# module: src.dbt_mcp.dbt_cli.binary_type
# qname: src.dbt_mcp.dbt_cli.binary_type.get_color_disable_flag
# lines: 46-59
def get_color_disable_flag(binary_type: BinaryType) -> str:
    """
    Get the appropriate color disable flag for the given binary type.

    Args:
        binary_type: The type of dbt binary

    Returns:
        str: The color disable flag to use
    """
    if binary_type == BinaryType.DBT_CLOUD_CLI:
        return "--no-color"
    else:  # DBT_CORE or FUSION
        return "--no-use-colors"