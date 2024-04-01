import bpy
import os
from pathlib import Path

class PR_OT_startPita(bpy.types.Operator):
    bl_idname = "scene.create_pita"
    bl_label = "Make Pita"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("hello 3d world! I am a pita and I am procedural")
        falafelPath = Path( os.path.join(__file__, "..", "..", "data", "procedural_pita-falafel_model.blend") ).resolve()
        print(falafelPath)

#        with bpy.data.libraries.load(falafelPath.absolute()) as (data_from, data_to):
#            data_to.objects = data_from.objects
#        
#        for obj in data_to.objects:
#            bpy.context.scene.collection.objects.link(obj)

        with bpy.data.libraries.load(str(falafelPath)) as (data_from, data_to):
            for attr in dir(data_to):
                setattr(data_to, attr, getattr(data_from, attr))

        return {'FINISHED'}
