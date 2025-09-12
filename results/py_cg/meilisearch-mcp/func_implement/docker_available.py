# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_docker_integration.py
# module: tests.test_docker_integration
# qname: tests.test_docker_integration.docker_available
# lines: 13-24
def docker_available():
    """Check if Docker is available on the system."""
    if not shutil.which("docker"):
        return False
    # Try to run docker version to ensure it's working
    try:
        result = subprocess.run(
            ["docker", "version"], capture_output=True, text=True, timeout=5
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False