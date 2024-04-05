import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

import open3d as o3d
import numpy as np

class Open3DWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mesh = None

    def create_mesh(self):
        # Create a sample mesh (you can replace this with your own data)
        mesh = o3d.geometry.TriangleMesh()
        mesh_vertices = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
        mesh_triangles = [[0, 1, 2], [1, 2, 3]]
        mesh.vertices = o3d.utility.Vector3dVector(mesh_vertices)
        mesh.triangles = o3d.utility.Vector3iVector(mesh_triangles)
        mesh.paint_uniform_color([1, 0.7, 0.5])
        mesh.compute_vertex_normals()

        self.mesh = mesh

    def render_mesh(self):
        if self.mesh is None:
            self.create_mesh()

        vis = o3d.visualization.Visualizer()
        vis.create_window(width=int(Window.width), height=int(Window.height))
        vis.add_geometry(self.mesh)
        vis.run()
        vis.destroy_window()

class TabletApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        label = Label(text='Press the button to render 3D mesh using Open3D')
        root.add_widget(label)

        open3d_widget = Open3DWidget()
        root.add_widget(open3d_widget)

        button = Button(text='Render 3D Mesh')
        button.bind(on_press=self.render_3d_mesh)
        root.add_widget(button)

        return root

    def render_3d_mesh(self, instance):
        instance.disabled = True
        instance.text = 'Rendering...'
        self.root.children[1].render_mesh()
        instance.text = 'Rendered!'

if __name__ == '__main__':
    TabletApp().run()
