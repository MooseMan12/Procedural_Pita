import bpy
import os
from pathlib import Path

class PR_OT_startPita(bpy.types.Operator):
    bl_idname = "scene.create_pita"
    bl_label = "Make Pita"
    bl_options = {'REGISTER', 'UNDO'}
    falafel_type: bpy.props.EnumProperty(items = (
        ('falafel', 'Falafel', 'a regular falafel'),
        ('burnt_falafel', 'Burnt Falafel', 'a burnt, slightly darker, falafel'),
        ('raw_falafel', 'Raw Falafel', 'a more raw, lighter, falafel')
    ),
    name = "Falafel Type", description = 'here you can choose what kind of falafel you want: burnt, raw, or regular', default = 'falafel', options={'ANIMATABLE'}, override=set(), tags=set(), update=None, get=None, set=None)
    falafel_count: bpy.props.IntProperty(name = "falafel amount", default = 1, min = 0, max = 4)

    def execute(self, context):
#        print("hello 3d world! I am a pita and I am procedural")
        modelspath = Path( os.path.join(__file__, "..", "..", "data", "models.blend") ).resolve()
        print(modelspath)

        with bpy.data.libraries.load(str(modelspath)) as (data_from, data_to):
            data_to.objects = [self.falafel_type]
            print("objects are: ", data_to.objects)
        
        bpy.context.scene.collection.objects.link(data_to.objects[0])
        falafelObj = data_to.objects[0]
        falafelObj.location = context.scene.cursor.location

        for i in range(self.falafel_count):
            falafelObj_new = falafelObj.copy()
            context.scene.collection.objects.link(falafelObj_new)
            falafelObj_new.location = falafelObj.location
        
        return {'FINISHED'}
 