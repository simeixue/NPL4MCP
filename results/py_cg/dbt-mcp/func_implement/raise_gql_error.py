# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/gql/errors.py
# module: src.dbt_mcp.gql.errors
# qname: src.dbt_mcp.gql.errors.raise_gql_error
# lines: 1-14
def raise_gql_error(result: dict) -> None:
    if result.get("errors"):
        if len(result.get("errors", [])) > 0:
            error_messages = [
                error.get("message", "Unknown error")
                for error in result.get("errors", [])
                if isinstance(error, dict)
            ]
            if error_messages:
                raise ValueError(f"Errors calling API: {', '.join(error_messages)}")
        raise ValueError(
            "Unknown error calling API. "
            + "Check your configuration or contact support if this persists."
        )