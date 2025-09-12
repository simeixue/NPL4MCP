# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/discovery/test_exposures_fetcher.py
# module: tests.unit.discovery.test_exposures_fetcher
# qname: tests.unit.discovery.test_exposures_fetcher.test_fetch_exposure_details_by_name
# lines: 400-469
def test_fetch_exposure_details_by_name(exposures_fetcher, mock_api_client):
    # Mock the response for fetch_exposures (which gets called when filtering by name)
    mock_exposures_response = {
        "data": {
            "environment": {
                "definition": {
                    "exposures": {
                        "pageInfo": {"hasNextPage": False, "endCursor": None},
                        "edges": [
                            {
                                "node": {
                                    "name": "sales_report",
                                    "uniqueId": "exposure.sales.sales_report",
                                    "exposureType": "analysis",
                                    "maturity": "medium",
                                    "ownerEmail": "sales@example.com",
                                    "ownerName": "Sales Team",
                                    "url": None,
                                    "meta": {},
                                    "freshnessStatus": "Stale",
                                    "description": "Monthly sales analysis report",
                                    "label": None,
                                    "parents": [{"uniqueId": "model.sales.sales_data"}],
                                }
                            },
                            {
                                "node": {
                                    "name": "other_exposure",
                                    "uniqueId": "exposure.other.other_exposure",
                                    "exposureType": "dashboard",
                                    "maturity": "high",
                                    "ownerEmail": "other@example.com",
                                    "ownerName": "Other Team",
                                    "url": None,
                                    "meta": {},
                                    "freshnessStatus": "Fresh",
                                    "description": "Other exposure",
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

    mock_api_client.execute_query.return_value = mock_exposures_response

    with patch("dbt_mcp.discovery.client.raise_gql_error"):
        result = exposures_fetcher.fetch_exposure_details(exposure_name="sales_report")

    assert isinstance(result, list)
    assert len(result) == 1
    exposure = result[0]
    assert exposure["name"] == "sales_report"
    assert exposure["uniqueId"] == "exposure.sales.sales_report"
    assert exposure["exposureType"] == "analysis"
    assert exposure["maturity"] == "medium"
    assert exposure["url"] is None
    assert exposure["meta"] == {}
    assert exposure["freshnessStatus"] == "Stale"
    assert exposure["label"] is None

    # Should have called the GET_EXPOSURES query (not GET_EXPOSURE_DETAILS)
    mock_api_client.execute_query.assert_called_once()
    args, kwargs = mock_api_client.execute_query.call_args
    assert args[1]["environmentId"] == 123
    assert args[1]["first"] == 100  # PAGE_SIZE for fetch_exposures