# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/utils.py
# module: src.semgrep_mcp.utilities.utils
# qname: src.semgrep_mcp.utilities.utils.set_semgrep_executable
# lines: 181-183
def set_semgrep_executable(semgrep_path: str) -> None:
    global SEMGREP_EXECUTABLE
    SEMGREP_EXECUTABLE = semgrep_path