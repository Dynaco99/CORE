import trimesh
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Path to your .obj file
obj_file_path = r"C:\Users\minke\OneDrive\Desktop\mesh.obj"  # Ensure this path is correct

# Check if the file exists
if not os.path.exists(obj_file_path):
    print(f"The file does not exist: {obj_file_path}")
else:
    try:
        # Load the mesh from the .obj file
        mesh = trimesh.load(obj_file_path)

        # Check if the mesh is empty
        if mesh.is_empty:
            raise ValueError("The mesh is empty or failed to load.")

        # Print basic information about the mesh
        print("Is the mesh watertight?:", mesh.is_watertight)
        print("Number of vertices:", mesh.vertices.shape[0])
        print("Number of faces:", mesh.faces.shape[0])

        # Visualize the mesh using Matplotlib
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Extract vertices and faces
        vertices = mesh.vertices
        faces = mesh.faces

        # Create a Poly3DCollection from the faces
        poly3d = [[vertices[vertice] for vertice in face] for face in faces]
        collection = Poly3DCollection(poly3d, alpha=0.5, edgecolor='k')  # Add edges with black color
        ax.add_collection3d(collection)

        # Set limits and labels
        ax.set_xlim(vertices[:, 0].min(), vertices[:, 0].max())
        ax.set_ylim(vertices[:, 1].min(), vertices[:, 1].max())
        ax.set_zlim(vertices[:, 2].min(), vertices[:, 2].max())
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Mesh Visualization')

        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")
