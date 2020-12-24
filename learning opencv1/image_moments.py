# 轮廓函数
#img = cv2.imread(path, ways):ways位0,1,2；选择读取的方式对轮廓有很大影响作用
#0、2：为读取灰度图
#1：为读取原图
#1.不论读取何种形式的图片，均需转化成灰度图，二进制格式，才可找到轮廓并能够画出轮廓，借助下面两句话
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# ret, thresh = cv2.threshold(gray, 127, 255, 0)
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


'''
#在一幅图上绘制所有的轮廓
import cv2
import numpy as np 
path = 'img.jpg'
img = cv2.imread(path)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
#cv2.findContours在opencv4.1.2版本是返回两个值，分别是轮廓值和轮廓层次结构
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(hierarchy)
img2 = cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow('image', img)
cv2.waitKey()

img2 = cv2.drawContours(imgray, contours, -1, (0,255,0), 3)
cv2.imshow('image', img2)
cv2.waitKey()
img3 = cv2.drawContours(thresh, contours, 3, (0,255,0), 3)

cv2.imshow('image', img3)
cv2.waitKey()
'''


#轮廓特征
#矩
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

path = 'img-shandian.jpg'
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#矩
cnt = contours[0]
M = cv2.moments(cnt)
print(M)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print(cx)
print(cy)


#轮廓面积
area = cv2.contourArea(cnt)
print(area)

#轮廓周长
perimeter = cv2.arcLength(cnt, True)
print(perimeter)

#轮廓近似
epsilon = 0.1*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
print(approx)


#凸包
print("=================")
hull = cv2.convexHull(points = cnt, returnPoints = False)
print(hull)

#凸性检测
k = cv2.isContourConvex(cnt)
print(k)

cnt = contours[0]
#边界矩形，直边界矩形
x, y, w, h = cv2.boundingRect(cnt)
img_bounding = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
img3 = cv2.drawContours(img_bounding, contours, -1, (0,255,0),5)
cv2.imshow('img', img3)
cv2.waitKey()

#边界矩形，旋转边界矩形
print("***************************")
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
print(box)
box = np.int0(box) #int0意味着64位整数
img33 = cv2.drawContours(img, [box], 0, (0,255,0),50)
cv2.imshow('img3', img33)
cv2.waitKey(0)

#最小外接圆

(x,y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img4 = cv2.circle(img, center, radius, (0,255, 0), 5)
img4 = cv2.drawContours(img4, contours, -1, (255,0, 0), 5)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()

#椭圆拟合，返回值为旋转边界矩形的内切圆
ellipse = cv2.fitEllipse(cnt)
im = cv2.ellipse(img, ellipse, (0, 255, 0), 2)
cv2.imshow('img', im)
cv2.waitKey()


