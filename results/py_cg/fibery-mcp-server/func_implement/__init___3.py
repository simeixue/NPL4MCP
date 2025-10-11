# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.FiberyClient.__init__
# lines: 125-134
    def __init__(self, fibery_host: str, fibery_api_token: str, fibery_https: bool = True):
        if not fibery_host:
            raise ValueError("Fibery host not provided. Set FIBERY_HOST environment variable.")

        if not fibery_api_token:
            raise ValueError("Fibery API token not provided. Set FIBERY_API_TOKEN environment variable.")

        self.__fibery_host: str = fibery_host
        self.__fibery_api_token: str = fibery_api_token
        self.__fibery_https: bool = fibery_https