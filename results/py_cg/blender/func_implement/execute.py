# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/blender/addon.py
# module: addon
# qname: addon.BLENDERMCP_OT_SetFreeTrialHyper3DAPIKey.execute
# lines: 1728-1732
    def execute(self, context):
        context.scene.blendermcp_hyper3d_api_key = RODIN_FREE_TRIAL_KEY
        context.scene.blendermcp_hyper3d_mode = 'MAIN_SITE'
        self.report({'INFO'}, "API Key set successfully!")
        return {'FINISHED'}