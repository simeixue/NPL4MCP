# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/main.py
# module: src.dbt_mcp.main
# qname: src.dbt_mcp.main.main
# lines: 7-9
def main() -> None:
    config = load_config()
    asyncio.run(create_dbt_mcp(config)).run()