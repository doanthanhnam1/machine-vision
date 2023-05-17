import cv2 #sử dụng cv2
from PIL import Image #thư viện xử lý ảnh PILLOW
import numpy as np
import matplotlib.pyplot as plt #thư viện vẽ biểu đồ


#sử dụng def để xử lý mức xám (Luminance)
def ChuyendoiRGBsangLuminance(imgPIL):
    Luminance= Image.new(imgPIL.mode, imgPIL.size)

    #lấy kích thước của ảnh từ imgPIL

    width= imgPIL.size[0]
    height= imgPIL.size[1]

    #sử dụng 2 vòng lặp for để đọc hết các pixel 
    for x in range(width):
        for y in range(height):
            #lấy giá trị của mỗi piexel có trong ảnh
            R,G,B= imgPIL.getpixel((x,y))
            #công thức tính màu xám cho Luminance
            gray=np.uint8(0.2126*R + 0.7152*G+ 0.0722*B)
            #đính kèm giá trị màu xám cho pixel
            Luminance.putpixel((x,y),(gray,gray,gray))
    return Luminance

   #đổi từ PIL sang OpenCV để hiển thị bằng OpenCV

def Cal_Histogram(HinhxamPIL):
    #mỗi pixel có giá trị từ 0-255, nên phải khai báo một mảng có 256 phần tử để chứa số đếm của các pixels có cùng giá trị
    his= np.zeros(256)

    #kích thước ảnh
    w= HinhxamPIL.size[0]
    h=HinhxamPIL.size[1]

    
    for x in range(w):
        for y in range(h):
            #lấy giá trị mức xám tại điểm (x,y)
            gR, gG, gB = HinhxamPIL.getpixel((x,y))

            #giá trị gray tính ra cũng chính là phần tử thứ gray trong mảng his đã khai báo ở trên.
            #sẽ tăng số đếm của phần tử gray lên 1
            his[gR]+=1

    return his 

#--------------------------------------------------------
# Begin: DrawingGraphHistogram(his)
#--------------------------------------------------------
# vẽ biểu đồ histogram dùng thư viện matplotlib
def DrawingGraphHistogram(his):
    w=8
    h=4
    plt.figure('biểu đồ histogram ảnh xám',figsize=((w,h)), dpi=100)
    X_axis= np.zeros(256)# mảng của trục x chứa 256 phần tử
    X_axis= np.linspace(0,256,256)  
    plt.plot(X_axis, his, color='orange')
    plt.title('biểu đồ histogram')
    plt.xlabel('giá trị mức xám')
    plt.ylabel('số điểm có cùng giá trị mức xám')
    Y_axis= np.zeros(256)
    plt.show()
#--------------------------------------------------------
# End: DrawingGraphHistogram(his)
#--------------------------------------------------------

#--------------------------------------------------------
# --------------BEGIN: CHƯƠNG TRÌNH CHÍNH----------------
#lưu ý: các hàm con phải khai báo trước khi chương trình chính gọi
#--------------------------------------------------------

#khai báo đường dẫn file hình
file_hinh= r"bird_small.jpg"
#đọc file hình ảnh sử dụng openCV
img= cv2.imread(file_hinh, cv2.IMREAD_COLOR)

#đọc ảnh dùng thư viện PIL
imgPIL= Image.open(file_hinh)

#chuyển sang ảnh mức xám
HinhxamPIL= ChuyendoiRGBsangLuminance(imgPIL)

#tính toán Hisogram
his= Cal_Histogram(HinhxamPIL)

#chuyển ảnh PIL sang OpenCV để hiển thị bằng thư viện cv2
HinhxamCV= np.array(HinhxamPIL)
cv2.imshow("The grayscale image",HinhxamCV)

#thể hiện hình ảnh gốc
cv2.imshow("The original picture",img)


#hiển thị biểu đồ histogram
DrawingGraphHistogram(his)
             

#nhấn phím bất kì để đóng của sổ hiển thị
cv2.waitKey()
#giải phóng bộ nhớ đã cấp phát cho các cửa sổ
cv2.destroyAllWindows()