# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.search_voice_library
# lines: 1013-1069
def search_voice_library(
    page: int = 0,
    page_size: int = 10,
    search: str | None = None,
) -> TextContent:
    response = client.voices.get_shared(
        page=page,
        page_size=page_size,
        search=search,
    )

    if not response.voices:
        return TextContent(
            type="text", text="No shared voices found with the specified criteria."
        )

    voice_list = []
    for voice in response.voices:
        language_info = "N/A"
        if hasattr(voice, "verified_languages") and voice.verified_languages:
            languages = []
            for lang in voice.verified_languages:
                accent_info = (
                    f" ({lang.accent})"
                    if hasattr(lang, "accent") and lang.accent
                    else ""
                )
                languages.append(f"{lang.language}{accent_info}")
            language_info = ", ".join(languages)

        details = [
            f"Name: {voice.name}",
            f"ID: {voice.voice_id}",
            f"Category: {getattr(voice, 'category', 'N/A')}",
        ]
        # TODO: Make cleaner
        if hasattr(voice, "gender") and voice.gender:
            details.append(f"Gender: {voice.gender}")
        if hasattr(voice, "age") and voice.age:
            details.append(f"Age: {voice.age}")
        if hasattr(voice, "accent") and voice.accent:
            details.append(f"Accent: {voice.accent}")
        if hasattr(voice, "description") and voice.description:
            details.append(f"Description: {voice.description}")
        if hasattr(voice, "use_case") and voice.use_case:
            details.append(f"Use Case: {voice.use_case}")

        details.append(f"Languages: {language_info}")

        if hasattr(voice, "preview_url") and voice.preview_url:
            details.append(f"Preview URL: {voice.preview_url}")

        voice_info = "\n".join(details)
        voice_list.append(voice_info)

    formatted_info = "\n\n".join(voice_list)
    return TextContent(type="text", text=f"Shared Voices:\n\n{formatted_info}")