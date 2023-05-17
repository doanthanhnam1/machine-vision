import cv2 # nhúng thư viện của openCV vào để sử dụng 
from PIL import Image #thư viện xử lí ảnh PILLOW hỗ trợ nhiều định dạng ảnh khác nhau 
import numpy as np # thư viện toán học của python dùng để tín toán các giá trị 

#khai báo đường dẫn file hình 
filehinh = r"ANH LENA.jpg"

#đọc ảnh màu dùng thư viện openCV 
img = cv2.imread(filehinh,cv2.IMREAD_COLOR)
#đọc ảnh màu dùng thư viện PILLOW.Ảnh PIL này sẽ được dùng để thực hiện các tác vụ xử lý và tính toán thay vì dùng openCv 
imgPIL = Image.open(filehinh)

#tạo một ảnh có cùng kích thước và mode với ảnh imgPIL
#ảnh này dùng để chứa kết quả chuyển đổi từ ảnh màu RGB sang Binary
binary = Image.new(imgPIL.mode , imgPIL.size)

#lấy kích thước của ảnh từ imgPIL
width = binary.size[0]
height = binary.size[1]

#thiết lập một giá trị ngưỡng để tín điểm ảnh nhị phân binary
Nguong = 130
#mỗi ảnh là một ma trận 2 chiều nên dùng 2 vòng lặp for
for x in range(width):
  for y in range(height):
    #lấy các điểm ảnh tại vị trí (x,y)
    R , G, B = imgPIL.getpixel((x,y))
    #công thức chuyển đổi điểm màu RGB sang điểm màu mức xám (grayscale) Luminace 
    gray = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)
    #xác định giá trị ảnh nhị phân(binary)
    if (gray < Nguong) :
     binary.putpixel((x,y),(0,0,0))
    else :
      binary.putpixel((x,y),(255,255,255))


#để hiện thị ảnh từ PIL sang openCV để hiển thị thì ta cần phải chuyển đổi
anhnhiphan = np.array(binary)



#--------------------------------------------------------------------------------------------------------------------------
#hiển thị ảnh dùng thư viện openCV 
cv2.imshow('Anh mau RGB goc ',img)
cv2.imshow('Anh nhi phan(binary)',anhnhiphan)

#bấm phím bất kỳ để đóng cửa sổ hiển thị 
cv2.waitKey(0)
#giải phóng bộ nhớ đã cấp phát cho các thiết bị
cv2.destroyAllWindows