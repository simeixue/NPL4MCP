# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/__init__.py
# module: src.chronulus_mcp.__init__
# qname: src.chronulus_mcp.__init__.get_scorecard_react_template
# lines: 277-279
def get_scorecard_react_template() -> str:
    """Get scorecard.tsx"""
    return get_react_component("Scorecard.jsx")