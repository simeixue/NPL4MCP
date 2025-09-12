# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/discovery/test_exposures_fetcher.py
# module: tests.unit.discovery.test_exposures_fetcher
# qname: tests.unit.discovery.test_exposures_fetcher.test_fetch_exposures_multiple_pages
# lines: 74-160
def test_fetch_exposures_multiple_pages(exposures_fetcher, mock_api_client):
    page1_response = {
        "data": {
            "environment": {
                "definition": {
                    "exposures": {
                        "pageInfo": {"hasNextPage": True, "endCursor": "cursor123"},
                        "edges": [
                            {
                                "node": {
                                    "name": "exposure1",
                                    "uniqueId": "exposure.test.exposure1",
                                    "exposureType": "application",
                                    "maturity": "high",
                                    "ownerEmail": "test1@example.com",
                                    "ownerName": "Test Owner 1",
                                    "url": "https://example1.com",
                                    "meta": {},
                                    "freshnessStatus": "Unknown",
                                    "description": "Test exposure 1",
                                    "label": None,
                                    "parents": [],
                                }
                            }
                        ],
                    }
                }
            }
        }
    }

    page2_response = {
        "data": {
            "environment": {
                "definition": {
                    "exposures": {
                        "pageInfo": {"hasNextPage": False, "endCursor": "cursor456"},
                        "edges": [
                            {
                                "node": {
                                    "name": "exposure2",
                                    "uniqueId": "exposure.test.exposure2",
                                    "exposureType": "dashboard",
                                    "maturity": "medium",
                                    "ownerEmail": "test2@example.com",
                                    "ownerName": "Test Owner 2",
                                    "url": "https://example2.com",
                                    "meta": {"key": "value"},
                                    "freshnessStatus": "Fresh",
                                    "description": "Test exposure 2",
                                    "label": "Label 2",
                                    "parents": [
                                        {"uniqueId": "model.test.parent_model2"}
                                    ],
                                }
                            }
                        ],
                    }
                }
            }
        }
    }

    mock_api_client.execute_query.side_effect = [page1_response, page2_response]

    with patch("dbt_mcp.discovery.client.raise_gql_error"):
        result = exposures_fetcher.fetch_exposures()

    assert len(result) == 2
    assert result[0]["name"] == "exposure1"
    assert result[1]["name"] == "exposure2"
    assert result[1]["meta"] == {"key": "value"}
    assert result[1]["label"] == "Label 2"

    assert mock_api_client.execute_query.call_count == 2

    # Check first call (no cursor)
    first_call = mock_api_client.execute_query.call_args_list[0]
    assert first_call[0][1]["environmentId"] == 123
    assert first_call[0][1]["first"] == 100
    assert "after" not in first_call[0][1]

    # Check second call (with cursor)
    second_call = mock_api_client.execute_query.call_args_list[1]
    assert second_call[0][1]["environmentId"] == 123
    assert second_call[0][1]["first"] == 100
    assert second_call[0][1]["after"] == "cursor123"