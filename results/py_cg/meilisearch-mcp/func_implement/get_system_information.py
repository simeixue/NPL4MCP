# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/monitoring.py
# module: src.meilisearch_mcp.monitoring
# qname: src.meilisearch_mcp.monitoring.MonitoringManager.get_system_information
# lines: 80-93
    def get_system_information(self) -> Dict[str, Any]:
        """Get system-level information"""
        try:
            version = self.client.get_version()
            stats = self.client.get_all_stats()

            return {
                "version": version,
                "database_size": stats["databaseSize"],
                "last_update": stats["lastUpdate"],
                "indexes": stats["indexes"],
            }
        except Exception as e:
            raise Exception(f"Failed to get system information: {str(e)}")