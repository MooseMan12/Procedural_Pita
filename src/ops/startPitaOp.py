import bpy
import os
import math
import random
from mathutils import Vector
from pathlib import Path

class PR_OT_startPita(bpy.types.Operator):
    bl_idname = "scene.create_pita"
    bl_label = "Make Pita"
    bl_options = {'REGISTER', 'UNDO'}
    falafel_type: bpy.props.EnumProperty(items = (
        ('falafel', 'Falafel', 'a regular falafel'),
        ('burnt_falafel', 'Burnt Falafel', 'a burnt, slightly darker, falafel'),
        ('raw_falafel', 'Raw Falafel', 'a rawer, slightly lighter, falafel')
    ),
    name = "Falafel Type", description = 'here you can choose what kind of falafel you want: burnt, raw, or regular', default = 'falafel', options={'ANIMATABLE'}, override=set(), tags=set(), update=None, get=None, set=None)
    falafel_count: bpy.props.IntProperty(name = "falafel amount", default = 1, min = 0, max = 7)

    moveArr = [[0,0],[1,0],[1,-1],[-1,-1],[-1,0],[-1,1],[1,1]]

    def falafelOffset(self, index, r):
        move = self.moveArr[index]
        offsetZ = move[1] * (math.sqrt(3) * r)
        offsetX = 0
        if move[1] ==0:
            offsetX = move[0] * (2 * r)
        else:
            offsetX = move[0] * r
        return Vector((offsetX,0,offsetZ))

    def execute(self, context):
        print("hello 3d world! I am a pita and I am procedural")
        modelspath = Path( os.path.join(__file__, "..", "..", "data", "models.blend") ).resolve()
        print(modelspath)

        with bpy.data.libraries.load(str(modelspath)) as (data_from, data_to):
            data_to.objects = [self.falafel_type]
            print("objects are: ", data_to.objects)
        
        if self.falafel_count != 0:
            bpy.context.scene.collection.objects.link(data_to.objects[0])
            falafelObj = data_to.objects[0]
            falafelR = falafelObj.dimensions.x / 2
            falafelObj.location = context.scene.cursor.location
            falafelObj.rotation_euler = (random.randint(0,360),random.randint(0,360),random.randint(0,360))

            for i in range(self.falafel_count-1):
                falafelObj_new = falafelObj.copy()
                falafelObj_new.location = context.scene.cursor.location + self.falafelOffset(i+1, falafelR)
                falafelObj_new.rotation_euler = (random.randint(0,360),random.randint(0,360),random.randint(0,360))
                context.scene.collection.objects.link(falafelObj_new)
        
        return {'FINISHED'}
 
