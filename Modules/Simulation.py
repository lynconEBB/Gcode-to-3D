import matplotlib.pyplot as plt

# Class to Simulate print process
class Simulation:
    @staticmethod
    def generate_layer_preview(layer, dest):
        ly=[[]]
        lx=[[]]
        fig = plt.figure(figsize=(7, 7))            # create a matplotlib figure 7x7 inches
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlim([0, 200])                       # set x axis max value to 200 and min value to 0
        ax.set_ylim([0, 200])                       # set y axis max value to 200 and min value to 0
        i=0
        lastz = 0
        for line in layer:
            if line[2] != "":
                lastz = float(line[2])
            elif line[3] != "" :                # add coordinates x and y to list if line has X, Y and E parameters
                lx[i].append(float(line[0]))
                ly[i].append(float(line[1]))
            else:
                ax.plot(lx[i], ly[i], 'black')
                lx.append([])
                ly.append([])
                i+=1
                lx[i].append(float(line[0]))
                ly[i].append(float(line[1]))
                ax.plot(lx[i], ly[i], linestyle="none")

        ax.plot(lx[i], ly[i], 'black')
        ax.set_axis_off()
        fig.savefig(dest)
        plt.close(fig)
        return lastz


if __name__ == '__main__':

    Simulation.extrude_preview()

