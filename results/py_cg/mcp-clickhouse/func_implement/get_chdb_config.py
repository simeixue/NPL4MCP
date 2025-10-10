# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_env.py
# module: mcp_clickhouse.mcp_env
# qname: mcp_clickhouse.mcp_env.get_chdb_config
# lines: 272-283
def get_chdb_config() -> ChDBConfig:
    """
    Gets the singleton instance of ChDBConfig.
    Instantiates it on the first call.

    Returns:
        ChDBConfig: The chDB configuration instance
    """
    global _CHDB_CONFIG_INSTANCE
    if _CHDB_CONFIG_INSTANCE is None:
        _CHDB_CONFIG_INSTANCE = ChDBConfig()
    return _CHDB_CONFIG_INSTANCE