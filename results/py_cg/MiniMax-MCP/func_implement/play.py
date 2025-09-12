# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/utils.py
# module: minimax_mcp.utils
# qname: minimax_mcp.utils.play
# lines: 147-170
def play(
    audio: Union[bytes, Iterator[bytes]]
) -> None:
    if isinstance(audio, Iterator):
        audio = b"".join(audio)

    if not is_installed("ffplay"):
        message = (
            "ffplay from ffmpeg not found, necessary to play audio. "
            "mac: install it with 'brew install ffmpeg'. "
            "linux or windows: install it from https://ffmpeg.org/"
        )
        raise ValueError(message)
    
    args = ["ffplay", "-autoexit", "-", "-nodisp"]
    proc = subprocess.Popen(
        args=args,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate(input=audio)

    proc.poll()