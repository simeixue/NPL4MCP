# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/qdrant.py
# module: src.mcp_server_qdrant.qdrant
# qname: src.mcp_server_qdrant.qdrant.QdrantConnector.get_collection_names
# lines: 55-61
    async def get_collection_names(self) -> list[str]:
        """
        Get the names of all collections in the Qdrant server.
        :return: A list of collection names.
        """
        response = await self._client.get_collections()
        return [collection.name for collection in response.collections]