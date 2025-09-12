# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-aiven/mcp_aiven/mcp_env.py
# module: mcp_aiven.mcp_env
# qname: mcp_aiven.mcp_env.AivenConfig.get_client_config
# lines: 38-49
    def get_client_config(self) -> dict:
        """Get the configuration dictionary for aiven_connect client.

        Returns:
            dict: Configuration ready to be passed to aiven_connect.get_client()
        """
        config = {
            "url": self.url,
            "token": self.token,
        }

        return config