# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/utils.py
# module: src.semgrep_mcp.utilities.utils
# qname: src.semgrep_mcp.utilities.utils.get_user_settings_file
# lines: 24-34
def get_user_settings_file() -> Path:
    def get_user_data_folder() -> Path:
        config_home = os.getenv("XDG_CONFIG_HOME")
        if config_home is None or not Path(config_home).is_dir():
            parent_dir = Path.home()
        else:
            parent_dir = Path(config_home)
        return parent_dir / ".semgrep"

    path = os.getenv("SEMGREP_SETTINGS_FILE", str(get_user_data_folder() / SETTINGS_FILENAME))
    return Path(path)