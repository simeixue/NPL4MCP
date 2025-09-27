# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/oss_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.oss_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.oss_tools.CredentialsProvider.__init__
# lines: 16-29
    def __init__(self) -> None:
        credentials = get_credentials_from_header()
        if credentials:
            access_key_id = credentials.get('AccessKeyId', None)
            access_key_secret = credentials.get('AccessKeySecret', None)
            session_token = credentials.get('SecurityToken', None)
        else:
            credentialsClient = CredClient()
            access_key_id = credentialsClient.get_credential().access_key_id
            access_key_secret = credentialsClient.get_credential().access_key_secret
            session_token = credentialsClient.get_credential().security_token

        self._credentials = Credentials(
            access_key_id, access_key_secret, session_token)