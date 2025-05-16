import bpy

bones_to_delete = ["butt_ref_l", "butt_ref_r", "breast_01_ref.l", "breast_01_ref.r", "breast_02_ref.l", "breast_02_ref.r", "belly_02_ref", "belly_01_ref"]

ob = bpy.context.object

if ob.type == 'ARMATURE':
    armature = ob.data

bpy.ops.object.mode_set(mode='EDIT')

for bone in armature.edit_bones:
    if bone.name in bones_to_delete:
        armature.edit_bones.remove(bone)

bpy.ops.object.mode_set(mode='OBJECT')