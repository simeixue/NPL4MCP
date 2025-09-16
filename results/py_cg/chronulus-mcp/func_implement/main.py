# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/__init__.py
# module: src.chronulus_mcp.__init__
# qname: src.chronulus_mcp.__init__.main
# lines: 294-298
def main():
    """Chronulus AI: A platform for the forecasting and prediction. Predict anything."""
    parser = argparse.ArgumentParser(description=SERVER_DESCRIPTION_V1)
    parser.parse_args()
    mcp.run(transport="stdio")