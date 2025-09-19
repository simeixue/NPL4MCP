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
