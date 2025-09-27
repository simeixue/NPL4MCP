# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.api_tools._create_parameter_schema
# lines: 138-139
def _create_parameter_schema(fields: dict):
    return make_dataclass("ParameterSchema", [(name, type_, value) for name, (type_, value) in fields.items()])