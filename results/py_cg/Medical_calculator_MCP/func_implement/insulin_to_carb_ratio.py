# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/Medical_calculator_MCP/server.py
# module: server
# qname: server.insulin_to_carb_ratio
# lines: 99-104
def insulin_to_carb_ratio(tdd: float) -> float:
    """
    Calculates insulin to carbohydrate ratio (I:C)
    Formula: 450 / TDD (using 450 rule)
    """
    return 450 / tdd