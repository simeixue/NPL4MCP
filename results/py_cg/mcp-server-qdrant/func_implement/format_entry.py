# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/mcp_server.py
# module: src.mcp_server_qdrant.mcp_server
# qname: src.mcp_server_qdrant.mcp_server.QdrantMCPServer.format_entry
# lines: 81-86
    def format_entry(self, entry: Entry) -> str:
        """
        Feel free to override this method in your subclass to customize the format of the entry.
        """
        entry_metadata = json.dumps(entry.metadata) if entry.metadata else ""
        return f"<entry><content>{entry.content}</content><metadata>{entry_metadata}</metadata></entry>"