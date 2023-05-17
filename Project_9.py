import cv2 #using cv2
from PIL import Image #Library fop processing image supporrting image
import numpy as np
import math
#Declare the path of image files
file_hinh= r"Lena_316x316.jpg"
img= cv2.imread(file_hinh, cv2.IMREAD_COLOR)

#Reading image files by using pillow because pillow for calculating and processing instead of using opencv
imgPIL= Image.open(file_hinh)

#Create the four images has the same and mode with picture imgPIL and containing all channels of XYZ space colors
#This picture using containing the result RGB exchange of the XYZ image

Channel_X=Image.new(imgPIL.mode, imgPIL.size)
Channel_Y=Image.new(imgPIL.mode, imgPIL.size)
Channel_Z=Image.new(imgPIL.mode, imgPIL.size)
XYZ_image=Image.new(imgPIL.mode, imgPIL.size)


#Getting the dimensions of the image from imgPIL

width= imgPIL.size[0]
height= imgPIL.size[1]

#Using two loops for reading all the pixels in the image cause the image is the two dimensions matrix
for a in range(width):
    for b in range(height):
        #Getting the values of the each pixel in the image
        R,G,B= imgPIL.getpixel((a,b))
        #calculating the Channel_Zs of the Channel_X
        X = np.uint8(0.4124564 * R + 0.3575761 * G + 0.1804375 * B)
        Y = np.uint8(0.2126729 * R + 0.7151522 * G + 0.07217508 * B)
        Z = np.uint8(0.0193339 * R + 0.1191920 * G + 0.9503041 * B)

        #Attaching the rules of each H-S-I
        
        Channel_X.putpixel((a,b),(X,X,X))
        Channel_Y.putpixel((a,b),(Y,Y,Y))
        Channel_Z.putpixel((a,b),(Z,Z,Z))
       
        XYZ_image.putpixel((a,b),(Z,Y,X))

        

#Exchange from PIL to OpenCV for showing by OpennCV
Channel_X_showing= np.array(Channel_X)        
Channel_Y_showing= np.array(Channel_Y)
Channel_Z_showing= np.array(Channel_Z)
XYZ_image_showing= np.array(XYZ_image)

#Showing by using OpenCV
cv2.imshow('Anh mau goc co gai lena',img)
cv2.imshow('Anh mau Channel_X',Channel_X_showing)
cv2.imshow('Anh mau Channel_Z',Channel_Z_showing)
cv2.imshow('Anh mau Channel_Y',Channel_Y_showing)
cv2.imshow('Anh mau ket hop XYZ',XYZ_image_showing)

#Pres any key to close the window
cv2.waitKey()
#Release the memory which contributing to all the windows
cv2.destroyAllWindows()