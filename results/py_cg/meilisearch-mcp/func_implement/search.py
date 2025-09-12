# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/client.py
# module: src.meilisearch_mcp.client
# qname: src.meilisearch_mcp.client.MeilisearchClient.search
# lines: 51-102
    def search(
        self,
        query: str,
        index_uid: Optional[str] = None,
        limit: Optional[int] = 20,
        offset: Optional[int] = 0,
        filter: Optional[str] = None,
        sort: Optional[List[str]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Search through Meilisearch indices.
        If index_uid is provided, search in that specific index.
        If not provided, search across all available indices.
        """
        try:
            # Prepare search parameters, removing None values
            search_params = {
                "limit": limit if limit is not None else 20,
                "offset": offset if offset is not None else 0,
            }

            if filter is not None:
                search_params["filter"] = filter
            if sort is not None:
                search_params["sort"] = sort

            # Add any additional parameters
            search_params.update({k: v for k, v in kwargs.items() if v is not None})

            if index_uid:
                # Search in specific index
                index = self.client.index(index_uid)
                return index.search(query, search_params)
            else:
                # Search across all indices
                results = {}
                indexes = self.client.get_indexes()

                for index in indexes["results"]:
                    try:
                        search_result = index.search(query, search_params)
                        if search_result["hits"]:  # Only include indices with matches
                            results[index.uid] = search_result
                    except Exception as e:
                        logger.warning(f"Failed to search index {index.uid}: {str(e)}")
                        continue

                return {"multi_index": True, "query": query, "results": results}

        except Exception as e:
            raise Exception(f"Search failed: {str(e)}")