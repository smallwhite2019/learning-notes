# 轮廓的性质
#findContours找轮廓与cv2.imread()读取方式有关，0/2模式可直接找寻，1模式必须转化为gray
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
#ret, thresh = cv2.threshold(gray,127,255,0)

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

path = 'img-air.jpg'
img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
# 长宽比
x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h
print('长宽比为%10.8f' %aspect_ratio)
#Extent 轮廓面积与边界矩形面积的比
area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w * h
extent = float(area)/rect_area
print('轮廓面积与边界矩形面积的比为%10.8f' %extent)
#轮廓面积与凸包面积的比
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
print('轮廓面积与凸包面积的比为%10.8f' %solidity)
#与轮廓面积相等的圆形的直径
area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)
print('直径 %10.8f' %equi_diameter)
#对象的方向
(x,y), (MA, ma), angle = cv2.fitEllipse(cnt)
print((x,y), (MA, ma), angle)
#掩膜
#img.shape一定要用原图形状
mask = np.zeros(img.shape, np.uint8)
#这里一定要使用参数-1，绘制填充的轮廓,可显示原貌
#drawContours三个参数，第一个是原图，第二个是轮廓（是个python列表），第三个是轮廓索引（当为-1时绘制所有轮廓），接下来就是颜色和厚度等
cv2.drawContours(mask, [cnt], 0, (255, 0, 0), -1)
pixelpoints = np.transpose(np.nonzero(mask))
cv2.imshow('img', mask)
cv2.waitKey(0)

#最大值和最小值及他们的位置
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img, mask = mask)
# print('值与位置 %10.8f'%min_val  %max_val  %min_loc  %max_loc)

# mean_val = cv2.mean(img, mask = mask)
# print(mean_val)

#极点
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
img_most = cv2.circle(mask,leftmost, 0, (0,255,0),10)
img_most = cv2.circle(mask,rightmost, 0, (0,255,0),10)
img_most = cv2.circle(mask,topmost, 0, (0,255,0),10)
img_most = cv2.circle(mask,bottommost, 0, (0,255,0),10)
cv2.imshow('img', img_most)
cv2.waitKey()
print(leftmost, rightmost, topmost, bottommost)