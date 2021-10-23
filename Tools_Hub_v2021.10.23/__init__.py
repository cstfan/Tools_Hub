import bpy
# from . import selection_sets
from bpy.types import Scene
from bpy.props import (
    BoolProperty,
    StringProperty
)

bl_info = {
    "name": "Tools Hub",
    "author": "Cstfan and V!nc3r for his precious help",
    "version": (2021, 10, 23),
    "blender": (2, 93, 5),
    "location": "View3D > UI > Tools Hub",
    "description": "Panel with tools",
    "warning": "",
    "doc_url": "",
    "category": "Material",
}

"""
**********************************************************************
*                            local variables                         *
**********************************************************************
"""

"""
**********************************************************************
*                            def section                             *
**********************************************************************
"""


def material_output(outputlabel):
    """ Select Material Output by using Label
    """
    output_label = outputlabel

    if len(bpy.context.view_layer.objects.selected) > 0:
        for obj in bpy.context.view_layer.objects.selected:
            if len(obj.data.materials) > 0:
                for mat in obj.data.materials:
                    for node in mat.node_tree.nodes:
                        if node.type != 'OUTPUT_MATERIAL':
                            continue
                        node.is_active_output = False
                        if node.label == output_label:
                            node.is_active_output = True


"""
**********************************************************************
*                       Panel class section                          *
**********************************************************************
"""


class TOOLSHUB_PT_material_3dviewPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tools Hub"


class TOOLSHUB_PT_material(TOOLSHUB_PT_material_3dviewPanel):
    """Creates a Panel in the Object properties window"""
    bl_idname = "TOOLSHUB_PT_material"
    bl_label = "Tools Hub - Materials"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.prop(context.scene, "toolshub_material_check_only_selected",
                 text="only on selection")


class TOOLSHUB_PT_material_output(TOOLSHUB_PT_material_3dviewPanel):
    bl_parent_id = "TOOLSHUB_PT_material"
    bl_idname = "TOOLSHUB_PT_material_output"
    bl_label = "Select Output Label"

    def draw(self, context):
        layout = self.layout

        if (
            not bpy.context.scene.toolshub_material_check_only_selected
            or (
                bpy.context.scene.toolshub_material_check_only_selected
                and len(bpy.context.selected_objects) > 0
            )
        ):

            # Select Output Label
            row = layout.row(align=True)
            row.operator("toolshub.material_output", text="Default").outputlabel = ""
            row.operator("toolshub.material_output", text="PBR").outputlabel = "PBR"
            row.operator("toolshub.material_output", text="Combined").outputlabel = "Combined"
            row.operator("toolshub.material_output", text="IDMap").outputlabel = "IDMap"


"""
**********************************************************************
*                       Operator class section                       *
**********************************************************************
"""


class TOOLSHUB_OT_material_output(bpy.types.Operator):
    bl_idname = "toolshub.material_output"
    bl_label = "Switch Material Output"
    bl_description = "Switch Material Output (Default Label must be Empty)"
    outputlabel: StringProperty()

    def execute(self, context):
        material_output(self.outputlabel)
        return {'FINISHED'}


"""
*********************************************************************
*                           Registration                            *
*********************************************************************
"""

classes = (
    TOOLSHUB_PT_material,
    TOOLSHUB_PT_material_output,
    TOOLSHUB_OT_material_output,
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    Scene.toolshub_material_check_only_selected = BoolProperty(
        name="Material tab use selected only",
        description="Material operations applies on selection, or not",
        default=True
    )


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del Scene.toolshub_material_check_only_selected


if __name__ == "__main__":
    register()
