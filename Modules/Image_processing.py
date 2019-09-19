import numpy as np
import cv2 


class Image:
    @staticmethod
    def get_coords(z,imagefile,skirt_h,cont):
        im = cv2.imread(imagefile)                                      # Open Image using OpenCV
        imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)                    # Convert image to Grayscale
        ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)    # Threshold image to white
        thresh=(255-thresh)                                             # Transform white pixels in black and black pixels in white
        if cont < skirt_h:
            im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(thresh, contours, 0, (0, 0, 0), 3)
            print(z)
        xy = np.where(thresh == [255])                                  # Get  white pixels coordinates
        coordinates = list(zip(xy[0], xy[1]))

        for i in range(0, len(coordinates)):                            # Add Z parameter to every coordinate
            coordinates[i] = list(coordinates[i])
            coordinates[i].append(z)

        return  coordinates


if __name__ == "__main__":
    im = Image()
    coordinatestorno = im.get_coords(0.35,"../Images/eve6.png",5)
    print(coordinatestorno)