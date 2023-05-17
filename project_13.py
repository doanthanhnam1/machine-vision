import cv2 #using cv2
from PIL import Image #Library fop processing image supporrting image
import numpy as np
import math
#Declare the path of image files
file_hinh= r"Lena_316x316.jpg"
img= cv2.imread(file_hinh, cv2.IMREAD_COLOR)

#Reading image files by using pillow because pillow for calculating and processing instead of using opencv
imgPIL= Image.open(file_hinh)

#Create the four images has the same and mode with picture imgPIL and containing all channels of CMKY space colors
#This picture using containing the result RGB exchange of the CMKY image


width= imgPIL.size[0]
height= imgPIL.size[1]


#nhập các giá trị (x1,y1) và (x2,y2) để chọn vùng ảnh 
x1=int(input("Nhap gia tri cua x1: "))
x2=int(input("Nhap gia tri cua x2: "))
y1=int(input("Nhap gia tri cua y1: "))
y2=int(input("Nhap gia tri cua y2: "))
#nhập giá trị của ngưỡng để so sánh 
Threshold=int(input("Nhap gia tri cua threshold: "))
#các biến chứa giá trị cộng dồn của vecto trung bình a 
aRtb=0
aGtb=0
aBtb=0
#lấy giá trị các kênh màu trong vùng ảnh đã chọn  

for i in range(x1,x2+1):
    for j in range(y1,y2+1):

#Using two loops for reading all the pixels in the image cause the image is the two dimensions matrix in area (x1,y1),(x2,y2)

        #Getting the values of the each pixel in the image
        R,G,B= imgPIL.getpixel((i,j))
        aRtb+=R
        aGtb+=G
        aBtb+=B
#tính giá trị vecto trung bình a(aRtb,aGtb,aBtb)=số các điểm ảnh của từng kênh/kích thước vùng ảnh(size)
size=abs(x2-x1)*abs(y2-y1)

aRtb=aRtb/size
aGtb=aGtb/size
aBtb=aBtb/size

#tạo một ảnh có cùng kích thước và mode với hình gốc 
segmimg=Image.new(imgPIL.mode,imgPIL.size)

#Lấy giá trị từng kênh màu ứng với bị trí (x,y) trên hình gốc 
for x in range(width):
    for y in range(height):
        zR,zG,zB= imgPIL.getpixel((x,y))
        
        #Áp dụng công thức 6.7-1 để tính kích thước Euclidean Distance giữa 2 vecto a và z 
        D = math.sqrt(math.pow(zR - aRtb, 2) + math.pow(zG - aGtb, 2) + math.pow(zB - aBtb, 2))
        if D<=Threshold: #điểm z(x,y) thuộc nền(background)
            segmimg.putpixel((x,y),(255,255,255))#set white color
        else:
            segmimg.putpixel((x,y),(zB,zG,zR))






#Exchange from PIL to OpenCV for showing by OpennCV
segimg_showing= np.array(segmimg)        


#Showing by using OpenCV
cv2.imshow('Anh mau goc co gai Lena',img)
cv2.imshow('Anh sau khi chinh sua segmimg',segimg_showing)


#Pres any key to close the window
cv2.waitKey()
#Release the memory which contributing to all the windows
cv2.destroyAllWindows()