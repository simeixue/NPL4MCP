# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/discovery/test_exposures_fetcher.py
# module: tests.unit.discovery.test_exposures_fetcher
# qname: tests.unit.discovery.test_exposures_fetcher.test_fetch_exposure_details_by_unique_ids_single
# lines: 246-312
def test_fetch_exposure_details_by_unique_ids_single(
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
                                    "parents": [
                                        {"uniqueId": "model.analytics.customers"},
                                        {
                                            "uniqueId": "model.analytics.customer_metrics"
                                        },
                                    ],
                                }
                            }
                        ]
                    }
                }
            }
        }
    }

    mock_api_client.execute_query.return_value = mock_response

    with patch("dbt_mcp.discovery.client.raise_gql_error"):
        result = exposures_fetcher.fetch_exposure_details(
            unique_ids=["exposure.analytics.customer_dashboard"]
        )

    assert isinstance(result, list)
    assert len(result) == 1
    exposure = result[0]
    assert exposure["name"] == "customer_dashboard"
    assert exposure["uniqueId"] == "exposure.analytics.customer_dashboard"
    assert exposure["exposureType"] == "dashboard"
    assert exposure["maturity"] == "high"
    assert exposure["ownerEmail"] == "analytics@example.com"
    assert exposure["ownerName"] == "Analytics Team"
    assert exposure["url"] == "https://dashboard.example.com/customers"
    assert exposure["meta"] == {"team": "analytics", "priority": "high"}
    assert exposure["freshnessStatus"] == "Fresh"
    assert exposure["description"] == "Customer analytics dashboard"
    assert exposure["label"] == "Customer Dashboard"
    assert len(exposure["parents"]) == 2
    assert exposure["parents"][0]["uniqueId"] == "model.analytics.customers"
    assert exposure["parents"][1]["uniqueId"] == "model.analytics.customer_metrics"

    mock_api_client.execute_query.assert_called_once()
    args, kwargs = mock_api_client.execute_query.call_args
    assert args[1]["environmentId"] == 123
    assert args[1]["first"] == 1
    assert args[1]["filter"] == {"uniqueIds": ["exposure.analytics.customer_dashboard"]}