import bpy

# Get all curve objects in the scene
curve_objects = [obj for obj in bpy.context.scene.objects if obj.type == 'CURVE']

# Iterate through curve objects
for obj in curve_objects:
    # Check if the curve object has hook modifiers
    if obj.modifiers:
        # Iterate through modifiers of the object
        for modifier in obj.modifiers:
            # Check if the modifier is a hook modifier
            if modifier.type == 'HOOK':
                # Set the active object and select the object with the modifier
                bpy.context.view_layer.objects.active = obj
                obj.select_set(True)
                
                # Reset the hook modifier
                bpy.ops.object.hook_reset(modifier=modifier.name)

                # Clear the selection
                bpy.context.view_layer.objects.active = None
                obj.select_set(False)
