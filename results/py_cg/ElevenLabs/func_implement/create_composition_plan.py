# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.create_composition_plan
# lines: 1168-1179
def create_composition_plan(
    prompt: str,
    music_length_ms: int | None = None,
    source_composition_plan: MusicPrompt | None = None,
) -> MusicPrompt:
    composition_plan = client.music.composition_plan.create(
        prompt=prompt,
        music_length_ms=music_length_ms,
        source_composition_plan=source_composition_plan,
    )

    return composition_plan