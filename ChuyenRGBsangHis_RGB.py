import cv2 #using cv2
from PIL import Image #thư viện xử lý ảnh PILLOW
import numpy as np
import matplotlib.pyplot as plt


def Cal_Histogram(imgPIL):
    #mỗi pixel có các giá trị từ 0 đến 255, vì vậy phải khai báo mảng có 256 phần tử chứa vô số pixel có cùng giá trị
    his1= np.zeros(256)
    his2=np.zeros(256)
    his3=np.zeros(256)
    #kích thước của hình ảnh
    w= imgPIL.size[0]
    h=imgPIL.size[1]
    
    for x in range(w):
        for y in range(h):
            #lấy giá trị màu tại diểm (x,y)
            gR,gG,gB= imgPIL.getpixel((x,y))

            his1[gR]+=1 #histogram của kênh màu Red
            his2[gG]+=1 #histogram của kênh màu Green
            his3[gB]+=1 #histogram của kênh màu Blue

    return his1,his2,his3
#vẽ biểu đồ histogram dùng thư viện matplotlib
def DrawingGraphHistogram(his1,his2,his3):
    w=8
    h=4
    plt.figure('biểu đồ graph bảng màu RGB',figsize=((w,h)), dpi=100)
    X_axis= np.zeros(256)# mảng trục x
    X_axis= np.linspace(0,256,256)
    
    plt.plot(X_axis, his1, color='red')
    plt.plot(X_axis, his2, color='green')
    plt.plot(X_axis, his3, color='blue')
    
    plt.title('Biểu đồ Graph')
    plt.xlabel('Gía trị màu RGB')
    plt.ylabel('số điểm ảnh có cùng giá trị màu ')
    Y_axis= np.zeros(256)
    plt.show()
#--------------------------------------------------------

#khai báo đường dẫn file hình
file_hinh= r"bird_small.jpg"
#đọc file hình ảnh sử dụng openCV
img= cv2.imread(file_hinh, cv2.IMREAD_COLOR)

#đọc ảnh dùng thư viện PIL
imgPIL= Image.open(file_hinh)



#tính toán Hisogram
his1,his2,his3= Cal_Histogram(imgPIL)

#thể hiện hình ảnh gốc
cv2.imshow("The original picture",img)


#hiển thị biểu đồ histogram
DrawingGraphHistogram(his1,his2,his3)
             

#nhấn phím bất kì để đóng của sổ hiển thị
cv2.waitKey()
#giải phóng bộ nhớ đã cấp phát cho các cửa sổ
cv2.destroyAllWindows()