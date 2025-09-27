# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/mcp_server.py
# module: src.mcp_server_qdrant.mcp_server
# qname: src.mcp_server_qdrant.mcp_server.QdrantMCPServer.__init__
# lines: 31-79
    def __init__(
        self,
        tool_settings: ToolSettings,
        qdrant_settings: QdrantSettings,
        embedding_provider_settings: Optional[EmbeddingProviderSettings] = None,
        embedding_provider: Optional[EmbeddingProvider] = None,
        name: str = "mcp-server-qdrant",
        instructions: str | None = None,
        **settings: Any,
    ):
        self.tool_settings = tool_settings
        self.qdrant_settings = qdrant_settings

        if embedding_provider_settings and embedding_provider:
            raise ValueError(
                "Cannot provide both embedding_provider_settings and embedding_provider"
            )

        if not embedding_provider_settings and not embedding_provider:
            raise ValueError(
                "Must provide either embedding_provider_settings or embedding_provider"
            )

        self.embedding_provider_settings: Optional[EmbeddingProviderSettings] = None
        self.embedding_provider: Optional[EmbeddingProvider] = None

        if embedding_provider_settings:
            self.embedding_provider_settings = embedding_provider_settings
            self.embedding_provider = create_embedding_provider(
                embedding_provider_settings
            )
        else:
            self.embedding_provider_settings = None
            self.embedding_provider = embedding_provider

        assert self.embedding_provider is not None, "Embedding provider is required"

        self.qdrant_connector = QdrantConnector(
            qdrant_settings.location,
            qdrant_settings.api_key,
            qdrant_settings.collection_name,
            self.embedding_provider,
            qdrant_settings.local_path,
            make_indexes(qdrant_settings.filterable_fields_dict()),
        )

        super().__init__(name=name, instructions=instructions, **settings)

        self.setup_tools()