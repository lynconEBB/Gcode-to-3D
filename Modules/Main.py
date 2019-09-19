from Modules.Simulation import *
from Modules.Treatment import *
from Modules.Image_processing import *
from Modules.Remesh import *
import os


class Main:
    def __init__(self,gcode_file,obj_file,ply_file,image_dir,save_img=False,skirt_height=0):
        self.gcode_file = gcode_file
        self.obj_file = obj_file
        self.ply_file= ply_file
        self.save_img = save_img
        self.skirt_height = skirt_height
        path = os.path.split(self.gcode_file)
        self.image_name = path[1].split(".")
        self.image_name = self.image_name[0]
        self.image_path = image_dir
        self.image_file = self.image_path+"/"+self.image_name+"0.png"

    def convert(self):
        all_coordinates=[]
        parse = Treatment.parse_gcode(self.gcode_file)
        self.layers = Treatment.select_layer(parse)
        i=0
        Treatment.clean_directory(self.image_path)
        for self.layer in self.layers:
            z = Simulation.generate_layer_preview(self.layer,self.image_file)
            coordinates =Image.get_coords(z,self.image_file,self.skirt_height,i)
            all_coordinates.append(coordinates)
            i += 1
            if self.save_img:
                self.image_file = self.image_path + "/" + self.image_name + str(i)+ ".png"

        Treatment.create_point_cloud_file(all_coordinates,self.ply_file)
        Remesh.create_obj(self.ply_file,self.obj_file)

    @staticmethod
    def export(obj_file,output_file):
        Remesh.export(obj_file, output_file)


if __name__ == "__main__":
    main = Main("../Gcodes/super.gcode","/home/lyncon/3d-printer-parser/Files/test_out.obj","/home/lyncon/3d-printer-parser/Files/point_cloud.ply","../Images",True,skirt_height=8)
    main.convert()
