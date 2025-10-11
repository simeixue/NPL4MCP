# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/tests/unit/test_safe_join.py
# module: tests.unit.test_safe_join
# qname: tests.unit.test_safe_join.test_safe_join_edge_cases
# lines: 51-72
def test_safe_join_edge_cases():
    """Test safe_join with edge cases"""
    base_dir = tempfile.mkdtemp(prefix="semgrep_scan_")

    # Test empty path
    assert safe_join(base_dir, "") == os.path.realpath(base_dir)

    # Test current directory
    assert safe_join(base_dir, ".") == os.path.realpath(base_dir)

    # Test path with only slashes
    assert safe_join(base_dir, "///") == os.path.realpath(base_dir)

    # Test path with spaces and special characters
    assert safe_join(base_dir, "my file with spaces.txt") == os.path.realpath(
        os.path.join(base_dir, "my file with spaces.txt")
    )

    # Test path with unicode characters
    assert safe_join(base_dir, "üñîçødé_fïlé.txt") == os.path.realpath(
        os.path.join(base_dir, "üñîçødé_fïlé.txt")
    )