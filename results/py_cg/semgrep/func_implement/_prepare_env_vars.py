# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/configure_semgrep_mcp.py
# module: scripts.configure_semgrep_mcp
# qname: scripts.configure_semgrep_mcp._prepare_env_vars
# lines: 43-56
def _prepare_env_vars() -> dict[str, str]:
    """Prepare and validate environment variables."""
    env_vars = {}

    # Add SEMGREP_APP_TOKEN if it exists and is valid
    if semgrep_token := os.getenv("SEMGREP_APP_TOKEN"):
        if _validate_env_var_name("SEMGREP_APP_TOKEN"):
            # Validate token format (basic check)
            if re.match(r"^[a-zA-Z0-9_-]+$", semgrep_token):
                env_vars["SEMGREP_APP_TOKEN"] = semgrep_token
            else:
                print("⚠️  Invalid SEMGREP_APP_TOKEN format, skipping")

    return env_vars