# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/blender/src/blender_mcp/server.py
# module: src.blender_mcp.server
# qname: src.blender_mcp.server.BlenderConnection.connect
# lines: 31-44
    def connect(self) -> bool:
        """Connect to the Blender addon socket server"""
        if self.sock:
            return True
            
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            logger.info(f"Connected to Blender at {self.host}:{self.port}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Blender: {str(e)}")
            self.sock = None
            return False