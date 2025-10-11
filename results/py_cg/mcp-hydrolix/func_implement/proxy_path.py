# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_env.py
# module: mcp_hydrolix.mcp_env
# qname: mcp_hydrolix.mcp_env.HydrolixConfig.proxy_path
# lines: 135-136
    def proxy_path(self) -> str:
        return os.getenv("HYDROLIX_PROXY_PATH")