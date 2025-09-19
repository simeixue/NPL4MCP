# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/Medical_calculator_MCP/server.py
# module: server
# qname: server.free_androgen_index
# lines: 78-86
def free_androgen_index(total_testosterone: float, shbg: float) -> float:
    """
    Calculates Free Androgen Index (FAI)
    Formula: FAI = (total testosterone / SHBG) * 100
    Where:
    - total testosterone in nmol/L
    - SHBG in nmol/L
    """
    return (total_testosterone / shbg) * 100