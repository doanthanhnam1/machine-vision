import cv2 #using cv2
from PIL import Image #Library fop processing image supporrting image
import numpy as np
import math
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

#mỗi ảnh là ma trận 2 chiều nên dùng 2 vòng lặp for để đọc hết các điểm ảnh có trong ảnh
for x in range(width):
    for y in range(height):
        #lấy giá trị điểm ảnh tại vị trí (x,y)
        R,G,B= imgPIL.getpixel((x,y))
        #chuyển đổi ảnh RGB thành ảnh mức xám dùng phương pháp average
        gray=np.uint8((R+G+B)/3) #ép kiểu bit
        #gán giá trị mức xám vừa tính cho ảnh xám 
        average.putpixel((x,y),(gray,gray,gray))

#ma trận thay thế để tính cho phương pháp SOBEL theo phương X
matranx =np.array([[-1, -2, -1],[ 0, 0, 0],[1, 2, 1]])
matrany =np.array([[-1, 0, 1],[ -2, 0, 2],[-1, 0, 1]])

#tạo một ảnh có cùng kích thước và mode với hình gốc 
DuongBien=Image.new(imgPIL.mode,imgPIL.size)

#Sử dụng mặt nạ 3x3 nên ta bỏ qua các viền 
#quét từ x=1 đến x=width-1 , y=1 đến y = height-1
for x in range (1,width-1):
    for y in range(1,height-1):
        #bién giá trị cộng dồn
        MTx=0
        MTy=0
        #bien chua gia tri bien do gradian(M) và giá trị 3 kênh màu(value)
        M=0
        value=0
        #tiến hành quét các điểm trong mặt nạ 
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                #lấy thông tin màu gray tại điểm (i,j) trong mặt nạ 
                R,G,B=average.getpixel((i,j))
                #nhân tích chập ma trận với tất cả các đểm ảnh ở mỗi kânh mức xám
                MTx += R *matranx[i-x+1,j-y+1]
                MTy += R *matrany[i-x+1,j-y+1]
        #kết thúc quét và cộng dồn điểm ảnh trong mặt nạ thì tính theo công thức 10.2-20
        M = abs(MTx) + abs(MTy) 
        #loc gia tri ve duong bien
        if (M <= nguong):
            value = 0
        if (M > nguong):
            value = 255
        DuongBien.putpixel((x,y),(value,value,value))

#Exchange from PIL to OpenCV for showing by OpennCV
DuongBien_showing= np.array(DuongBien)

#Showing by using OpenCV
cv2.imshow('Anh mau goc co gai Lena',img)
cv2.imshow('Anh sau khi chinh sua Duong Bien',DuongBien_showing)


#Pres any key to close the window
cv2.waitKey()
#Release the memory which contributing to all the windows
cv2.destroyAllWindows()