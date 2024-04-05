import open3d as o3d
import numpy as np

# Create a sample mesh (you can replace this with your own data)
mesh = o3d.geometry.TriangleMesh()
mesh_vertices = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
mesh_triangles = [[0, 1, 2], [1, 2, 3]]
mesh.vertices = o3d.utility.Vector3dVector(mesh_vertices)
mesh.triangles = o3d.utility.Vector3iVector(mesh_triangles)
mesh.paint_uniform_color([1, 0.7, 0.5])
mesh.compute_vertex_normals()

# Render and save the mesh
vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(mesh)
vis.run()
vis.capture_screen_image("mesh_image.png")
vis.destroy_window()