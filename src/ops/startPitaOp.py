import bpy

class PR_OT_startPita(bpy.types.Operator):
    bl_idname = "scene.create_pita"
    bl_label = "Make Pita"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("hello 3d world! I am a pita and I am procedural")
        print(__file__)
        return {'FINISHED'}
