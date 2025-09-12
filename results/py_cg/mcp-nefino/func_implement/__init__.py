# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/client.py
# module: src.mcp_nefino.client
# qname: src.mcp_nefino.client.NefinoClient.__init__
# lines: 13-17
    def __init__(self, config: NefinoConfig):
        """Initialize the Nefino client with configuration."""
        self.base_url = config.base_url
        self.jwt_secret = config.jwt_secret
        self.token = self._create_token(config.username, config.password)