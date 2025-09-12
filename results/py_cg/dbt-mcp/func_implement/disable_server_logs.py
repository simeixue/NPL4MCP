# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/oauth/logging.py
# module: src.dbt_mcp.oauth.logging
# qname: src.dbt_mcp.oauth.logging.disable_server_logs
# lines: 4-14
def disable_server_logs() -> None:
    # Disable uvicorn, fastapi, and related loggers
    loggers = (
        "uvicorn",
        "uvicorn.error",
        "uvicorn.access",
        "fastapi",
    )

    for logger_name in loggers:
        logging.getLogger(logger_name).disabled = True