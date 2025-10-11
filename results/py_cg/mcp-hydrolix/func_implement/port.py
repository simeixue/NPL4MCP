# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_env.py
# module: mcp_hydrolix.mcp_env
# qname: mcp_hydrolix.mcp_env.HydrolixConfig.port
# lines: 61-69
    def port(self) -> int:
        """Get the Hydrolix port.

        Defaults to 8088.
        Can be overridden by HYDROLIX_PORT environment variable.
        """
        if "HYDROLIX_PORT" in os.environ:
            return int(os.environ["HYDROLIX_PORT"])
        return 8088