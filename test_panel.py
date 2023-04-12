import bpy
from vaina import clean_animation_curves

class CleanCurvesPanel(bpy.types.Panel):
    bl_label = "Clean Animation Curves"
    bl_idname = "OBJECT_PT_clean_animation_curves"
    bl_space_type = "PROPERTIES"
    bl_region_type = "UI"
    bl_context = "data"

# label is visible when you press the "END" key

    def execute(self, context):
        obj = context.active_object
        clean_animation_curves(obj, self.threshold)
        return {"FINISHED"}
