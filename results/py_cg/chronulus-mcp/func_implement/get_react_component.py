# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/assets.py
# module: src.chronulus_mcp.assets
# qname: src.chronulus_mcp.assets.get_react_component
# lines: 7-22
def get_react_component(filename: str) -> str:
    """
    Get the code for a react template.

    Returns
    -------
    str
        React template source code
    """
    # Get the package directory
    for file in resources.files("chronulus_mcp._assets.react").iterdir():
        if file.is_file() and file.name == filename:
            contents = file.read_text()
            return contents

    raise FileNotFoundError(filename)