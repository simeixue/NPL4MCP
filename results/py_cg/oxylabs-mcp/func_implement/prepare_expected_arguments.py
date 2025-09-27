# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/utils.py
# module: tests.utils
# qname: tests.utils.prepare_expected_arguments
# lines: 16-20
def prepare_expected_arguments(arguments: dict) -> dict:
    arguments_copy = {**arguments}
    if "output_format" in arguments_copy:
        del arguments_copy["output_format"]
    return arguments_copy