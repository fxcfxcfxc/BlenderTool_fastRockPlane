import bpy
import bmesh


bpy.ops.mesh.select_mode(type= 'FACE')
obj = bpy.context.edit_object
me = obj.data
bm = bmesh.from_edit_mesh(me)


qh_face = bm.faces
for a in qh_face :
    
    a.select = True
    bmesh.update_edit_mesh(me, True)
    bpy.ops.mesh.select_linked(delimit={'SHARP'})
    bpy.ops.mesh.looptools_flatten(influence=100, lock_x=False, lock_y=False, lock_z=False, plane='best_fit', restriction='none')
    bpy.ops.mesh.select_all(action='DESELECT')
   
else:
    print("没有循环数据!")    