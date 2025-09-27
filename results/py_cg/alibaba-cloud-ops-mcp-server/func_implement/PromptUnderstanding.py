# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/common_api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.common_api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.common_api_tools.PromptUnderstanding
# lines: 27-40
def PromptUnderstanding() -> str:
    """
    Always use this tool first to understand the user's query and convert it into suggestions from Alibaba Cloud experts.
    """
    global _CUSTOM_SERVICE_LIST

    content = PROMPT_UNDERSTANDING
    if _CUSTOM_SERVICE_LIST:
        import re
        pattern = r'Supported Services\s*:\s*\n(?:\s{3}- .+?\n)+'
        replacement = f"Supported Services:\n   - " + "\n   - ".join([f"{k}: {v}" for k, v in _CUSTOM_SERVICE_LIST])
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    return content