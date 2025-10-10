# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-clickhouse/mcp_clickhouse/main.py
# module: mcp_clickhouse.main
# qname: mcp_clickhouse.main.main
# lines: 5-17
def main():
    config = get_config()
    transport = config.mcp_server_transport

    # For HTTP and SSE transports, we need to specify host and port
    http_transports = [TransportType.HTTP.value, TransportType.SSE.value]
    if transport in http_transports:
        # Use the configured bind host (defaults to 127.0.0.1, can be set to 0.0.0.0)
        # and bind port (defaults to 8000)
        mcp.run(transport=transport, host=config.mcp_bind_host, port=config.mcp_bind_port)
    else:
        # For stdio transport, no host or port is needed
        mcp.run(transport=transport)