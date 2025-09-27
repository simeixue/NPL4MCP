# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/alibabacloud/exception.py
# module: src.alibaba_cloud_ops_mcp_server.alibabacloud.exception
# qname: src.alibaba_cloud_ops_mcp_server.alibabacloud.exception.AcsException.__init__
# lines: 13-23
    def __init__(self, **kwargs):
        self.kwargs = kwargs

        try:
            self.message = self.msg_fmt.format(**kwargs) if kwargs else self.msg_fmt
            if isinstance(self.message, str):
                self.message = self.message.rstrip('.') + '.'
        except KeyError:
            logger.exception(f'Exception in string format operation: {self.code}, {self.msg_fmt}, {kwargs}')
            for name, value in kwargs.items():
                logger.error(f'{name}: {value}')