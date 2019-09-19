from meshlabxml import *
import os

class Remesh:
    @staticmethod
    def create_obj(input_file,output_file):
        meshlabserver_path = 'C:\Program Files\VCG\MeshLab'
        os.environ['PATH'] = meshlabserver_path + os.pathsep + os.environ['PATH']                   # Add meshlabserver to your path

        mesh = mlx.FilterScript(file_in=input_file,file_out=output_file,ml_version="2016.12")       # initializes MeshLab Script setting input and output files
        transform.scale2(mesh,value=[0.38,0.38,1],uniform=False,center_pt="barycenter")             # Alter Scale on axis X and Y
        normals.estimate_radius(mesh,16)                                                            # Estimate Radius using point cloud density
        select.vert_function(mesh,function="rad<0.3")                                               # Select No-Bounding vertices
        delete.selected(mesh,face=False)                                                            # Delete selected Vertices
        normals.point_sets(mesh,neighbors=100)                                                      # Compute normals to get surfaces direction
        remesh.surface_poisson_screened(mesh,depth=8)                                               # Screened Poisson Remeshing
        layers.delete(mesh,layer_num=0)                                                             # Delete Point Cloud Layer
        smooth.laplacian(mesh,iterations=6)                                                         # Smooth mesh surface
        mesh.run_script()                                                                       # Run on MeshLab Server
        Remesh.decrease_faces(output_file)                                                         # Decrease faces for better performance

    @staticmethod
    def export(input_file,output_file):
        meshlabserver_path = 'C:\Program Files\VCG\MeshLab'
        os.environ['PATH'] = meshlabserver_path + os.pathsep + os.environ['PATH']                   # Add meshlabserver to your path
        stl = mlx.FilterScript(file_in=input_file, file_out=output_file, ml_version="2016.12")      # Generate script that convert OBJ file into STL file
        stl.run_script()                                                                            # Run script on MeshLab Server

    @staticmethod
    def decrease_faces(file):
        mesh = mlx.FilterScript(file_in=file, file_out=file, ml_version="2016.12")
        topology = files.measure_topology(file,ml_version="2016.12")
        faces = int(topology["face_num"]/200)
        remesh.simplify(mesh, texture=False, faces=faces, preserve_topology=False)
        mesh.run_script()

    @staticmethod
    def measure_diff(file_in1,file_in2,file_out):
        meshlabserver_path = 'C:\Program Files\VCG\MeshLab'
        os.environ['PATH'] = meshlabserver_path + os.pathsep + os.environ['PATH']                   # Add meshlabserver to your path
        texture_file = os.path.basename(file_out)
        texture_file = texture_file.split(".")
        texture_file = texture_file[0]+".png"
        diff = mlx.FilterScript(file_in=[file_in1,file_in2],file_out=file_out,ml_version="2016.12")
        sampling.dist_ref(diff)
        vert_color.colorize(diff)
        texture.per_triangle(diff)
        layers.delet_0(diff)
        transfer.vc2tex(diff,texture_file)
        diff.run_script()

if __name__ == "__main__":
    mesh = Remesh()
    #mesh.decrease_faces("C:\\Users\\Lyncon\\3d-printer-parser\\Files\\test_out.obj")
    mesh.create_obj("/home/lyncon/3d-printer-parser/Files/point_cloud.ply","/home/lyncon/3d-printer-parser/Files/test_out.obj")
    #mesh.measure_diff("C:\\Users\\Lyncon\\Desktop\\files\\eevee_lowpoly_flowalistik.stl","C:\\Users\\Lyncon\\3d-printer-parser\\Files\\test_out.obj","C:\\Users\\Lyncon\\3d-printer-parser\\Files\\test_out6.obj")
    #mesh.export("/home/lyncon/3d-printer-parser/Files/test_out.obj","/home/lyncon/3d-printer-parser/Files/test.stl")