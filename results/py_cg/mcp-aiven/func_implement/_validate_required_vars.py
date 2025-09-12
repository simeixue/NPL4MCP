# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-aiven/mcp_aiven/mcp_env.py
# module: mcp_aiven.mcp_env
# qname: mcp_aiven.mcp_env.AivenConfig._validate_required_vars
# lines: 51-66
    def _validate_required_vars(self) -> None:
        """Validate that all required environment variables are set.

        Raises:
            ValueError: If any required environment variable is missing.
        """
        load_dotenv()
        missing_vars = []
        for var in ["AIVEN_BASE_URL", "AIVEN_TOKEN"]:
            if var not in os.environ:
                missing_vars.append(var)

        if missing_vars:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing_vars)}"
            )