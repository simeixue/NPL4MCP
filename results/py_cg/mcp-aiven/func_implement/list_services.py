# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-aiven/mcp_aiven/mcp_server.py
# module: mcp_aiven.mcp_server
# qname: mcp_aiven.mcp_server.list_services
# lines: 38-42
def list_services(project_name):
    logger.info("Listing all services in a project: %s", project_name)
    results = aiven_client.get_services(project=project_name)
    logger.info(f"Found {len(results)} services")
    return [s["service_name"] for s in results]