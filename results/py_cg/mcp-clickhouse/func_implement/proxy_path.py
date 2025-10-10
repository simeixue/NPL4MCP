# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/mcp_env.py
# module: mcp_clickhouse.mcp_env
# qname: mcp_clickhouse.mcp_env.ClickHouseConfig.proxy_path
# lines: 129-130
    def proxy_path(self) -> str:
        return os.getenv("CLICKHOUSE_PROXY_PATH")