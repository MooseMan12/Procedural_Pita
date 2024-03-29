bl_info = {
    "name": "cursor array",
    "Blender": (3,6,0),
    "category": "Object"
}


import bpy
from bpy import context

class ObjectCursorArray(bpy.types.Operator):
    """Object Cursor Array"""
    
    
    bl_idname = "object.cursor_array"
    bl_label = "cursor array"
    bl_options = {"REGISTER", "UNDO"}
    total: bpy.props.IntProperty(name = "steps", default = 2, min = 1, max = 100)
    rotations_X: bpy.props.IntProperty(name = "rotations on x axis", default = 1, min = 0, max = 20)
    rotations_Y: bpy.props.IntProperty(name = "rotations on y axis", default = 1, min = 0, max = 20)
    rotations_Z: bpy.props.IntProperty(name = "rotations on z axis", default = 1, min = 0, max = 20)
    obj_type: bpy.props.EnumProperty(items = (
            ('cube', 'Cube', 'abc'),
            ('monkey', 'Monkey - Susan', 'abc'),
            ('cone', 'Cone', 'abc'),
            ('ico sphere', 'Ico Sphere', 'abc')
        ),
        name = "Object type", description = '', default = 'cube', options={'ANIMATABLE'}, override=set(), tags=set(), update=None, get=None, set=None)
    #cursor_location: bpy.props.IntVectorProperty(name='3d cursor location', description='', default=(0, 0, 0), min=-2**31, max=2**31 - 1, soft_min=-2**31, soft_max=2**31 - 1, step=1, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', size=3, update=None, get=None, set=None)
    
    def execute(self, context):
        scene = context.scene
        cursor = scene.cursor.location
        #cursor = self.cursor_location
        obj = context.active_object
        if obj == None:
            match self.obj_type:
                case 'cube':
                    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                case 'monkey':
                    bpy.ops.mesh.primitive_monkey_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                case 'cone':
                    bpy.ops.mesh.primitive_cone_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                case 'ico sphere':
                    bpy.ops.mesh.primitive_ico_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
            obj = context.active_object
        else:
            bpy.ops.object.delete(use_global=False)
            match self.obj_type:
                case 'cube':
                    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                case 'monkey':
                    bpy.ops.mesh.primitive_monkey_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                case 'cone':
                    bpy.ops.mesh.primitive_cone_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                case 'ico sphere':
                    bpy.ops.mesh.primitive_ico_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
            obj = context.active_object


        # Add 'total' objects into the scene
        for i in range(self.total):
            obj_new = obj.copy()
            scene.collection.objects.link(obj_new)

            # Now place the object in between the cursor
            # and the active object based on 'i'
            factor = i / self.total
            obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))
            obj_new.rotation_euler = (360*self.rotations_X*factor, 360*self.rotations_Y*factor, 360*self.rotations_Z*factor)
        
        return {"FINISHED"}
    
    
def menu_func(self, context):
    self.layout.operator(ObjectCursorArray.bl_idname)

addon_keymaps = []

def register():
    bpy.utils.register_class(ObjectCursorArray)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
    # handle the keymap
    wm = bpy.context.window_manager
    # Note that in background mode (no GUI available), keyconfigs are not available either,
    # so we have to check this to avoid nasty errors in background case.
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new(ObjectCursorArray.bl_idname, 'T', 'PRESS', ctrl=True, shift=True)
        kmi.properties.total = 4
        addon_keymaps.append((km, kmi))
        kmi = km.keymap_items.new(ObjectCursorArray.bl_idname, 'T', 'PRESS', ctrl=True, shift=True, alt=True)
        kmi.properties.total = 50
        addon_keymaps.append((km, kmi))

def unregister():
        # Note: when unregistering, it's usually good practice to do it in reverse order you registered.
    # Can avoid strange issues like keymap still referring to operators already unregistered...
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(ObjectCursorArray)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    
if __name__ == "__main__":
    register()
    