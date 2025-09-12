# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/embeddings/fastembed.py
# module: src.mcp_server_qdrant.embeddings.fastembed
# qname: src.mcp_server_qdrant.embeddings.fastembed.FastEmbedProvider.__init__
# lines: 15-17
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.embedding_model = TextEmbedding(model_name)