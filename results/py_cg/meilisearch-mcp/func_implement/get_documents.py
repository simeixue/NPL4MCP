# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/documents.py
# module: src.meilisearch_mcp.documents
# qname: src.meilisearch_mcp.documents.DocumentManager.get_documents
# lines: 11-60
    def get_documents(
        self,
        index_uid: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        fields: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Get documents from an index"""
        try:
            index = self.client.index(index_uid)
            # Build parameters dict, excluding None values to avoid API errors
            params = {}
            if offset is not None:
                params["offset"] = offset
            if limit is not None:
                params["limit"] = limit
            if fields is not None:
                params["fields"] = fields

            result = index.get_documents(params if params else {})

            # Convert meilisearch model objects to JSON-serializable format
            if hasattr(result, "__dict__"):
                result_dict = result.__dict__.copy()
                # Convert individual document objects in results if they exist
                if "results" in result_dict and isinstance(
                    result_dict["results"], list
                ):
                    serialized_results = []
                    for doc in result_dict["results"]:
                        if hasattr(doc, "__dict__"):
                            # Extract the actual document data
                            doc_dict = doc.__dict__.copy()
                            # Look for private attributes that might contain the actual data
                            for key, value in doc_dict.items():
                                if key.startswith("_") and isinstance(value, dict):
                                    # Use the dict content instead of the wrapper
                                    serialized_results.append(value)
                                    break
                            else:
                                # If no private dict found, use the object dict directly
                                serialized_results.append(doc_dict)
                        else:
                            serialized_results.append(doc)
                    result_dict["results"] = serialized_results
                return result_dict
            else:
                return result
        except Exception as e:
            raise Exception(f"Failed to get documents: {str(e)}")