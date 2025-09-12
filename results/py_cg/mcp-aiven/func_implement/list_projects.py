# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-aiven/mcp_aiven/mcp_server.py
# module: mcp_aiven.mcp_server
# qname: mcp_aiven.mcp_server.list_projects
# lines: 30-34
def list_projects():
    logger.info("Listing all projects")
    results = aiven_client.get_projects()
    logger.info(f"Found {len(results)} projects")
    return [result['project_name'] for result in results]