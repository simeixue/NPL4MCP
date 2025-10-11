# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/tools/query.py
# module: src.fibery_mcp_server.tools.query
# qname: src.fibery_mcp_server.tools.query.parse_q_order_by
# lines: 71-74
def parse_q_order_by(q_order_by: Dict[str, str] | None) -> List[Tuple[List[str], str]] | None:
    if not q_order_by:
        return None
    return [([field], q_order) for field, q_order in q_order_by.items()]