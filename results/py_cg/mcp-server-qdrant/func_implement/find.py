# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/common/wrap_filters.py
# module: src.mcp_server_qdrant.common.wrap_filters
# qname: src.mcp_server_qdrant.common.wrap_filters.find
# lines: 114-124
    def find(
        query: Annotated[str, Field(description="What to search for")],
        collection_name: Annotated[
            str, Field(description="The collection to search in")
        ],
        query_filter: Optional[models.Filter] = None,
    ) -> list[str]:
        print("query", query)
        print("collection_name", collection_name)
        print("query_filter", query_filter)
        return ["mypy rules"]