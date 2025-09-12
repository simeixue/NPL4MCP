# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/discovery/test_exposures_fetcher.py
# module: tests.unit.discovery.test_exposures_fetcher
# qname: tests.unit.discovery.test_exposures_fetcher.test_fetch_exposures_handles_malformed_edges
# lines: 186-243
def test_fetch_exposures_handles_malformed_edges(exposures_fetcher, mock_api_client):
    mock_response = {
        "data": {
            "environment": {
                "definition": {
                    "exposures": {
                        "pageInfo": {"hasNextPage": False, "endCursor": None},
                        "edges": [
                            {
                                "node": {
                                    "name": "valid_exposure",
                                    "uniqueId": "exposure.test.valid_exposure",
                                    "exposureType": "application",
                                    "maturity": "high",
                                    "ownerEmail": "test@example.com",
                                    "ownerName": "Test Owner",
                                    "url": "https://example.com",
                                    "meta": {},
                                    "freshnessStatus": "Unknown",
                                    "description": "Valid exposure",
                                    "label": None,
                                    "parents": [],
                                }
                            },
                            {"invalid": "edge"},  # Missing "node" key
                            {"node": "not_a_dict"},  # Node is not a dict
                            {
                                "node": {
                                    "name": "another_valid_exposure",
                                    "uniqueId": "exposure.test.another_valid_exposure",
                                    "exposureType": "dashboard",
                                    "maturity": "low",
                                    "ownerEmail": "test2@example.com",
                                    "ownerName": "Test Owner 2",
                                    "url": "https://example2.com",
                                    "meta": {},
                                    "freshnessStatus": "Stale",
                                    "description": "Another valid exposure",
                                    "label": None,
                                    "parents": [],
                                }
                            },
                        ],
                    }
                }
            }
        }
    }

    mock_api_client.execute_query.return_value = mock_response

    with patch("dbt_mcp.discovery.client.raise_gql_error"):
        result = exposures_fetcher.fetch_exposures()

    # Should only get the valid exposures (malformed edges should be filtered out)
    assert len(result) == 2
    assert result[0]["name"] == "valid_exposure"
    assert result[1]["name"] == "another_valid_exposure"