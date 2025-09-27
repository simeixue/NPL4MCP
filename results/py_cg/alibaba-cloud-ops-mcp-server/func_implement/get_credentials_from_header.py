# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/utils.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.utils
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.utils.get_credentials_from_header
# lines: 11-29
def get_credentials_from_header():
    credentials = None
    try:
        request = get_http_request()
        headers = request.headers
        access_key_id = headers.get('x-acs-accesskey-id', None)
        access_key_secret = headers.get('x-acs-accesskey-secret', None)
        token = headers.get('x-acs-security-token', None)

        if access_key_id:
            credentials = {
                'AccessKeyId': access_key_id,
                'AccessKeySecret': access_key_secret,
                'SecurityToken': token
            }

    except Exception as e:
        logger.info(f'get_credentials_from_header error: {e}')
    return credentials