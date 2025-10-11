# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/tracing.py
# module: src.semgrep_mcp.utilities.tracing
# qname: src.semgrep_mcp.utilities.tracing.get_token_from_user_settings
# lines: 60-70
def get_token_from_user_settings() -> str:
    settings_file = get_user_settings_file()
    if not os.access(settings_file, os.R_OK) or not settings_file.is_file():
        return ""
    with settings_file.open() as fd:
        yaml_contents = yaml.load(fd)

    if not isinstance(yaml_contents, Mapping):
        return ""

    return yaml_contents.get("api_token", "")