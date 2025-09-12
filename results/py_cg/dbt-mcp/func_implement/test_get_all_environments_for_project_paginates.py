# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/oauth/test_fastapi_app_pagination.py
# module: tests.unit.oauth.test_fastapi_app_pagination
# qname: tests.unit.oauth.test_fastapi_app_pagination.test_get_all_environments_for_project_paginates
# lines: 76-116
def test_get_all_environments_for_project_paginates(mock_get: Mock, base_headers):
    # Two pages: first full page (limit=2), second partial (1 item)
    first_page_resp = Mock()
    first_page_resp.json.return_value = {
        "data": [
            {"id": 201, "name": "Dev", "deployment_type": "development"},
            {"id": 202, "name": "Prod", "deployment_type": "production"},
        ]
    }
    first_page_resp.raise_for_status.return_value = None

    second_page_resp = Mock()
    second_page_resp.json.return_value = {
        "data": [
            {"id": 203, "name": "Staging", "deployment_type": "development"},
        ]
    }
    second_page_resp.raise_for_status.return_value = None

    mock_get.side_effect = [first_page_resp, second_page_resp]

    result = _get_all_environments_for_project(
        dbt_platform_url="https://cloud.getdbt.com",
        account_id=1,
        project_id=9,
        headers=base_headers,
        page_size=2,
    )

    assert len(result) == 3
    assert {e.id for e in result} == {201, 202, 203}

    expected_urls = [
        "https://cloud.getdbt.com/api/v3/accounts/1/projects/9/environments/?state=1&offset=0&limit=2",
        "https://cloud.getdbt.com/api/v3/accounts/1/projects/9/environments/?state=1&offset=2&limit=2",
    ]
    actual_urls = [
        call.kwargs["url"] if "url" in call.kwargs else call.args[0]
        for call in mock_get.call_args_list
    ]
    assert actual_urls == expected_urls