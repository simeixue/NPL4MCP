# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/tests/test_utils.py
# module: tests.test_utils
# qname: tests.test_utils.test_handle_input_file
# lines: 77-89
def test_handle_input_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        test_file = temp_path / "test.mp3"

        with open(test_file, "wb") as f:
            f.write(b"\xff\xfb\x90\x64\x00")

        result = handle_input_file(str(test_file))
        assert result == test_file

        with pytest.raises(ElevenLabsMcpError):
            handle_input_file(str(temp_path / "nonexistent.mp3"))