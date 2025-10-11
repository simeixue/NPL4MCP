# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_server.py
# module: mcp_hydrolix.mcp_server
# qname: mcp_hydrolix.mcp_server.create_hydrolix_client
# lines: 245-268
def create_hydrolix_client():
    client_config = get_config().get_client_config()
    auth_info = (
        f"as {client_config['username']}"
        if "username" in client_config
        else "using service account token"
    )
    logger.info(
        f"Creating Hydrolix client connection to {client_config['host']}:{client_config['port']} "
        f"{auth_info} "
        f"(secure={client_config['secure']}, verify={client_config['verify']}, "
        f"connect_timeout={client_config['connect_timeout']}s, "
        f"send_receive_timeout={client_config['send_receive_timeout']}s)"
    )

    try:
        client = clickhouse_connect.get_client(**client_config)
        # Test the connection
        version = client.server_version
        logger.info(f"Successfully connected to Hydrolix compatible with ClickHouse {version}")
        return client
    except Exception as e:
        logger.error(f"Failed to connect to Hydrolix: {str(e)}")
        raise