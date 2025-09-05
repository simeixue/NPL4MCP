# ========== 配置 ==========
REPO_BASE = "/Users/xue/workspace/mcp_project/mcp_server_repos"

# 手动写 serverKey 对应的仓库文件夹
SERVER_REPO_DIR = {
    "weather":"weather",
    "Wikipedia": "wikipedia-mcp",
    "amap-maps": "amap-maps",
    "mcp-sequentialthinking-tools": "mcp-sequentialthinking-tools",
}

CONFIG = {
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": [
                "--directory",
                f"{REPO_BASE}/weather",
                "run",
                "weather.py"
            ]
        },
        "Wikipedia": {"command": "npx", "args": ["-y", "wikipedia-mcp"]},
        "amap-maps": {
            "command": "npx",
            "args": [
                "-y",
                "@amap/amap-maps-mcp-server"
            ],
            "env": {
                "AMAP_MAPS_API_KEY": "c0b4b756aa82fdee14537edd073fc99f"
            }
        },
        # "windows-cli": {"command": "npx", "args": ["-y", "@simonb97/server-win-cli"]},
        # "windows-cmd": {"command": "node", "args": ["/path/to/dist/index.js"]},
        "mcp-sequentialthinking-tools": {
            "command": "npx",
            "args": ["-y", "mcp-sequentialthinking-tools"]
        },
    }
}

OUT_JSON = "./results/tools_list_implementation.json"
OUT_DIR = "./results"