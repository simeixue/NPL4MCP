# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/client.py
# module: src.mcp_nefino.client
# qname: src.mcp_nefino.client.NefinoClient._create_token
# lines: 19-26
    def _create_token(self, username: str, password: str) -> str:
        """Create JWT token for authentication."""
        payload = {
            "username": username,
            "password": password,
            "api_key": self.jwt_secret,
        }
        return jwt.encode(payload, self.jwt_secret, algorithm="HS256")