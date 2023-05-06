import cv2  #thư viện xử lý ảnh openCV cho python
import numpy as np #thư viện toán học, đặc biệt là các tính toán ma trận

#đọc ảnh màu sử dụng thư viện openCV
img  = cv2.imread('gai-dep.jpg',cv2.IMREAD_COLOR)

#lấy kích thước của ảnh
height=len(img[0])
width=len(img[1])

#khai báo 3 biến để chứa hình 3 kênh màu R, G, B
red=np.zeros((width,height,3), np.uint8)  #chỉ tạo 2 ma trận width và height nhưng có 3 kênh màu red, green, blue. mỗi kênh 8 bit
green =np.zeros((width,height,3), np.uint8)
blue=np.zeros((width,height,3), np.uint8)

#ban đầu set zero cho tất cả các điểm ảnh có trong cả 3 kênh trong mỗi hình
red[:]=[0,0,0]  #: set lại các giá trị ở trên lại thành 0
green[:]=[0,0,0]
blue[:]=[0,0,0]

#mỗi hình là một ma trận 2 chiều nên phải dùng 2 vòng lặp for để đọc hết các điểm ảnh có trong hình
for x in range(width):
    for y in range(height):

        #lấy giá trị điểm ảnh tại vị trí (x, y)
        R= img[x,y,2]   #red chứa ở kênh số 2
        G= img[x,y,1]   #green chứa ở kênh số 1
        B= img[x,y,0]   #blue chứa ở kênh số 0

        #thiết lập màu cho các kênh
        red[x,y,2]=R
        green[x,y,1]=G
        blue[x,y,0]=B

#hiển thị hình dùng thư viện openCV
cv2.imshow('Hinh goc RGB',img)
cv2.imshow('Hinh chuyen qua mau red ',red)
cv2.imshow('Hinh chuyen qua mau green ',green)
cv2.imshow('Hinh chuyen qua mau blue ',blue)


#bấm phím bất kỳ để đóng cửa sổ hiển thị hình
cv2.waitKey()

#giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị hình
cv2.destroyAllWindows()
