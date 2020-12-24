# 图像平滑
'''
import cv2
import numpy as np  
from matplotlib import pyplot as plt 

path = 'img.jpg'
img = cv2.imread(path)
cv2.imshow('image', img)
kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
cv2.imshow('dst', dst) #显示为BGR格式
plt.subplot(121), plt.imshow(img), plt.title('original')  #plt显示为RGB格式，两者颜色有差别
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('averaging')
plt.xticks([]), plt.yticks([])
plt.show()

'''
'''
#图像模糊（图像平滑）

import cv2
import numpy as np
from matplotlib import pyplot as plt

path = 'img.jpg'
img = cv2.imread(path)
#blur = cv2.blur(img, (5,5))
#blur = cv2.GaussianBlur(img, (5,5), 0) #高斯滤波 
blur = cv2.bilateralFilter(img, 9, 75, 75) #双边滤波

plt.subplot(121), plt.imshow(img), plt.title('original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('blur')
plt.xticks([]), plt.yticks([])
plt.show()
'''


#结构化元素
import cv2
a = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
print(a)
b = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
print(b)
c = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))
print(c)

