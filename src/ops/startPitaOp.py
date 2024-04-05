import bpy
import os
from pathlib import Path

class PR_OT_startPita(bpy.types.Operator):
    bl_idname = "scene.create_pita"
    bl_label = "Make Pita"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("hello 3d world! I am a pita and I am procedural")
        modelspath = Path( os.path.join(__file__, "..", "..", "data", "models.blend") ).resolve()
        print(modelspath)

        with bpy.data.libraries.load(str(modelspath)) as (data_from, data_to):
            data_to.meshes = data_from.meshes

        return {'FINISHED'}
