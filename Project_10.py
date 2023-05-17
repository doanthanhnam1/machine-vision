import cv2 #using cv2
from PIL import Image #Library fop processing image supporrting image
import numpy as np
import math
#Declare the path of image files
file_hinh= r"Lena_316x316.jpg"
img= cv2.imread(file_hinh, cv2.IMREAD_COLOR)

#Reading image files by using pillow because pillow for calculating and processing instead of using opencv
imgPIL= Image.open(file_hinh)

#Create the four images has the same and mode with picture imgPIL and containing all channels of YcbCr space colors
#This picture using containing the result RGB exchange of the CMKY image

Channel_Y=Image.new(imgPIL.mode, imgPIL.size)
Channel_Cb=Image.new(imgPIL.mode, imgPIL.size)
Channel_Cr=Image.new(imgPIL.mode, imgPIL.size)
YCbCr_img=Image.new(imgPIL.mode, imgPIL.size)


#Getting the dimensions of the image from imgPIL

width= imgPIL.size[0]
height= imgPIL.size[1]

#Using two loops for reading all the pixels in the image cause the image is the two dimensions matrix
for x in range(width):
    for y in range(height):
        #Getting the values of the each pixel in the image
        R,G,B= imgPIL.getpixel((x,y))
        #calculating the Channel_Crs of the Channel_Y
        Y = np.uint8(16 + (65.738 / 256) * R + (129.057 / 256) * G + (25.064 / 256) * B)
        Cb = np.uint8(128 - (37.945 / 156) * R - (74.494 / 256) * G + (112.439 / 256) * B)
        Cr = np.uint8(128 + (112.439 / 256) * R - (94.154 / 256) * G - (18.285 / 256) * B)
    

        #Attaching the rules of each H-S-I
        
        Channel_Y.putpixel((x,y),(Y,Y,Y))
        Channel_Cb.putpixel((x,y),(Cb,Cb,Cb))
        Channel_Cr.putpixel((x,y),(Cr,Cr,Cr))
       
        YCbCr_img.putpixel((x,y),(Cr,Cb,Y))

        

#Exchange from PIL to OpenCV for showing by OpennCV
Channel_Y_showing= np.array(Channel_Y)        
Channel_Cb_showing= np.array(Channel_Cb)
Channel_Cr_showing= np.array(Channel_Cr)
YCbCr_img_showing= np.array(YCbCr_img)

#Showing by using OpenCV
cv2.imshow('Anh mau goc co gai lena',img)
cv2.imshow('Anh mau Channel_Y',Channel_Y_showing)
cv2.imshow('Anh mau Channel_Cr',Channel_Cr_showing)
cv2.imshow('Anh mau Channel_Cb',Channel_Cb_showing)
cv2.imshow('Anh mau ket hop YCbCr',YCbCr_img_showing)

#Pres any key to close the window
cv2.waitKey()
#Release the memory which contributing to all the windows
cv2.destroyAllWindows()