# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/tests/unit/test_safe_join.py
# module: tests.unit.test_safe_join
# qname: tests.unit.test_safe_join.test_safe_join_valid_paths
# lines: 9-27
def test_safe_join_valid_paths():
    """Test safe_join with valid paths that should be allowed"""
    base_dir = tempfile.mkdtemp(prefix="semgrep_scan_")

    # Test basic path joining
    assert safe_join(base_dir, "file.txt") == os.path.realpath(os.path.join(base_dir, "file.txt"))

    # Test with subdirectories
    assert safe_join(base_dir, "subdir/file.txt") == os.path.realpath(
        os.path.join(base_dir, "subdir/file.txt")
    )

    # Test with current directory references
    assert safe_join(base_dir, "./file.txt") == os.path.realpath(os.path.join(base_dir, "file.txt"))

    # Test with multiple subdirectories
    assert safe_join(base_dir, "sub1/sub2/file.txt") == os.path.realpath(
        os.path.join(base_dir, "sub1/sub2/file.txt")
    )