# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/prompts/prompts.py
# module: src.dbt_mcp.prompts.prompts
# qname: src.dbt_mcp.prompts.prompts.get_prompt
# lines: 4-5
def get_prompt(name: str) -> str:
    return (Path(__file__).parent / f"{name}.md").read_text()