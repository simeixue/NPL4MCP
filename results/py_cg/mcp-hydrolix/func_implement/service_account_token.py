# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_env.py
# module: mcp_hydrolix.mcp_env
# qname: mcp_hydrolix.mcp_env.HydrolixConfig.service_account_token
# lines: 81-89
    def service_account_token(self) -> str:
        """Get the service account token

        Defaults to None.
        Can be overridden if HYDROLIX_TOKEN environment variable.
        """
        if "HYDROLIX_TOKEN" in os.environ:
            return os.environ["HYDROLIX_TOKEN"]
        return None