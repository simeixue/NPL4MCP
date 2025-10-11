# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/tests/unit/test_safe_join.py
# module: tests.unit.test_safe_join
# qname: tests.unit.test_safe_join.test_safe_join_with_normalized_base
# lines: 75-85
def test_safe_join_with_normalized_base():
    """Test safe_join handles base directory normalization correctly"""
    # Test with non-normalized base path
    base_dir = tempfile.mkdtemp(prefix="semgrep_scan_")

    # Should normalize the base path
    assert safe_join(base_dir, "file.txt") == os.path.realpath(os.path.join(base_dir, "file.txt"))

    # Should still prevent traversal with normalized base
    with pytest.raises(ValueError, match="Untrusted path escapes the base directory!"):
        safe_join(base_dir, "../file.txt")