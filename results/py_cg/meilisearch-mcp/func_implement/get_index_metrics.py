# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/monitoring.py
# module: src.meilisearch_mcp.monitoring
# qname: src.meilisearch_mcp.monitoring.MonitoringManager.get_index_metrics
# lines: 65-78
    def get_index_metrics(self, index_uid: str) -> IndexMetrics:
        """Get detailed metrics for an index"""
        try:
            index = self.client.index(index_uid)
            stats = index.get_stats()

            return IndexMetrics(
                number_of_documents=stats["numberOfDocuments"],
                field_distribution=stats["fieldDistribution"],
                is_indexing=stats["isIndexing"],
                index_size=stats.get("indexSize"),
            )
        except Exception as e:
            raise Exception(f"Failed to get index metrics: {str(e)}")