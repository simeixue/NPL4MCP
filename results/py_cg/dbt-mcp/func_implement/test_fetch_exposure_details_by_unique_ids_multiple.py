# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/discovery/test_exposures_fetcher.py
# module: tests.unit.discovery.test_exposures_fetcher
# qname: tests.unit.discovery.test_exposures_fetcher.test_fetch_exposure_details_by_unique_ids_multiple
# lines: 315-397
def test_fetch_exposure_details_by_unique_ids_multiple(
    exposures_fetcher, mock_api_client
):
    mock_response = {
        "data": {
            "environment": {
                "definition": {
                    "exposures": {
                        "edges": [
                            {
                                "node": {
                                    "name": "customer_dashboard",
                                    "uniqueId": "exposure.analytics.customer_dashboard",
                                    "exposureType": "dashboard",
                                    "maturity": "high",
                                    "ownerEmail": "analytics@example.com",
                                    "ownerName": "Analytics Team",
                                    "url": "https://dashboard.example.com/customers",
                                    "meta": {"team": "analytics", "priority": "high"},
                                    "freshnessStatus": "Fresh",
                                    "description": "Customer analytics dashboard",
                                    "label": "Customer Dashboard",
                                    "parents": [],
                                }
                            },
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
                        ]
                    }
                }
            }
        }
    }

    mock_api_client.execute_query.return_value = mock_response

    with patch("dbt_mcp.discovery.client.raise_gql_error"):
        result = exposures_fetcher.fetch_exposure_details(
            unique_ids=[
                "exposure.analytics.customer_dashboard",
                "exposure.sales.sales_report",
            ]
        )

    assert isinstance(result, list)
    assert len(result) == 2

    # Check first exposure
    exposure1 = result[0]
    assert exposure1["name"] == "customer_dashboard"
    assert exposure1["uniqueId"] == "exposure.analytics.customer_dashboard"
    assert exposure1["exposureType"] == "dashboard"

    # Check second exposure
    exposure2 = result[1]
    assert exposure2["name"] == "sales_report"
    assert exposure2["uniqueId"] == "exposure.sales.sales_report"
    assert exposure2["exposureType"] == "analysis"

    mock_api_client.execute_query.assert_called_once()
    args, kwargs = mock_api_client.execute_query.call_args
    assert args[1]["environmentId"] == 123
    assert args[1]["first"] == 2
    assert args[1]["filter"] == {
        "uniqueIds": [
            "exposure.analytics.customer_dashboard",
            "exposure.sales.sales_report",
        ]
    }