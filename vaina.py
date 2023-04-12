import bpy
from bpy.props import FloatProperty
from bpy.types import Operator, Panel
from test_panel import CleanCurvesPanel

def clean_animation_curves(obj, threshold):
    if obj.animation_data:
        action = obj.animation_data.action
        if action:
            for fcurve in action.fcurves:
                prev_keyframe = None
                keyframes_to_remove = []

                for i, keyframe in enumerate(fcurve.keyframe_points):
                    if prev_keyframe:
                        difference = abs(keyframe.co[1] - prev_keyframe.co[1])
                        if difference < threshold:
                            keyframes_to_remove.append(i)
                    prev_keyframe = keyframe

                for i in reversed(keyframes_to_remove):
                    fcurve.keyframe_points.remove(fcurve.keyframe_points[i])

class CleanCurvesOperator(Operator):
    bl_idname = "object.clean_animation_curves"
    bl_label = "Clean Animation Curves"
    bl_options = {"REGISTER", "UNDO"}

    threshold: FloatProperty(
        name="Threshold",
        description="Threshold to determine if a keyframe should be removed",
        default=0.01,
        min=0.0,
    )




    def draw(self, context):
        layout = self.layout
        layout.operator(CleanCurvesOperator.bl_idname)

classes = (CleanCurvesOperator, CleanCurvesPanel)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()