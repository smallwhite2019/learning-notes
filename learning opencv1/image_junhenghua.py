
# 直方图均衡化

#numpy进行均衡化

import  cv2
import numpy as np 
from matplotlib import pyplot as plt 

path = './data/img.jpg'
img = cv2.imread(path, 0)

cv2.imshow('img', img)
cv2.waitKey(0)

# flatten()将数组变成一维
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
# 计算累计分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()


plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(), 256, [0, 256], color= 'r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc = 'upper left')
plt.show()


# 进行直方图均衡化
# 构建numpy掩膜数组，cdf为原数组，当数组元素为0时， 掩盖（计算时被忽略）
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
# 对被掩盖的元素赋值，这里赋值为0
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img2 = cdf[img]

hist, bins = np.histogram(img2.flatten(), 256, [0, 256])
# 计算累计分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()


plt.plot(cdf_normalized, color = 'b')
plt.hist(img2.flatten(), 256, [0, 256], color= 'r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc = 'upper left')
plt.show()

cv2.imshow('img', img2)
cv2.waitKey(0)

# opencv直方图均衡化
path = './data/img.jpg'
img = cv2.imread(path, 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imshow('res', res)
cv2.waitKey(0)

# opencv CLAHE有限对比适应性直方图均衡化（自适应均衡化）

import numpy as np
import cv2

path = './data/img.jpg'
img = cv2.imread(path, 0)
# 实例化自适应直方图均衡化函数
clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))
# 进行自适应均衡化图像
cl = clahe.apply(img)
cv2.imshow('calhe', cl)
cv2.waitKey(0)
