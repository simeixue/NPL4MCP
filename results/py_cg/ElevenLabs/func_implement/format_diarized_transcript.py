# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.format_diarized_transcript
# lines: 63-141
def format_diarized_transcript(transcription) -> str:
    """Format transcript with speaker labels from diarized response."""
    try:
        # Try to access words array - the exact attribute might vary
        words = None
        if hasattr(transcription, "words"):
            words = transcription.words
        elif hasattr(transcription, "__dict__"):
            # Try to find words in the response dict
            for key, value in transcription.__dict__.items():
                if key == "words" or (
                    isinstance(value, list)
                    and len(value) > 0
                    and (
                        hasattr(value[0], "speaker_id")
                        if hasattr(value[0], "__dict__")
                        else (
                            "speaker_id" in value[0]
                            if isinstance(value[0], dict)
                            else False
                        )
                    )
                ):
                    words = value
                    break

        if not words:
            return transcription.text

        formatted_lines = []
        current_speaker = None
        current_text = []

        for word in words:
            # Get speaker_id - might be an attribute or dict key
            word_speaker = None
            if hasattr(word, "speaker_id"):
                word_speaker = word.speaker_id
            elif isinstance(word, dict) and "speaker_id" in word:
                word_speaker = word["speaker_id"]

            # Get text - might be an attribute or dict key
            word_text = None
            if hasattr(word, "text"):
                word_text = word.text
            elif isinstance(word, dict) and "text" in word:
                word_text = word["text"]

            if not word_speaker or not word_text:
                continue

            # Skip spacing/punctuation types if they exist
            if hasattr(word, "type") and word.type == "spacing":
                continue
            elif isinstance(word, dict) and word.get("type") == "spacing":
                continue

            if current_speaker != word_speaker:
                # Save previous speaker's text
                if current_speaker and current_text:
                    speaker_label = current_speaker.upper().replace("_", " ")
                    formatted_lines.append(f"{speaker_label}: {' '.join(current_text)}")

                # Start new speaker
                current_speaker = word_speaker
                current_text = [word_text.strip()]
            else:
                current_text.append(word_text.strip())

        # Add final speaker's text
        if current_speaker and current_text:
            speaker_label = current_speaker.upper().replace("_", " ")
            formatted_lines.append(f"{speaker_label}: {' '.join(current_text)}")

        return "\n\n".join(formatted_lines)

    except Exception:
        # Fallback to regular text if something goes wrong
        return transcription.text