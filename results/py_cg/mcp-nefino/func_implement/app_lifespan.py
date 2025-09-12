# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/server.py
# module: src.mcp_nefino.server
# qname: src.mcp_nefino.server.app_lifespan
# lines: 28-37
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Initialize and manage the lifecycle of application dependencies."""
    try:
        config = NefinoConfig.from_env()
        client = NefinoClient(config)
        task_manager = TaskManager()
        yield AppContext(config=config, client=client, task_manager=task_manager)
    except Exception as e:
        print(f"Failed to initialize Nefino client: {str(e)}")
        raise