import cv2 #using cv2
from PIL import Image #Library fop processing image supporrting image
import numpy as np
import math 
#Declare the path of image files
file_hinh= r"Lena_316x316.jpg"
img= cv2.imread(file_hinh, cv2.IMREAD_COLOR)

#Reading image files by using pillow because pillow for calculating and processing instead of using opencv
imgPIL= Image.open(file_hinh)

#Create the four images has the same and mode with picture imgPIL and containing all channels of HSI space colors
#This picture using containing the result RGB exchange of the HSI image

Hue=Image.new(imgPIL.mode, imgPIL.size)
Saturation=Image.new(imgPIL.mode, imgPIL.size)
Intensity=Image.new(imgPIL.mode, imgPIL.size)
HSI_image=Image.new(imgPIL.mode, imgPIL.size)


#Getting the dimensions of the image from imgPIL

width= imgPIL.size[0]
height= imgPIL.size[1]

#Using two loops for reading all the pixels in the image cause the image is the two dimensions matrix
for x in range(width):
    for y in range(height):
        #Getting the values of the each pixel in the image
        R,G,B= imgPIL.getpixel((x,y))
        #calculating the values of the Hue
        t1= 1/2*((R-G)+(R-B))
        t2=math.sqrt((R-G)*(R-G)+(R-B)*(G-B))
        if t2==0:
            print("The value of t2 is 0")
        else:
            theta=math.acos(t1/t2)
        #Conditions for putting Hue values
        H=0
        if (B<=G):
            H=theta
        if (B>G):
            H=2*math.pi-theta
        H=H*180/math.pi
        H=np.uint8(H)
        #calculating the values of the Saturation
        
        if (R+G+B==0):
            print("An total of R,G,B is 0" )
        else:
            
            S=np.uint8(255*(1-(3/(R+G+B))*min(R,G,B)))
        #Converting range values from [0;1] to [0;255] by multiply with 255
        #S = S * 255;
        #Formula for calulating in Intensity
        I = np.uint8((1/3) * (R + G + B))



        #Attaching the rules of each H-S-I
        
        Hue.putpixel((x,y),(H,H,H))
        Saturation.putpixel((x,y),(S,S,S))
        Intensity.putpixel((x,y),(I,I,I))
       
        HSI_image.putpixel((x,y),(I,S,H))

        

#Exchange from PIL to OpenCV for showing by OpennCV
Hue_showing= np.array(Hue)        
Saturation_showing= np.array(Saturation)
Intensity_showing= np.array(Intensity)
HSI_image_showing= np.array(HSI_image)

#Showing by using OpenCV
cv2.imshow('Anh mau goc co gai nuoc Nhat',img)
cv2.imshow('Anh mau Hue',Hue_showing)
cv2.imshow('Anh mau Intensity',Intensity_showing)
cv2.imshow('Anh mau Saturation',Saturation_showing)
cv2.imshow('Anh mau ket hop H-S-I',HSI_image_showing)

#Pres any key to close the window
cv2.waitKey()
#Release the memory which contributing to all the windows
cv2.destroyAllWindows()