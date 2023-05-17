import cv2 #using cv2
from PIL import Image #Library fop processing image supporrting image
import numpy as np

#Declare the path of image files
file_hinh= r"Lena_316x316.jpg"
img= cv2.imread(file_hinh, cv2.IMREAD_COLOR)

#Reading image files by using pillow because pillow for calculating and processing instead of using opencv
imgPIL= Image.open(file_hinh)


#tạo một ảnh có cùng kích thước và model với ảnh imgPIL. Ảnh này dùng để chứa kết quả chuyển đỏi RGB sang Grayscale
average= Image.new(imgPIL.mode, imgPIL.size)

width= imgPIL.size[0]
height= imgPIL.size[1]

#nhập giá trị threshold
nguong=int(input("Nhap gia tri cua threshold: "))


#ma trận thay thế để tính cho phương pháp SOBEL theo phương X
matranx =np.array([[-1, -2, -1],[ 0, 0, 0],[1, 2, 1]])
matrany =np.array([[-1, 0, 1],[ -2, 0, 2],[-1, 0, 1]])

#tạo một ảnh có cùng kích thước và mode với hình gốc 
HinhBien=Image.new(imgPIL.mode,imgPIL.size)

#Sử dụng mặt nạ 3x3 nên ta bỏ qua các viền 
#quét từ x=1 đến x=width-1 , y=1 đến y = height-1
for x in range (1,width-1):
    for y in range(1,height-1):
        #bién giá trị cộng dồn
        MTRx = 0
        MTRy = 0
        MTGx = 0
        MTGy = 0
        MTBx = 0
        MTBy = 0
        #bien chua gia tri bien do gradian(M) và giá trị 3 kênh màu(value)
        F0=0
        value=0
        #tiến hành quét các điểm trong mặt nạ 
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                #lấy thông tin màu gray tại điểm (i,j) trong mặt nạ 
                R,G,B=imgPIL.getpixel((i,j))
                #nhân tích chập ma trận với tất cả các đểm ảnh ở mỗi kânh mức xám
                

                MTRx += R * matranx[i - x + 1, j - y + 1]
                MTRy += R * matrany[i - x + 1, j - y + 1]

                MTGx += G * matranx[i - x + 1, j - y + 1]
                MTGy += G * matrany[i - x + 1, j - y + 1]

                MTBx += B * matranx[i - x + 1, j - y + 1]
                MTBy += B * matrany[i - x + 1, j - y + 1]
        

        #kết quả công thức nhận dạng đường biên 
        Gxx = np.abs(MTRx)**2 + np.abs(MTGx)**2+ np.abs(MTBx)**2
        Gyy = np.abs(MTRy)**2 + np.abs(MTGy)**2+ np.abs(MTBy)**2
        Gxy = (MTRx * MTRy)+ (MTGx * MTGy) + (MTBx * MTBy)
        #Tính theta thay vì tính theo công thứuc chúng ta có thể dùng Atan , tuy nhiên để tránh trường hợp (Gxx-Gyy)<0
        #=>nên ta dùng atan2
        theta = 0.5 * np.arctan2((2 * Gxy), (Gxx - Gyy))
        F0 = np.sqrt(0.5 * ((Gxx + Gyy) + (Gxx - Gyy) * np.cos(2 * theta) + 2 * Gxy * np.sin(2 * theta)))
        #loc gia tri tinh sac net 
        if (F0 <= nguong):
            value = 0
        if (F0 > nguong):
            value = 255
        HinhBien.putpixel((x,y),(value,value,value))

#Exchange from PIL to OpenCV for showing by OpennCV
HinhBien_showing= np.array(HinhBien)

#Showing by using OpenCV
cv2.imshow('Anh mau goc co gai Lena',img)
cv2.imshow('Anh sau khi chinh sua Duong Bien',HinhBien_showing)


#Pres any key to close the window
cv2.waitKey()
#Release the memory which contributing to all the windows
cv2.destroyAllWindows()