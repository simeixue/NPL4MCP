# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/discovery/client.py
# module: src.dbt_mcp.discovery.client
# qname: src.dbt_mcp.discovery.client.ExposuresFetcher.fetch_exposure_details
# lines: 532-559
    def fetch_exposure_details(
        self, exposure_name: str | None = None, unique_ids: list[str] | None = None
    ) -> list[dict]:
        if exposure_name and not unique_ids:
            # Since ExposureFilter doesn't support filtering by name,
            # we need to fetch all exposures and find the one with matching name
            all_exposures = self.fetch_exposures()
            for exposure in all_exposures:
                if exposure.get("name") == exposure_name:
                    return [exposure]
            return []
        elif unique_ids:
            exposure_filters = self._get_exposure_filters(unique_ids=unique_ids)
            variables = {
                "environmentId": self.environment_id,
                "filter": exposure_filters,
                "first": len(unique_ids),  # Request as many as we're filtering for
            }
            result = self.api_client.execute_query(
                GraphQLQueries.GET_EXPOSURE_DETAILS, variables
            )
            raise_gql_error(result)
            edges = result["data"]["environment"]["definition"]["exposures"]["edges"]
            if not edges:
                return []
            return [edge["node"] for edge in edges]
        else:
            raise ValueError("Either exposure_name or unique_ids must be provided")