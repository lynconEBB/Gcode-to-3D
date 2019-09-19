import os
import shutil

# Class to parse the gcode file
class Treatment:
    @staticmethod
    def parse_gcode(file):
        coords = []

        for line in open(file,"r"):                         # Open File to read
            if line.startswith(";"):                        # Ignore if Line is a comment
                continue
            if line == "":                                  # Ignore if line is empty
                continue
            if not line.startswith("G"):                    # Ignore if line starts with other letter than 'G'
                continue
            else:                                           # Do this if Line starts with G - Lines in Gcode that starts with G are Print commands or travel commands
                values = line.split()
                x, y, z, e = "", "", "", ""
                for i in range(1,len(values)):
                    if values[i].startswith("X"):
                        x = values[i]
                        x = x[1:]
                    elif values[i].startswith("Y"):
                        y = values[i]
                        y = y[1:]
                    elif values[i].startswith("Z"):
                        z = values[i]
                        z = z[1:]
                    if values[i].startswith("E"):
                        e = values[i]
                        e = e[1:]

                if (x != "" and y != "") or (z != ""):
                    coords.append([x,y,z,e])
        return coords

    @staticmethod
    def select_layer(vector):    # method to find layer and separate into lists
        layers=[]
        i=-1
        for ii in range(1,len(vector)):
            if vector[ii][2] != "":
                layers.append([])
                i += 1
                layers[i].append(vector[ii])

            else:
                layers[i].append(vector[ii])

        return layers

    @staticmethod
    def create_point_cloud_file(coords,ply_file): #Method to create point cloud with all coordinates of contours
        coords_final=[]
        lx=[]
        ly=[]
        lz=[]
        for ii in range(0,len(coords)):
            for i in range(0,len(coords[ii])):
                coords_final.append(coords[ii][i])

        for coord in coords_final:
            lx.append(coord[0])
            ly.append(coord[1])
            lz.append(coord[2])

        max_x = max(lx)
        min_x = min(lx)
        max_y = max(ly)
        min_y = min(ly)
        max_z = max(lz)
        min_z = min(lz)

        cx = (min_x + max_x) / 2
        cy = (min_y + max_y) / 2
        cz = (min_z + max_z) / 2

        vertex_num=str(len(coords_final))
        gcode = open(ply_file,"w")
        gcode.write("ply\n")
        gcode.write("format ascii 1.0\n")
        gcode.write("element vertex "+vertex_num+" \n")
        gcode.write("property float32 x\n")
        gcode.write("property float32 y\n")
        gcode.write("property float32 z\n")
        gcode.write("end_header\n")
        
        for i in range(0,len(coords_final)):
            x = str(coords_final[i][0]-cx)
            y = str(coords_final[i][1]-cy)
            z = str(coords_final[i][2]-cz)
            gcode.write(x+" "+y+" "+z+"\n")
        gcode.close()

    @staticmethod
    def gcode_preview(file):
        new = [[]]
        final = [[]]
        lx, lz, ly = [], [], []
        edges = [[]]
        layer_count = 0

        parse = Treatment.parse_gcode(file)
        layers = Treatment.select_layer(parse)
        i = 0
        for layer in layers:
            lastz = 0
            for line in layer:
                if line[2] != "":
                    lastz = float(line[2])
                    layer_count+=1
                elif line[3] != "":
                    new[i].append([float(line[0]), lastz, float(line[1])])
                else:
                    new.append([])
                    i += 1

        new.pop(0)
        for layer in new:
            for coord in layer:
                lx.append(coord[0])
                ly.append(coord[1])
                lz.append(coord[2])

        max_x = max(lx)
        min_x = min(lx)
        max_y = max(ly)
        min_y = min(ly)
        max_z = max(lz)
        min_z = min(lz)

        cx = float((min_x + max_x) / 2)
        cy = float((min_y + max_y) / 2)
        cz = float((min_z + max_z) / 2)

        i = 0
        for layer in new:
            if len(layer) % 2 == 1:
                layer.pop()
            for coord in layer:
                final[i].append([coord[0] - cx, coord[1] - cy, coord[2] - cz])

            for ii in range(len(final[i]) - 1):
                edges[i].append((ii, ii + 1))

            edges.append([])
            final.append([])
            i += 1

        final.pop()
        edges.pop()
        return final, edges, layer_count

    @staticmethod
    def clean_directory(dir):
        for the_file in os.listdir(dir):
            file_path = os.path.join(dir, the_file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)


if __name__ == "__main__":
    Treatment.clean_directory("../Images")