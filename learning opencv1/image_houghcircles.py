# Hough圆环变换
import cv2
import numpy as np 

path = './data/img-opencv.jpg'
img = cv2.imread(path, 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# image为输入图像，需要灰度图
# method为检测方法,常用CV_HOUGH_GRADIENT，霍夫梯度法，它可以使用边界的梯度信息
# dp为检测内侧圆心的累加器图像的分辨率于输入图像之比的倒数，
# 如dp=1，累加器和输入图像具有相同的分辨率，如果dp=2，累计器便有输入图像一半那么大的宽度和高度
# minDist表示两个圆之间圆心的最小距离
# param1有默认值100，它是method设置的检测方法的对应的参数，对当前唯一的方法霍夫梯度法cv2.HOUGH_GRADIENT，
# 它表示传递给canny边缘检测算子的高阈值，而低阈值为高阈值的一半
# param2有默认值100，它是method设置的检测方法的对应的参数，对当前唯一的方法霍夫梯度法cv2.HOUGH_GRADIENT，
# 它表示在检测阶段圆心的累加器阈值，它越小，就越可以检测到更多根本不存在的圆，而它越大的话，能通过检测的圆就更加接近完美的圆形了
# minRadius有默认值0，圆半径的最小值
# maxRadius有默认值0，圆半径的最大值
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2= 50, minRadius = 0, maxRadius = 0)
circles = np.uint16(np.around(circles))


# cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
#     根据给定的圆心和半径等画圆
#     img：输入的图片data
#     center：圆心位置
#     radius：圆的半径
#     color：圆的颜色
#     thickness：圆形轮廓的粗细（如果为正）。负厚度表示要绘制实心圆。
#     lineType： 圆边界的类型。
#     shift：中心坐标和半径值中的小数位数。


for i in circles[0,:]:
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 0, 255), 2)
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 255, 0), 3)

cv2.imshow('detected circles', cimg)
cv2.waitKey(0)
cv2.destoryAllWindows()
