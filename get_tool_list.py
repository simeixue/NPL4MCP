from fastmcp import Client
# from fastmcp import ParsedFunction
from fastmcp.tools import FunctionTool
import inspect
import asyncio
from utils.file_util import FileUtil
# 根目录
REPO_BASE = "/Users/xue/workspace/mcp_project/mcp_server_pyrepos"

# 工具对象序列化函数
def serialize_tool(tool):
    return {
        "name": tool.name,
        "description": tool.description,
        # "implementation": source,
        "input_schema": tool.inputSchema,
        "annotations": tool.annotations,
    }

config = {
    "mcpServers": {
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
        # "atla-mcp-server": {
        #     "command": "uvx",
        #     "args": ["atla-mcp-server"],
        #     "env": {
        #         "ATLA_API_KEY": "<your-atla-api-key>"
        #     }
        # },
        # "dappier-mcp": {
        #     "command": "uvx",
        #     "args": ["dappier-mcp"],
        #     "env": {
        #         "DAPPIER_API_KEY": "YOUR_API_KEY_HERE"
        #     }
        # },
        # "geekbot-mcp": {
        #   "command": "uv",
        #   "args": [
        #     "tool",
        #     "run",
        #     "geekbot-mcp"
        #   ],
        #   "env": {
        #     "GB_API_KEY": "YOUR-API-KEY"
        #   }
        # },
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
        # "MiniMax": {
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
        # "mcp-server-motherduck": {
        #     "command": "uvx",
        #     "args": [
        #         "mcp-server-motherduck",
        #         "--db-path",
        #         "md:",
        #         "--motherduck-token",
        #         "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNpbWF5eHVlQGdtYWlsLmNvbSIsInNlc3Npb24iOiJzaW1heXh1ZS5nbWFpbC5jb20iLCJwYXQiOiJWcHVnUkhGOE8wSTltQXN0UFVpZUV6eUdnQm82MC14QldnVFdDbVlLSFBRIiwidXNlcklkIjoiOWQ3OTZjNDAtZWEzOC00ZTY2LTkxZjctZGQ0YWIzZTc5ODAxIiwiaXNzIjoibWRfcGF0IiwicmVhZE9ubHkiOmZhbHNlLCJ0b2tlblR5cGUiOiJyZWFkX3dyaXRlIiwiaWF0IjoxNzU4OTg1OTg3fQ.MI0blGkkyEbjQNd2Eo5JPanJcyRnfQBRtjmKQyb6NkM"
        #     ]
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
        # "ElevenLabs": {
        #     "command": "uvx",
        #     "args": ["elevenlabs-mcp"],
        #     "env": {
        #         "ELEVENLABS_API_KEY": "f9e85540026f9fc5ebe1901fa5bbe368afab6637768a4623d6752589f480a8d8"
        #     }
        # },
        # "time": {
        #     "command": "uvx",
        #     "args": ["mcp-server-time"]
        # }
        # "Medical_calculator_MCP": {
        #     "command": "python",
        #     "args": [
        #         f"{REPO_BASE}/Medical_calculator_MCP/server.py"
        #     ]
        # },
        # "twolven_mcp-server-puppeteer-py": {
        #     "command": "python",
        #     "args": [f"{REPO_BASE}/twolven_mcp-server-puppeteer-py/puppeteer.py"]
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
        #         "mcp-aiven"
        #     ],
        #     "env": {
        #         "AIVEN_BASE_URL": "https://api.aiven.io",
        #         "AIVEN_TOKEN": "$AIVEN_TOKEN"
        #     }
        # },
        # "windows-cmd": {
        #     "command": "node",
        #     "args": ["/path/to/dist/index.js"]
        # },
        # "time": {
        #     "command": "uvx",
        #     "args": [
        #         "mcp-server-time",
        #         "--local-timezone=America/New_York"
        #     ]
        # },
        # "amap-maps": {
        #     "command": "npx",
        #     "args": [
        #         "-y",
        #         "@amap/amap-maps-mcp-server"
        #     ],
        #     "env": {
        #         "AMAP_MAPS_API_KEY": "c0b4b756aa82fdee14537edd073fc99f"
        #     }
        # },
        


        # "weather": {
        #     "command": "uv",
        #     "args": [
        #         "--directory",
        #         "/Users/xue/workspace/mcp_project/weather",
        #         "run",
        #         "weather.py"
        #     ]
        # },
        # "mcp-sequentialthinking-tools": {
		# 	"command": "npx",
		# 	"args": ["-y", "mcp-sequentialthinking-tools"]
		# },
        # "windows-cli": { #javascript
        #     "command": "npx",
        #     "args": ["-y", "@simonb97/server-win-cli"]
        # },
        # "Wikipedia": { #javascript
        #     "command": "npx",
        #     "args": ["-y", "wikipedia-mcp"]
        # },
        # "calculate_expression1": {
        #     # "isActive": false,
        #     "command": "uv",
        #     "args": [
        #         "run",
        #         "--directory",
        #         "/path/to/mcp_calculate_server",
        #         "server.py"
        #     ],
        # }
    }
}

# Create a client that connects to both servers
client = Client(config)

async def main():
    tools=[]
    # Connection is established here
    async with client:
        print(f"Client connected: {client.is_connected()}")

        # Make MCP calls within the context
        tools = await client.list_tools()


        print(f"Available tools: {tools}")
        
        

    # Connection is closed automatically here
    print(f"Client connected: {client.is_connected()}")

    # 先转换为可 JSON 序列化格式
    serializable_tools = [serialize_tool(t) for t in tools]
    FileUtil.save_data(serializable_tools, './results/tools_list.json',indent=2)



if __name__ == "__main__":
    asyncio.run(main())
