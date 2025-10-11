# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/utils.py
# module: src.semgrep_mcp.utilities.utils
# qname: src.semgrep_mcp.utilities.utils.get_semgrep_app_token
# lines: 37-55
def get_semgrep_app_token() -> str | None:
    """
    Returns the deployment ID the token is for, if token is valid
    """

    # Prioritize environment variable first
    env_token = os.environ.get("SEMGREP_APP_TOKEN")
    if env_token is not None:
        return env_token

    # Fall back to settings file if environment variable is not set
    user_settings_file = get_user_settings_file()
    if user_settings_file.exists():
        with open(user_settings_file) as f:
            yaml = YAML(typ="safe", pure=True)
            settings = yaml.load(f)
            return settings.get("api_token")

    return None