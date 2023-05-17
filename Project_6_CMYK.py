import cv2 #using cv2
from PIL import Image #thư viện xử lý ảnh PILLOW
import numpy as np


#khai báo đường dẫn file hình
file_hinh= r"Lena_316x316.jpg"
#đọc file hình ảnh sử dụng openCV
img= cv2.imread(file_hinh, cv2.IMREAD_COLOR)

#đọc ảnh dùng thư viện PIL
imgPIL= Image.open(file_hinh)

#tạo 4 khung hình có cùng mô hình và kích thước với imgPIL và chứa các kênh của không gian màu CMYK
#Ảnh này chứa kết quả chuyển đổi RGB của ảnh CMKY

Cyan=Image.new(imgPIL.mode, imgPIL.size)
Magenta=Image.new(imgPIL.mode, imgPIL.size)
Yellow=Image.new(imgPIL.mode, imgPIL.size)
Black=Image.new(imgPIL.mode, imgPIL.size)


##lấy kích thước của hình ảnh

width= imgPIL.size[0]
height= imgPIL.size[1]

#dùng 2 vòng for để quét các điểm ảnh có trong hìnho
for x in range(width):
    for y in range(height):
        #lấy giá trị của mỗi điểm ảnh
        R,G,B= imgPIL.getpixel((x,y))
       
        #Đính kèm các quy tắc của từng CMYK
        Cyan.putpixel((x,y),(B,G,0))
        Magenta.putpixel((x,y),(B,0,R))
        Yellow.putpixel((x,y),(0,G,R))
        Black_color= min(B,G,R)
        Black.putpixel((x,y),(Black_color,Black_color,Black_color))

        

#chuyển từ PIL sang OpenCV để hiển thị bằng OpenCV
Cyan_showing= np.array(Cyan)        
Magenta_showing= np.array(Magenta)
Yellow_showing= np.array(Yellow)
Black_showing= np.array(Black)

##thể hiện hình ảnh sử dụng OpenCV
cv2.imshow('Anh mau goc co gai lena',img)
cv2.imshow('Anh mau Cyan',Yellow_showing)
cv2.imshow('Anh mau Magneta',Magenta_showing)
cv2.imshow('Anh mau Yellow',Cyan_showing)
cv2.imshow('Anh mau Black',Black_showing)
#nhấn phím bất kì để đóng của sổ hiển thị
cv2.waitKey()
#giải phóng bộ nhớ đã cấp phát cho các cửa sổ
cv2.destroyAllWindows()