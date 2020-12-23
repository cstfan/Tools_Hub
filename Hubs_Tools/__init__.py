bl_info = {
    "name": "Hubs Tools",
    "author": "Cstfan",
    "version": (0, 1),
    "blender": (2, 90, 1),
    "location": "View3D > UI > CTS",
    "description": "Switch textures between normal and combined",
    "warning": "",
    "doc_url": "",
    "category": "Material",
}


import bpy

class OBJET_PT_HT(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Texture Switcher Normal/Combined"
    bl_idname = "OBJET_PT_HT"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Hubs Tools"

    def draw(self, context):
        layout = self.layout

        # obj = context.object

        # row = layout.row()
        # row.label(text="Hello world!", icon='WORLD_DATA')

        # row = layout.row()
        # row.label(text="Active object is: " + obj.name)
        # row = layout.row()
        # row.prop(obj, "name")

        row = layout.row()
        row.operator("mesh.primitive_cube_add")


def register():
    bpy.utils.register_class(OBJET_PT_HT)


def unregister():
    bpy.utils.unregister_class(OBJET_PT_HT)


if __name__ == "__main__":
    register()