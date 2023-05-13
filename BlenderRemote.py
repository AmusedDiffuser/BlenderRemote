
import os
import urllib.request
import zipfile
import bpy
import random

# Download Blender for Linux
url = "https://download.blender.org/release/Blender2.93/blender-2.93.6-linux-x64.tar.xz"
filename = "blender.tar.xz"
urllib.request.urlretrieve(url, filename)

# Extract Blender
os.system(f"tar -xf {filename}")

# Set the path to Blender
blender_path = os.path.join(os.getcwd(), "blender-2.93.6-linux-x64", "blender")

# Run Blender with the script
os.system(f"{blender_path} --background --python blender_script.py")

# Create a plane
bpy.ops.mesh.primitive_plane_add(size=10)

# Create six spheres at random positions on the plane
for i in range(6):
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    z = random.uniform(0, 2)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(x, y, z))

# Create a camera and set its position and rotation
bpy.ops.object.camera_add(location=(0, -10, 2), rotation=(1.0472, 0, 0))

# Create a path for the camera to follow
bpy.ops.curve.primitive_bezier_circle_add(radius=10)
bpy.context.object.name = "Path"
bpy.context.object.data.path_duration = 90

# Set the camera to follow the path
bpy.context.scene.camera = bpy.data.objects["Camera"]
bpy.context.scene.camera.constraints.new(type='FOLLOW_PATH')
bpy.context.scene.camera.constraints['Follow Path'].target = bpy.data.objects["Path"]
bpy.context.scene.camera.constraints['Follow Path'].use_fixed_location = True

# Set the render engine to Eevee
bpy.context.scene.render.engine = 'BLENDER_EEVEE'

# Set the output file format and name
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.filepath = 'SphereTest.mp4'

# Set the render resolution as 720p
bpy.context.scene.render.resolution_x = 1280
bpy.context.scene.render.resolution_y = 720

# Render the animation
bpy.ops.render.render(animation=True)
