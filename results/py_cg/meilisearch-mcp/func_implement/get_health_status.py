# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/monitoring.py
# module: src.meilisearch_mcp.monitoring
# qname: src.meilisearch_mcp.monitoring.MonitoringManager.get_health_status
# lines: 35-63
    def get_health_status(self) -> HealthStatus:
        """Get comprehensive health status"""
        try:
            # Get various stats to build health picture
            stats = self.client.get_all_stats()
            indexes = self.client.get_indexes()

            indexes_info = []
            for index in indexes:
                index_stats = self.client.index(index.uid).get_stats()
                indexes_info.append(
                    {
                        "uid": index.uid,
                        "documents_count": index_stats["numberOfDocuments"],
                        "is_indexing": index_stats["isIndexing"],
                    }
                )

            return HealthStatus(
                is_healthy=True,
                database_size=stats["databaseSize"],
                last_update=datetime.fromisoformat(
                    stats["lastUpdate"].replace("Z", "+00:00")
                ),
                indexes_count=len(indexes),
                indexes_info=indexes_info,
            )
        except Exception as e:
            raise Exception(f"Failed to get health status: {str(e)}")