# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/tests/unit/test_safe_join.py
# module: tests.unit.test_safe_join
# qname: tests.unit.test_safe_join.test_safe_join_path_traversal_attempts
# lines: 30-48
def test_safe_join_path_traversal_attempts():
    """Test safe_join blocks path traversal attempts"""
    base_dir = tempfile.mkdtemp(prefix="semgrep_scan_")

    # Test simple parent directory traversal
    with pytest.raises(ValueError, match="Untrusted path escapes the base directory!"):
        safe_join(base_dir, "../file.txt")

    # Test nested parent directory traversal
    with pytest.raises(ValueError, match="Untrusted path escapes the base directory!"):
        safe_join(base_dir, "subdir/../../file.txt")

    # Test absolute path attempt
    with pytest.raises(ValueError, match="Untrusted path must be relative"):
        safe_join(base_dir, "/etc/passwd")

    # Test complex traversal with current directory references
    with pytest.raises(ValueError, match="Untrusted path escapes the base directory!"):
        safe_join(base_dir, "./subdir/../../../file.txt")