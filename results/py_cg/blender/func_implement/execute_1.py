# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/blender/addon.py
# module: addon
# qname: addon.BLENDERMCP_OT_StartServer.execute
# lines: 1740-1751
    def execute(self, context):
        scene = context.scene

        # Create a new server instance
        if not hasattr(bpy.types, "blendermcp_server") or not bpy.types.blendermcp_server:
            bpy.types.blendermcp_server = BlenderMCPServer(port=scene.blendermcp_port)

        # Start the server
        bpy.types.blendermcp_server.start()
        scene.blendermcp_server_running = True

        return {'FINISHED'}