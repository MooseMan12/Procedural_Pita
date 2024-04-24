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
    falafel_count: bpy.props.IntProperty(name = "falafel amount", default = 7, min = 0, max = 7)
    tomato_amount: bpy.props.IntProperty(name = "tomato amount", default = 4, min = 0, max = 4)

#                       [x,z]
    falafelMoveArr = [[0,0],[1,0],[1,-1],[-1,-1],[-1,0],[-1,1],[1,1]]
#                   [x,y,z]
    tomatoMoveArr = [[-1,1,0],[1,1,1],[-1,-1,1],[1,-1,0]]

    def falafelOffset(self, index, r):
        move = self.falafelMoveArr[index]
        offsetZ = move[1] * (math.sqrt(3) * r)
        offsetX = 0
        if move[1] ==0:
            offsetX = move[0] * (2 * r)
        else:
            offsetX = move[0] * r
        return Vector((offsetX,0,offsetZ))

    def tomatoOffset(self, tomato_index, r, tomatoHeight):
        tomato_move = self.tomatoMoveArr[tomato_index]
        tomatoXOffset = r * tomato_move[0]
        tomatoYOffset = (r + (tomatoHeight * 0.5)) * tomato_move[1]
        tomatoZOffset = r * tomato_move[2]
        return Vector((tomatoXOffset,tomatoYOffset,tomatoZOffset))

    def execute(self, context):
        modelspath = Path( os.path.join(__file__, "..", "..", "data", "models.blend") ).resolve()
        #print(modelspath)

        with bpy.data.libraries.load(str(modelspath)) as (data_from, data_to):
            data_to.objects = [self.falafel_type, 'tomato_1', 'tomato_2']
            #print("objects are: ", data_to.objects)

        falafelR = 0.2

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
        

        if self.tomato_amount != 0:
            bpy.context.scene.collection.objects.link(data_to.objects[1])
            TomatoObj = data_to.objects[1]
            TomatoHeight = TomatoObj.dimensions.z
            TomatoObj.location = context.scene.cursor.location + self.tomatoOffset(0, falafelR, TomatoHeight)
            TomatoObj.rotation_euler = (0,math.pi*0.5,-(math.pi*0.5))

            for i in range(self.tomato_amount-1):
                tomatoObj_new = TomatoObj.copy()
                tomatoObj_new.location = context.scene.cursor.location + self.tomatoOffset(i+1, falafelR, TomatoHeight)
                context.scene.collection.objects.link(tomatoObj_new)
        
        return {'FINISHED'}
 
