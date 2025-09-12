# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_docker_integration.py
# module: tests.test_docker_integration
# qname: tests.test_docker_integration.test_docker_image_runs
# lines: 43-75
def test_docker_image_runs():
    """Test that the Docker image can run and show help."""
    # First build the image
    build_result = subprocess.run(
        ["docker", "build", "-t", "meilisearch-mcp-test", "."],
        capture_output=True,
        text=True,
    )
    if build_result.returncode != 0:
        pytest.skip(f"Docker build failed: {build_result.stderr}")

    # Try to run the container and check it starts
    result = subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "-e",
            "MEILI_HTTP_ADDR=http://localhost:7700",
            "-e",
            "MEILI_MASTER_KEY=test",
            "meilisearch-mcp-test",
            "python",
            "-c",
            "import src.meilisearch_mcp; print('MCP module loaded successfully')",
        ],
        capture_output=True,
        text=True,
        timeout=30,
    )

    assert result.returncode == 0, f"Docker run failed: {result.stderr}"
    assert "MCP module loaded successfully" in result.stdout