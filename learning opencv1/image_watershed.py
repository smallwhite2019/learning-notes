# 分水岭算法图像分割
# 详细解说网址：https://www.cnblogs.com/ssyfj/p/9278815.html
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

path = './data/thresh.jpg'
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)     # otsu's二值化
# cv2.imshow('thresh', gray)
# cv2.waitKey(0)
# cv2.destoryAllwindows()

# 形态学操作，进一步消除噪声
kernel = np.ones((3, 3), np.uint8)
# 连续两次开操作，消除图像的噪点
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)

# 3次膨胀,可以获取到大部分都是背景的区域
sure_bg = cv2.dilate(opening, kernel, iterations = 3)

# 距离变换的基本含义是计算一个图像中非零像素点到最近的零像素点的距离，也就是到零像素点的最短距离
# 个最常见的距离变换算法就是通过连续的腐蚀操作来实现，腐蚀操作的停止条件是所有前景像素都被完全
# 腐蚀。这样根据腐蚀的先后顺序，我们就得到各个前景像素点到前景中心[emoji:DBD5DC57][emoji:DBC8DD65]像素点的
# 距离。根据各个像素点的距离值，设置为不同的灰度值。这样就完成了二值图像的距离变换
#cv2.distanceTransform(src, distanceType, maskSize)
# 第二个参数0,1,2 分别表示CV_DIST_L1, CV_DIST_L2 , CV_DIST_C

dist_transform = cv2.distanceTransform(opening, 1, 5)     # 获取距离数据结果
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)     # 获取前景色

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)   #  #保持色彩空间一致才能进行运算，现在是背景空间为整型空间，前景为浮点型空间，所以进行转换


# 获取mask
ret, markers1 = cv2.connectedComponents(sure_fg)

markers = markers1 + 1
markers[unknown == 255] = 0

# 实施分水岭
markers3 = cv2.watershed(img, markers)
img[markers3 == -1] = [0, 0, 255]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destoryAllwindows()