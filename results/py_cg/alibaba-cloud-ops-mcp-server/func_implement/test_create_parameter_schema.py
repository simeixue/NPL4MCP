# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/tests/tools/test_api_tools.py
# module: tests.tools.test_api_tools
# qname: tests.tools.test_api_tools.test_create_parameter_schema
# lines: 38-45
def test_create_parameter_schema():
    fields = {
        'foo': (str, MagicMock()),
        'bar': (int, MagicMock())
    }
    schema_cls = api_tools._create_parameter_schema(fields)
    inst = schema_cls(foo='a', bar=1)
    assert inst.foo == 'a' and inst.bar == 1