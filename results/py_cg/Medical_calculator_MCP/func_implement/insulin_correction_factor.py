# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/Medical_calculator_MCP/server.py
# module: server
# qname: server.insulin_correction_factor
# lines: 91-96
def insulin_correction_factor(tdd: float) -> float:
    """
    Calculates insulin correction factor (ICF) or insulin sensitivity factor
    Formula: 1800 / TDD (using 1800 rule)
    """
    return 1800 / tdd