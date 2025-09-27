# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/utils.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.utils
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.utils.create_config
# lines: 32-51
def create_config():
    credentials = get_credentials_from_header()

    if credentials:
        access_key_id = credentials.get('AccessKeyId')
        access_key_secret = credentials.get('AccessKeySecret')
        token = credentials.get('SecurityToken')
        config = Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=token
        )
    elif settings.headers_credential_only:
        config = Config()
    else:
        credentials_client = CredClient()
        config = Config(credential=credentials_client)

    config.user_agent = 'alibaba-cloud-ops-mcp-server'
    return config