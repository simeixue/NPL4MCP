# config.py
import os

# 根目录
REPO_BASE = "/Users/xue/workspace/mcp_project/mcp_server_repos"

# 自动扫描 REPO_BASE 下的子文件夹作为 server repo
SERVER_REPO_DIR = {
    name: name
    for name in os.listdir(REPO_BASE)
    if os.path.isdir(os.path.join(REPO_BASE, name))
}

print(SERVER_REPO_DIR)

# 手动写启动方式，每个server的名字需要和SERVER_REPO_DIR的字段一致
CONFIG = {
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": ["--directory", f"{REPO_BASE}/weather", "run", "weather.py"],
        },
        "wikipedia-mcp": {"command": "npx", "args": ["-y", "wikipedia-mcp"]},
        "amap-maps": {
            "command": "npx",
            "args": ["-y", "@amap/amap-maps-mcp-server"],
            "env": {"AMAP_MAPS_API_KEY": "c0b4b756aa82fdee14537edd073fc99f"},
        },
        "mcp-sequentialthinking-tools": {
            "command": "npx",
            "args": ["-y", "mcp-sequentialthinking-tools"],
        },
        "mcp_calculate_server": {
            "command": "uv",
            "args": [
                "run",
                "--directory",
                f"{REPO_BASE}/mcp_calculate_server",
                "server.py"
            ],
            }
    }
}

OUT_JSON = "./results/tools_list_implementation.json"
OUT_DIR = "./results"
