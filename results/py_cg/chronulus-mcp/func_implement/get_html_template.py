# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/assets.py
# module: src.chronulus_mcp.assets
# qname: src.chronulus_mcp.assets.get_html_template
# lines: 26-41
def get_html_template(filename: str) -> str:
    """
    Get the code for a html template.

    Returns
    -------
    str
        Html template source code
    """
    # Get the package directory
    for file in resources.files("chronulus_mcp._assets.html").iterdir():
        if file.is_file() and file.name == filename:
            contents = file.read_text()
            return contents

    raise FileNotFoundError(filename)