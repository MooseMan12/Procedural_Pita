import bpy

bl_info = {
    "name": "Procedural Pita",
    "version": (0,1),
    "blender": (4,1,0),
    "location": "Toolshelf",
    "category": "Object",
    "description": "creates a procedural pita and lets the user customize the pita and the toppings of said pita."
}

class PR_OT_startPita(bpy.types.Operator):
    bl_idname = "scene.create_pita"
    bl_label = "Make Pita"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("hello 3d world! I am a pita and I am procedural")
        print(__file__)
        return {'FINISHED'}


class PitaToolshelfPanel(bpy.types.Panel):
    bl_label = "Procedural Pita"
    bl_idname = "OBJECT_PT_Procedural_Pita"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Procedural Pita"

    def draw(self, context):

        # column buttons solution. Less space than single buttons ...
        layout = self.layout
        view = context.space_data
        # Three buttons
        col = layout.column(align=True)
        col.separator()
        col.label(text="hello 3d world")
        col.operator("scene.create_pita", text="Make Pita!")
  
  
classes = (PitaToolshelfPanel,PR_OT_startPita, )

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()