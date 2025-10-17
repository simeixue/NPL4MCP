from pathlib import Path
import os

REPO_BASE = "/Users/xue/workspace/mcp_project/mcp_server_pyrepos"
OUT_BASE = Path("/Users/xue/workspace/mcp_project/NPL4MCP/results/py_cg")

# ---------------- Server config ----------------
config = {
    "mcpServers": {
        # "kagimcp": {
        #     "command": "uvx",
        #     "args": ["kagimcp"],
        #     "env": {
        #         "KAGI_API_KEY": "YOUR_API_KEY_HERE",
        #         "KAGI_SUMMARIZER_ENGINE": "YOUR_ENGINE_CHOICE_HERE" 
        #     }
        # },
        # "alibaba-cloud-ops-mcp-server": {
        #     "timeout": 600,
        #     "command": "uvx",
        #     "args": [
        #         "alibaba-cloud-ops-mcp-server@latest"
        #     ],
        #     "env": {
        #         "ALIBABA_CLOUD_ACCESS_KEY_ID": "Your Access Key ID",
        #         "ALIBABA_CLOUD_ACCESS_KEY_SECRET": "Your Access Key SECRET"
        #     }
        # },
        # "mcp-server-qdrant": {
        #     "command": "uvx",
        #     "args": ["mcp-server-qdrant"],
        #     "env": {
        #     "QDRANT_URL": "https://xyz-example.eu-central.aws.cloud.qdrant.io:6333",
        #     "QDRANT_API_KEY": "your_api_key",
        #     "COLLECTION_NAME": "your-collection-name",
        #     "EMBEDDING_MODEL": "sentence-transformers/all-MiniLM-L6-v2"
        #     }
        # },
        # "AbletonMCP": {
        #     "command": "uvx",
        #     "args": [
        #         "ableton-mcp"
        #     ]
        # },
        # "blender": {
        #     "command": "uvx",
        #     "args": [
        #         "blender-mcp"
        #     ]
        # },
        # "time": {
        #     "command": "uvx",
        #     "args": ["mcp-server-time"]
        # },
        # "fetch": {
        #     "command": "uvx",
        #     "args": ["mcp-server-fetch"]
        # },
        # "git": {
        #     "command": "uvx",
        #     "args": ["mcp-server-git"]
        # },

        # "twolven_mcp-server-puppeteer-py": {
        #     "command": "python",
        #     "args": [f"{REPO_BASE}/twolven_mcp-server-puppeteer-py/puppeteer.py"]
        # },
        # "AgentWong_optimized-memory-mcp-serverv2": {
        #     "command": "python",
        #     "args": ["-m", "src.main"]
        # },

        # "Medical_calculator_MCP":{
        #     "command": "python",
        #     "args": [
        #         f"{REPO_BASE}/Medical_calculator_MCP/server.py"
        #     ]
        # },
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
        # },
        # "mcp-clickhouse": {
        #     "command": "uv",
        #     "args": [
        #         "run",
        #         "--with",
        #         "mcp-clickhouse",
        #         "mcp-clickhouse"
        #     ],
        #     "env": {
        #         "CLICKHOUSE_HOST": "sql-clickhouse.clickhouse.com",
        #         "CLICKHOUSE_PORT": "8443",
        #         "CLICKHOUSE_USER": "demo",
        #         "CLICKHOUSE_PASSWORD": "",
        #         "CLICKHOUSE_SECURE": "true",
        #         "CLICKHOUSE_VERIFY": "true",
        #         "CLICKHOUSE_CONNECT_TIMEOUT": "30",
        #         "CLICKHOUSE_SEND_RECEIVE_TIMEOUT": "30"
        #     }
        # },
        # "dappier-mcp": {
        #     "command": "uvx",
        #     "args": ["dappier-mcp"],
        #     "env": {
        #         "DAPPIER_API_KEY": "YOUR_API_KEY_HERE"
        #     }
        # },
        # "atla-mcp-server": {
        #     "command": "uvx",
        #     "args": ["atla-mcp-server"],
        #     "env": {
        #         "ATLA_API_KEY": "<your-atla-api-key>"
        #     }
        # },
        # "mcp-metricool": {
        #     "command": "uvx",
        #     "args": [
        #         "--upgrade",
        #         "mcp-metricool"
        #     ],
        #     "env": {
        #         "METRICOOL_USER_TOKEN": "<METRICOOL_USER_TOKEN>",
        #         "METRICOOL_USER_ID": "<METRICOOL_USER_ID>"
        #     }
        # },
        # "mcp-hydrolix": {
        #     "command": "uv",
        #     "args": [
        #         "run",
        #         "--with",
        #         "mcp-hydrolix",
        #         "--python",
        #         "3.13",
        #         "mcp-hydrolix"
        #     ],
        #     "env": {
        #         "HYDROLIX_HOST": "<hydrolix-host>",
        #         "HYDROLIX_USER": "<hydrolix-user>",
        #         "HYDROLIX_PASSWORD": "<hydrolix-password>"
        #     }
        # },
        # "semgrep": {
        #     "command": "uvx",
        #     "args": ["semgrep-mcp"],
        #     "env": {
        #         "SEMGREP_APP_TOKEN": "<token>"
        #     }
        # },
        # "fibery-mcp-server": {
        #     "command": "uv",
        #     "args": [
        #          "tool",
        #          "run",
        #          "fibery-mcp-server",
        #          "--fibery-host",
        #          "your-domain.fibery.io",
        #          "--fibery-api-token",
        #          "your-api-token"
        #     ]
        # },

# ---------------- 需要配置的server ----------------
        "magic-mcp": {
            "command": "npx",
            "args": ["--directory",
             f"{REPO_BASE}/magic-mcp", "API_KEY=\"68c52aff4557513401a1120a75361ad6eab2139b77c825bbb54d4d0909cd3ddd\""]
        },
        # "web-eval-agent": {
        #     "command": "uvx",
        #     "args": [
        #         "--refresh-package",
        #         "webEvalAgent",
        #         "--from",
        #         "git+https://github.com/Operative-Sh/web-eval-agent.git",
        #         "webEvalAgent"
        #     ],
        #     "env": {
        #         "OPERATIVE_API_KEY": "op-vm057UM7hvCx8zTHGpKc3dPn1oo1lNznju0fJLdx_90"
        #     }
        # },
        # "MiniMax-MCP": {
        #     "command": "uvx",
        #     "args": [
        #         "minimax-mcp",
        #         "-y"
        #     ],
        #     "env": {
        #         "MINIMAX_API_KEY": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiJTaSBteCIsIlVzZXJOYW1lIjoiU2kgbXgiLCJBY2NvdW50IjoiIiwiU3ViamVjdElEIjoiMTk3MTkxODEyOTg0ODEyODMzMyIsIlBob25lIjoiIiwiR3JvdXBJRCI6IjE5NzE5MTgxMjk4NDM5MzgxMjUiLCJQYWdlTmFtZSI6IiIsIk1haWwiOiJzaW1heXh1ZUBnbWFpbC5jb20iLCJDcmVhdGVUaW1lIjoiMjAyNS0wOS0yNyAyMzozMToxMCIsIlRva2VuVHlwZSI6MSwiaXNzIjoibWluaW1heCJ9.Nlv4ep0fMV-HJEbJzeXiD8RPZMsxG_uSldJt896Skj_P-mxDpKqjq7wpRiQLxBCuuW1oXbXuLk08FrRAbTlsnuRo8PkRf51pR6CZampLQyN0x0UMRAq90T8HLmIKljZAMV8jCECJXtwXnVsKwUx6U8MhH6GkxCW1z6FDcBVMR7dRaTneAleBPNBD4DH8EEPOiY6FzliOOhJYxLMRfE5T5PIj7k093F94lXsYw1o1zJHyuwC4AO35ayDz8tD6HTYLu8mhmYQECEe0UTtxu7cCZk9X2FqHzKajhAE7pAP8A_Oy-ItrXsHqlD7nFOd9do1CaT4auCJUMV63vaRnzRQt0g",
        #         "MINIMAX_MCP_BASE_PATH": "local-output-dir-path, such as /User/xxx/Desktop",
        #         "MINIMAX_API_HOST": "api host, https://api.minimax.io | https://api.minimaxi.com",
        #         "MINIMAX_API_RESOURCE_MODE": "optional, [url|local], url is default, audio/image/video are downloaded locally or provided in URL format"
        #     }
        # },
        # "ElevenLabs": {
        #     "command": "uvx",
        #     "args": ["elevenlabs-mcp"],
        #     "env": {
        #         "ELEVENLABS_API_KEY": "f9e85540026f9fc5ebe1901fa5bbe368afab6637768a4623d6752589f480a8d8"
        #     }
        # },
        # "oxylabs-mcp": {
        #     "command": "uvx",
        #     "args": ["oxylabs-mcp"],
        #     "env": {
        #         "OXYLABS_USERNAME": "simayxue@gmail.com",
        #         "OXYLABS_PASSWORD": "D6N2D3XET9sk@rP",
        #         "OXYLABS_AI_STUDIO_API_KEY": "ULcB6BoAsq7IL0zAa9t0d64Z7PkfIsqH8SNO39nG"
        #     }
        # },
        # "mcp-server-motherduck": {
        #     "command": "uvx",
        #     "args": [
        #         "mcp-server-motherduck",
        #         "--db-path",
        #         "md:",
        #         "--motherduck-token",
        #         "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNpbWF5eHVlQGdtYWlsLmNvbSIsInNlc3Npb24iOiJzaW1heXh1ZS5nbWFpbC5jb20iLCJwYXQiOiJWcHVnUkhGOE8wSTltQXN0UFVpZUV6eUdnQm82MC14QldnVFdDbVlLSFBRIiwidXNlcklkIjoiOWQ3OTZjNDAtZWEzOC00ZTY2LTkxZjctZGQ0YWIzZTc5ODAxIiwiaXNzIjoibWRfcGF0IiwicmVhZE9ubHkiOmZhbHNlLCJ0b2tlblR5cGUiOiJyZWFkX3dyaXRlIiwiaWF0IjoxNzU4OTg1OTg3fQ.MI0blGkkyEbjQNd2Eo5JPanJcyRnfQBRtjmKQyb6NkM"
        #     ]
        # }
        
        


# ---------------- 有问题的server ----------------
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
        # "ProxmoxMCP": {
        #     "command": "python",
        #     "args": ["-m", "proxmox_mcp.server"],
        #     "cwd": f"{REPO_BASE}/ProxmoxMCP",
        #     "env": {
        #         "PYTHONPATH": f"{REPO_BASE}/ProxmoxMCP/src",
        #         "PROXMOX_MCP_CONFIG": f"{REPO_BASE}/ProxmoxMCP/proxmox-config/config.json",
        #         "PROXMOX_HOST": "your-proxmox-host",
        #         "PROXMOX_USER": "username@pve",
        #         "PROXMOX_TOKEN_NAME": "token-name",
        #         "PROXMOX_TOKEN_VALUE": "token-value",
        #         "PROXMOX_PORT": "8006",
        #         "PROXMOX_VERIFY_SSL": "false",
        #         "PROXMOX_SERVICE": "PVE",
        #         "LOG_LEVEL": "DEBUG"
        #     },
        #     "disabled": False,
        #     "autoApprove": []
        # },
    }
}