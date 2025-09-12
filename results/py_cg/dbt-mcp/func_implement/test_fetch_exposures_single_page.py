# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/discovery/test_exposures_fetcher.py
# module: tests.unit.discovery.test_exposures_fetcher
# qname: tests.unit.discovery.test_exposures_fetcher.test_fetch_exposures_single_page
# lines: 17-71
def test_fetch_exposures_single_page(exposures_fetcher, mock_api_client):
    mock_response = {
        "data": {
            "environment": {
                "definition": {
                    "exposures": {
                        "pageInfo": {"hasNextPage": False, "endCursor": None},
                        "edges": [
                            {
                                "node": {
                                    "name": "test_exposure",
                                    "uniqueId": "exposure.test.test_exposure",
                                    "exposureType": "application",
                                    "maturity": "high",
                                    "ownerEmail": "test@example.com",
                                    "ownerName": "Test Owner",
                                    "url": "https://example.com",
                                    "meta": {},
                                    "freshnessStatus": "Unknown",
                                    "description": "Test exposure",
                                    "label": None,
                                    "parents": [
                                        {"uniqueId": "model.test.parent_model"}
                                    ],
                                }
                            }
                        ],
                    }
                }
            }
        }
    }

    mock_api_client.execute_query.return_value = mock_response

    with patch("dbt_mcp.discovery.client.raise_gql_error"):
        result = exposures_fetcher.fetch_exposures()

    assert len(result) == 1
    assert result[0]["name"] == "test_exposure"
    assert result[0]["uniqueId"] == "exposure.test.test_exposure"
    assert result[0]["exposureType"] == "application"
    assert result[0]["maturity"] == "high"
    assert result[0]["ownerEmail"] == "test@example.com"
    assert result[0]["ownerName"] == "Test Owner"
    assert result[0]["url"] == "https://example.com"
    assert result[0]["meta"] == {}
    assert result[0]["freshnessStatus"] == "Unknown"
    assert result[0]["description"] == "Test exposure"
    assert result[0]["parents"] == [{"uniqueId": "model.test.parent_model"}]

    mock_api_client.execute_query.assert_called_once()
    args, kwargs = mock_api_client.execute_query.call_args
    assert args[1]["environmentId"] == 123
    assert args[1]["first"] == 100