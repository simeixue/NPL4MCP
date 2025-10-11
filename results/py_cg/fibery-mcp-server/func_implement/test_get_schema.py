# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/tests/fibery_service_test.py
# module: tests.fibery_service_test
# qname: tests.fibery_service_test.test_get_schema
# lines: 22-28
async def test_get_schema() -> None:
    """Test the get_schema function"""
    fibery_client = FiberyClient(__fibery_host, __fibery_api_token)
    schema = await fibery_client.get_schema()

    assert schema is not None, "No schema returned"
    assert len(schema.databases) > 0, "Schema does not contain 'types' field"