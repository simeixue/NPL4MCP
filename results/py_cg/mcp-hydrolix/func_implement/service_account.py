# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_env.py
# module: mcp_hydrolix.mcp_env
# qname: mcp_hydrolix.mcp_env.HydrolixConfig.service_account
# lines: 72-78
    def service_account(self) -> bool:
        """Determine if service account is enabled

        Defaults to false.
        Can be overridden if HYDROLIX_TOKEN environment variable.
        """
        return "HYDROLIX_TOKEN" in os.environ