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



# import bpy 
# path = "/Users/bairy/Library/Application Support/Blender/4.1/scripts/addons/src/data/models.blend"

# def approach1(): 
#     with bpy.data.libraries.load(path) as (data_from, data_to):
#         files = []
#         for obj in data_from.objects:
#             files.append({'name':obj})
#         print( files )
#         bpy.ops.wm.append(directory=path+'\\Object\\', files = files)

# def approach2():
#     with bpy.data.libraries.load(path) as (data_from, data_to):
#         data_to.objects = [name for name in data_from.objects]
#         print("objects are: ", data_to.objects)
        
#     for obj in data_to.objects:
#         print(dir(bpy.context.scene.collection))
#         bpy.context.scene.collection.objects.link(obj)
        

# approach2()

