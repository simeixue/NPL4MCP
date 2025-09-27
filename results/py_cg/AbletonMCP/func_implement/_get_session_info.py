# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/AbletonMCP/AbletonMCP_Remote_Script/__init__.py
# module: AbletonMCP_Remote_Script.__init__
# qname: AbletonMCP_Remote_Script.__init__.AbletonMCP._get_session_info
# lines: 342-360
    def _get_session_info(self):
        """Get information about the current session"""
        try:
            result = {
                "tempo": self._song.tempo,
                "signature_numerator": self._song.signature_numerator,
                "signature_denominator": self._song.signature_denominator,
                "track_count": len(self._song.tracks),
                "return_track_count": len(self._song.return_tracks),
                "master_track": {
                    "name": "Master",
                    "volume": self._song.master_track.mixer_device.volume.value,
                    "panning": self._song.master_track.mixer_device.panning.value
                }
            }
            return result
        except Exception as e:
            self.log_message("Error getting session info: " + str(e))
            raise