# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_docker_integration.py
# module: tests.test_docker_integration
# qname: tests.test_docker_integration.test_docker_build
# lines: 33-40
def test_docker_build():
    """Test that the Docker image can be built successfully."""
    result = subprocess.run(
        ["docker", "build", "-t", "meilisearch-mcp-test", "."],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Docker build failed: {result.stderr}"