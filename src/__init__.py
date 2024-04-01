import bpy

bl_info = {
    "name": "Procedural Pita",
    "version": (0,1),
    "blender": (4,1,0),
    "location": "Toolshelf",
    "category": "Object",
    "description": "creates a procedural pita and lets the user customize the pita and the toppings of said pita."
}

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
  
  
def register():
    from src.ops.startPitaOp import PR_OT_startPita
    bpy.utils.register_class(PitaToolshelfPanel)
    bpy.utils.register_class(PR_OT_startPita)

def unregister():
    from src.ops.startPitaOp import PR_OT_startPita
    bpy.utils.unregister_class(PR_OT_startPita)
    bpy.utils.unregister_class(PitaToolshelfPanel)

if __name__ == "__main__":
    register()