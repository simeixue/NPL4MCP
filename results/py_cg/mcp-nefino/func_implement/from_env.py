# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/config.py
# module: src.mcp_nefino.config
# qname: src.mcp_nefino.config.NefinoConfig.from_env
# lines: 20-30
    def from_env(cls) -> "NefinoConfig":
        """Create configuration from environment variables."""
        try:
            return cls(
                username=os.environ["NEFINO_USERNAME"],
                password=os.environ["NEFINO_PASSWORD"],
                jwt_secret=os.environ["NEFINO_JWT_SECRET"],
                base_url=os.environ["NEFINO_BASE_URL"],
            )
        except KeyError as e:
            raise ValueError(f"{e.args[0]} environment variable is required") from e