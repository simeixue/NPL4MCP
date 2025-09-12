# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/chat.py
# module: src.meilisearch_mcp.chat
# qname: src.meilisearch_mcp.chat.ChatManager._combine_chunks
# lines: 49-57
    def _combine_chunks(self, chunks: List[Dict[str, Any]]) -> str:
        """Combine streaming chunks into a single response message."""
        content_parts = []
        for chunk in chunks:
            if "choices" in chunk and chunk["choices"]:
                choice = chunk["choices"][0]
                if "delta" in choice and "content" in choice["delta"]:
                    content_parts.append(choice["delta"]["content"])
        return "".join(content_parts)