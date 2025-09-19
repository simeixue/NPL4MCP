from pathlib import Path
import os

REPO_BASE = "/Users/xue/workspace/mcp_project/mcp_server_pyrepos"
OUT_BASE = Path("/Users/xue/workspace/mcp_project/NPL4MCP/results/py_cg")

# ---------------- Server config ----------------
config = {
    "mcpServers": {
        "twolven_mcp-server-puppeteer-py": {
            "command": "python",
            "args": [f"{REPO_BASE}/twolven_mcp-server-puppeteer-py/puppeteer.py"]
        }
        # "Medical_calculator_MCP":{
        #     "command": "python",
        #     "args": [
        #         f"{REPO_BASE}/Medical_calculator_MCP/server.py"
        #     ]
        # }
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
        # "python-notebook-mcp": {
        #     "command": "python", 
        #     "args": [
        #         f"{REPO_BASE}/python-notebook-mcp/server.py"
        #         ],
        #     "autoApprove": ["initialize_workspace"]
        # }
        
        


# ---------------- 有问题或需要配置的server ----------------
        # "MemProcFS-mcp-server": {
        #     "command": "python",
        #     "args": [
        #         f"{REPO_BASE}/MemProcFS-mcp-server/server.py"
        #     ]
        # }

        # "mcp-server-qdrant": { #tool的名字改变
        #     "command": "uvx",
        #     "args": ["mcp-server-qdrant"],
        #     "env": {
        #     "QDRANT_URL": "https://xyz-example.eu-central.aws.cloud.qdrant.io:6333",
        #     "QDRANT_API_KEY": "your_api_key",
        #     "COLLECTION_NAME": "your-collection-name",
        #     "EMBEDDING_MODEL": "sentence-transformers/all-MiniLM-L6-v2"
        #     }
        # }
        # "mcp-server-nacos": {
        #     "command": "uv",
        #     "args": [ 
        #     "--directory",
        #     f"{REPO_BASE}/mcp-server-nacos",
        #     "run",
        #     "mcp-server-nacos"
        #     ]
        # }
        
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

        # "alibabacloud-observability-mcp-server": {
        #     "url": "http://localhost:7897/sse"
        # },
    }
}