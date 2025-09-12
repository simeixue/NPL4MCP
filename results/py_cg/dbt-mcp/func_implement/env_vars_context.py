# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/tests/env_vars.py
# module: tests.env_vars
# qname: tests.env_vars.env_vars_context
# lines: 6-25
def env_vars_context(env_vars: dict[str, str]):
    """Temporarily set environment variables and restore them afterward."""
    # Store original env vars
    original_env = {}

    # Save original and set new values
    for key, value in env_vars.items():
        if key in os.environ:
            original_env[key] = os.environ[key]
        os.environ[key] = value

    try:
        yield
    finally:
        # Restore original values
        for key in env_vars:
            if key in original_env:
                os.environ[key] = original_env[key]
            else:
                del os.environ[key]