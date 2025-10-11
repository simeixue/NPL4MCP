# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/database.py
# module: src.fibery_mcp_server.tools.database
# qname: src.fibery_mcp_server.tools.database.describe_database
# lines: 28-32
def describe_database(database: str, fields: List[PrettyField]) -> str:
    content = f"Database {database}:\n"
    for field in fields:
        content += f"    {field.title} [{field.name}]: {field.type}\n"
    return content + "\n"