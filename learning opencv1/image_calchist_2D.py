
# 22.3 opencv中的2D直方图

import cv2
import numpy as np 

path = './data/img.jpg'
img = cv2.imread(path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

cv2.imshow('hist', hist)
cv2.waitKey(0)


# numpy中的2D直方图

import numpy as np 
import cv2
from matplotlib import pyplot as plt 

path = './data/img.jpg'
img = cv2.imread(path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)
hist, xbins, ybins = np.histogram2d(h.ravel(), s.ravel(), [180, 256], [[0, 180], [0, 256]]) 
plt.imshow(hist, interpolation= 'nearest')
plt.show()

# plt.imshow()显示彩色图，与cv2.imshow()显示灰度图

import cv2
import numpy as np
from matplotlib import pyplot as plt 

path = './data/img.jpg'
img = cv2.imread(path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

plt.xlabel('s')
plt.ylabel('h')
plt.imshow(hist, interpolation= 'nearest')
plt.show()
