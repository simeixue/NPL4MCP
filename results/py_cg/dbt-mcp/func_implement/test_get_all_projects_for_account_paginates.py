# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/unit/oauth/test_fastapi_app_pagination.py
# module: tests.unit.oauth.test_fastapi_app_pagination
# qname: tests.unit.oauth.test_fastapi_app_pagination.test_get_all_projects_for_account_paginates
# lines: 30-72
def test_get_all_projects_for_account_paginates(mock_get: Mock, base_headers, account):
    # Two pages: first full page (limit=2), second partial page (1 item) -> stop
    first_page_resp = Mock()
    first_page_resp.json.return_value = {
        "data": [
            {"id": 101, "name": "Proj A", "account_id": account.id},
            {"id": 102, "name": "Proj B", "account_id": account.id},
        ]
    }
    first_page_resp.raise_for_status.return_value = None

    second_page_resp = Mock()
    second_page_resp.json.return_value = {
        "data": [
            {"id": 103, "name": "Proj C", "account_id": account.id},
        ]
    }
    second_page_resp.raise_for_status.return_value = None

    mock_get.side_effect = [first_page_resp, second_page_resp]

    result = _get_all_projects_for_account(
        dbt_platform_url="https://cloud.getdbt.com",
        account=account,
        headers=base_headers,
        page_size=2,
    )

    # Should aggregate 3 projects and include account_name field
    assert len(result) == 3
    assert {p.id for p in result} == {101, 102, 103}
    assert all(p.account_name == account.name for p in result)

    # Verify correct pagination URLs called
    expected_urls = [
        "https://cloud.getdbt.com/api/v3/accounts/1/projects/?state=1&offset=0&limit=2",
        "https://cloud.getdbt.com/api/v3/accounts/1/projects/?state=1&offset=2&limit=2",
    ]
    actual_urls = [
        call.kwargs["url"] if "url" in call.kwargs else call.args[0]
        for call in mock_get.call_args_list
    ]
    assert actual_urls == expected_urls