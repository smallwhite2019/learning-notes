# 霍夫变换检测形状
# 霍夫变换检测直线
# 直线数学表达式 y= mx + c 或 ρ = xconθ + yxinθ
# 霍夫曼乘1000讲解网址(https://blog.csdn.net/yl_best/article/details/88744997)

'''
# 第一种方法：cv2.HoughLines()
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

path = './data/line.jpg'
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3) # 边缘检测 50为阈值1,150为阈值2

# cv2.HoughLines()四个值，分别为二值化或边缘检测、像素ρ、弧度、阈值
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
lines = lines[:, 0, :]      # 提取为二维
for rho, theta in lines[:]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))   # 可乘500或800，均可
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
'''

# 第二种方法：cv2.HoughLinesP()

import cv2
import numpy as np
from matplotlib import pyplot as plt

path = './data/line.jpg'
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize= 3)

minLineLength = 100     # 线的最短长度，比这个短的线都会被忽略
maxLineGap = 10         # 两条线段之间的最大间隔，如果小于此值，这两条直线就被看成是一条直线。
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
lines = lines[:, 0, :]
for x1, y1, x2, y2 in lines[:]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)




