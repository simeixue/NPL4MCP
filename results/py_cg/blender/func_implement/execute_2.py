# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/blender/addon.py
# module: addon
# qname: addon.BLENDERMCP_OT_StopServer.execute
# lines: 1759-1769
    def execute(self, context):
        scene = context.scene

        # Stop the server if it exists
        if hasattr(bpy.types, "blendermcp_server") and bpy.types.blendermcp_server:
            bpy.types.blendermcp_server.stop()
            del bpy.types.blendermcp_server

        scene.blendermcp_server_running = False

        return {'FINISHED'}