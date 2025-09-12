# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/discovery/test_exposures_fetcher.py
# module: tests.unit.discovery.test_exposures_fetcher
# qname: tests.unit.discovery.test_exposures_fetcher.test_fetch_exposure_details_by_name_not_found
# lines: 513-535
def test_fetch_exposure_details_by_name_not_found(exposures_fetcher, mock_api_client):
    # Mock empty response for fetch_exposures
    mock_response = {
        "data": {
            "environment": {
                "definition": {
                    "exposures": {
                        "pageInfo": {"hasNextPage": False, "endCursor": None},
                        "edges": [],
                    }
                }
            }
        }
    }

    mock_api_client.execute_query.return_value = mock_response

    with patch("dbt_mcp.discovery.client.raise_gql_error"):
        result = exposures_fetcher.fetch_exposure_details(
            exposure_name="nonexistent_exposure"
        )

    assert result == []