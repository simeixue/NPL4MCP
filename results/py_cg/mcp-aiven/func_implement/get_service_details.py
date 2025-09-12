# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-aiven/mcp_aiven/mcp_server.py
# module: mcp_aiven.mcp_server
# qname: mcp_aiven.mcp_server.get_service_details
# lines: 46-49
def get_service_details(project_name, service_name):
    logger.info("Fetching details for service: %s in project: %s", service_name, project_name)
    result = aiven_client.get_service(project=project_name, service=service_name)
    return result