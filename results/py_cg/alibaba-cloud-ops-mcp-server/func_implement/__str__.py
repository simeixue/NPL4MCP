# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/exception.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.exception
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.exception.AcsException.__str__
# lines: 25-30
    def __str__(self):
        body = {
            'Message': self.message,
            'Code': self.code
        }
        return json.dumps(body)