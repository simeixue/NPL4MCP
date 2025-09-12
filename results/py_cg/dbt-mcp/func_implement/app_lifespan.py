# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/mcp/server.py
# module: src.dbt_mcp.mcp.server
# qname: src.dbt_mcp.mcp.server.app_lifespan
# lines: 28-44
async def app_lifespan(server: FastMCP) -> AsyncIterator[None]:
    logger.info("Starting MCP server")
    try:
        yield
    except Exception as e:
        logger.error(f"Error in MCP server: {e}")
        raise e
    finally:
        logger.info("Shutting down MCP server")
        try:
            await SqlToolsManager.close()
        except Exception:
            logger.exception("Error closing SQL tools manager")
        try:
            shutdown()
        except Exception:
            logger.exception("Error shutting down MCP server")