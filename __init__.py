# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.



import bpy
import bmesh


#blender插件信息11
bl_info = {
    "name" : "test",
    "author" : "fxc",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}



#创建面片
class TEST_OT_hello(bpy.types.Operator):
    bl_idname = "triangle.hello"
    bl_label = "hello"



    def execute(self, context):

       
        bpy.ops.mesh.primitive_plane_add(enter_editmode=False, location=(0, 0, 0), rotation=(1.5708, 0, 0), scale=(1, 1, 1))
  

        return {"FINISHED"}



class TEST1_OT_hello(bpy.types.Operator):
    bl_idname = "triangle.hello1"
    bl_label = "hello"



    def execute(self, context):

        bpy.ops.mesh.primitive_plane_add(enter_editmode=False, location=(0, 0, 0), rotation=(0, 1.5708, 0), scale=(1, 1, 1))
    
        
        return {"FINISHED"}



class TEST2_OT_hello(bpy.types.Operator):
    bl_idname = "triangle.hello2"
    bl_label = "hello"



    def execute(self, context):

        
     
        
        bpy.ops.mesh.primitive_plane_add(enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 1.5708), scale=(1, 1, 1))
        
        return {"FINISHED"}


#-------------烘培重命名------------------

class Bake_OT_rename(bpy.types.Operator):
    bl_idname = "triangle.rename"
    bl_label = "rename"
   

    def execute(self, context):

        count = len(bpy.context.selected_objects)

        if  count == 2:

            me00 = bpy.context.selected_objects[0]
            me01 = bpy.context.selected_objects[1]

            a = len( me00.data.polygons)
            b = len( me01.data.polygons)
            var1 = me00.name
            var2 = me01.name
            if a < b :
               
                me00.name = var1 + "_low"
                me01.name = var1 + "_high"

            else:
            
                me00.name = var2 + "_high"
                me01.name = var2 + "_low"


        
        return {"FINISHED"}






#终极打平面工具
class  Face_OT_plane(bpy.types.Operator):
    bl_idname = "triangle.keeplane"
    bl_label = "keeplane"


    def execute(self, context):
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
            print("结束")

        return {"FINISHED"}

        
#-------------界面ui绘制---------------------
class Test_PT_view3d(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "ADD_OBJECT"
    bl_idname = "view3d test"

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "mesh_edit"

    bl_category = "Test"

    def draw(self, context):#在面板中绘制ui方法
        layout = self.layout
        
        #
        layout.label(text="ADD_plane")
        row = layout.row()
        row.operator("triangle.hello",text="x",icon = "CUBE") 
        row.operator("triangle.hello1",text="y",icon = "CUBE") 
        row.operator("triangle.hello2",text="z",icon = "CUBE") 
        

        #
        layout.label(text="Bake_Rename")
        row = layout.row()

        row.operator("triangle.rename",text="Rename") 


        layout.label(text="硬边面工具打平")
        row = layout.row()

        row.operator("triangle.keeplane",text="硬边面打平")







#注册
def register():

    bpy.utils.register_class(TEST_OT_hello)
    bpy.utils.register_class(TEST1_OT_hello)
    bpy.utils.register_class(TEST2_OT_hello)
    bpy.utils.register_class(Test_PT_view3d)
    bpy.utils.register_class(Bake_OT_rename)
    bpy.utils.register_class(Face_OT_plane)
    
    ...

def unregister():
    bpy.utils.unregister_class(TEST_OT_hello)
    bpy.utils.unregister_class(TEST1_OT_hello)
    bpy.utils.unregister_class(TEST2_OT_hello)
    bpy.utils.unregister_class(Test_PT_view3d)
    bpy.utils.unregister_class(Bake_OT_rename)
    bpy.utils.unregister_class(Face_OT_plane)
   


    ...
