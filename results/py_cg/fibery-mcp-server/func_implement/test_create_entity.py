# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/tests/fibery_service_test.py
# module: tests.fibery_service_test
# qname: tests.fibery_service_test.test_create_entity
# lines: 31-42
async def test_create_entity() -> None:
    """Test the create_entity function"""
    fibery_client = FiberyClient(__fibery_host, __fibery_api_token)
    fibery_id = str(uuid4())
    creation_result = await fibery_client.create_entity(
        "Product Management/Item", {"fibery/id": fibery_id, "Product Management/Name": "Test"}
    )

    assert creation_result.success is True, "Entity creation failed"

    deletion_result = await fibery_client.delete_entity("Product Management/Item", fibery_id)
    assert deletion_result.success is True, "Entity deletion failed"