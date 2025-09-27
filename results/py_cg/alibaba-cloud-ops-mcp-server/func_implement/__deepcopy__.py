# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/exception.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.exception
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.exception.AcsException.__deepcopy__
# lines: 32-33
    def __deepcopy__(self, memo):
        return self.__class__(**self.kwargs)