'''
图像方面的一些属性、操作
'''

import cv2
import numpy as np 
path = 'img.jpg'
img = cv2.imread(path)
print(img.item(10, 10, 2))  #img.item()操作，可以直接定位到对应的区域
img.itemset((10, 10, 2), 100) #修改像素值
print(img.item(10, 10, 2))
print('图像属性 ===== ', img.shape)
print('像素数目》》》》》', img.size)
print('数据类型》》》》》', img.dtype)
ball = img[280:340, 330:390]  #ROI
img[273:333, 100:160] = ball

b = img[:,:,0]
img[:,:,2] = 0

cv2.imshow('image', img)
cv2.waitKey(0)