from pathlib import Path
import os

REPO_BASE = "/Users/xue/workspace/mcp_project/mcp_server_pyrepos"
OUT_BASE = Path("/Users/xue/workspace/mcp_project/NPL4MCP/results/py_cg")

# ---------------- Server config ----------------
config = {
    "mcpServers": {
        # "mcp-aiven": {
        #     "command": "uv",
        #     "args": [
        #         "--directory",
        #         f"{REPO_BASE}/mcp-aiven",
        #         "run",
        #         "--with-editable",
        #         f"{REPO_BASE}/mcp-aiven",
        #         "--python",
        #         "3.13",
        #         "mcp-aiven",
        #     ],
        #     "env": {
        #         "AIVEN_BASE_URL": "https://api.aiven.io",
        #         "AIVEN_TOKEN": os.environ.get("AIVEN_TOKEN", ""),
        #     },
        # },
        # "chronulus-mcp": {
        #     "command": "uvx",
        #     "args": ["chronulus-mcp"],
        #     "env": {"CHRONULUS_API_KEY": os.environ.get("CHRONULUS_API_KEY", "")},
        # },
        # "meilisearch-mcp": {
        #     "command": "uvx",
        #     "args": ["-n", "meilisearch-mcp"]
        # },
        "mcp-server-qdrant": {
            "command": "uvx",
            "args": ["mcp-server-qdrant"],
            "env": {
            "QDRANT_URL": "https://xyz-example.eu-central.aws.cloud.qdrant.io:6333",
            "QDRANT_API_KEY": "your_api_key",
            "COLLECTION_NAME": "your-collection-name",
            "EMBEDDING_MODEL": "sentence-transformers/all-MiniLM-L6-v2"
            }
        }
        
        # "MiniMax-MCP": {
        #     "command": "uvx",
        #     "args": ["minimax-mcp", "-y"],
        #     "env": {
        #         "MINIMAX_API_KEY": os.environ.get("MINIMAX_API_KEY", ""),
        #         "MINIMAX_MCP_BASE_PATH": os.environ.get("MINIMAX_MCP_BASE_PATH", ""),
        #         "MINIMAX_API_HOST": os.environ.get("MINIMAX_API_HOST", ""),
        #         "MINIMAX_API_RESOURCE_MODE": os.environ.get(
        #             "MINIMAX_API_RESOURCE_MODE", ""
        #         ),
        #     },
        # },
    }
}