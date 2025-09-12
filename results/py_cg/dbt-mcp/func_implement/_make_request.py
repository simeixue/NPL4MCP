# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_admin/client.py
# module: src.dbt_mcp.dbt_admin.client
# qname: src.dbt_mcp.dbt_admin.client.DbtAdminAPIClient._make_request
# lines: 28-38
    def _make_request(self, method: str, endpoint: str, **kwargs) -> dict[str, Any]:
        """Make a request to the dbt API."""
        url = f"{self.config.url}{endpoint}"

        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise AdminAPIError(f"API request failed: {e}")