# 直方图反投影，用来做图像分割或者在图像中找寻我们感兴趣的部分
'''
# numpy中的算法
# 目标图像的直方图(M)，（待搜索）输入图像的直方图（I）
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

# roi是我们需要找到的对象或区域，M
path1 = './data/ball-green.jpg'
roi = cv2.imread(path1)
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# target是我们搜索的图像，I
path2 = './data/ball.jpg'
target = cv2.imread(path2)
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

# 用calcHist来找直方图，也可以 用np.histogram2d
M = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
I = cv2.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256])

# 找比率 R = M/I
# 报错，R找不到
h, s, v = cv2.split(hsvt)
B = R[h.ravel(), s.ravel()]
B = np.minimum(B, 1)
B = B.reshape(hsvt.shape[:2])

# 应用一个圆盘算子做卷积
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
cv2.filter2D(B, -1, disc)
B = np.uint8(B)
cv2.normalize(B, B, 0, 255, cv2.NORM_MINMAX)

# 给出阈值
ret, thresh = cv2.threshold(B, 50, 255, 0)

cv2.imshow('ret', ret)
cv2.waitKey(0)
'''

# opencv中的反向投影

import cv2
import numpy as np 

# 要寻找的目标图像
path1 = './data/ball-green.jpg'
roi = cv2.imread(path1)
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# 输入图像
path2 = './data/ball.jpg'
target = cv2.imread(path2)
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

roihist = cv2.calcHist([roi], [0, 1], None, [180, 256], [0, 180, 0, 256])

# 归一化：原始图像，结果图像，映射到结果图像中的最小值，最大值，归一化类型
# cv2.NORM_MINMAX对数组的所有值进行转化， 使它们线性映射到最小值和最大值之间
# 归一化后的直方图便于显示，归一化之后就变成了0到255之间的数啦。

cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)

# 此处卷积可把分散的点连在一起
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dst = cv2.filter2D(dst, -1, disc)

# 阈值
ret, thresh = cv2.threshold(dst, 20,255, 0)

# 别忘了是三通道图像，因此这里使用merge变成3通道
thresh = cv2.merge((thresh, thresh, thresh))

# 按位操作
res = cv2.bitwise_and(target, thresh)

res = np.hstack((target, thresh, res))

# 显示图像，效果并不是很好
cv2.namedWindow('res', 0)
#cv2.cvResizeWindow('res', (800, 400))
cv2.imshow('res', res)
cv2.waitKey(0)
