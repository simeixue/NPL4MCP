# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-hydrolix/mcp_hydrolix/mcp_env.py
# module: mcp_hydrolix.mcp_env
# qname: mcp_hydrolix.mcp_env.HydrolixConfig._validate_required_vars
# lines: 202-218
    def _validate_required_vars(self) -> None:
        """Validate that all required environment variables are set.

        Raises:
            ValueError: If any required environment variable is missing.
        """
        missing_vars = []
        if self.service_account:
            required_vars = ["HYDROLIX_HOST", "HYDROLIX_TOKEN"]
        else:
            required_vars = ["HYDROLIX_HOST", "HYDROLIX_USER", "HYDROLIX_PASSWORD"]
        for var in required_vars:
            if var not in os.environ:
                missing_vars.append(var)

        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")