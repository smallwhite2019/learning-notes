# 第九部分 计算摄影学
# 图像去噪
# 学习使用非局部平均值去噪算法去除图像中的噪音
# 像素级别的噪声去除是限制在局部邻域的

# cv2.fastNlMeansDenoising()使用对象为灰度图
# cv2.fastNlMeansDenoisingColored()使用对象为彩色图
# cv2.fastNlMeansDenoisingMulti()适用于短时间的图像序列（灰度图像）
# cv2.fastNlMeansDenoisingColoredMulti()适用于短时间的图像序列（彩色图像）
# 共同参数有：
# h: 决定过滤程度。h值高可以很好的去除噪声，但也会把图像的细节抹去（取10的效果不错）
# hForColorComponents:与h相同，但使用与彩色图像。
# templateWindowSize(): 奇数。(推荐值为7)
# searchWindowSize(): 奇数。(推荐值为21)



#　cv2.fastNlMeansDenoisingColored()
'''
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('./data/noise.jpg')
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(dst)
plt.show()
'''

# cv2.fastNlMeansDenoisingMulti()

import cv2 
import numpy as np 
from matplotlib import pyplot as plt 

cap = cv2.VideoCapture('./data/cs4.mp4')

img = [cap.read()[1] for i in range(5)]
gray = [cv2.cvtColor(i, cv2.COLOR_BGR2GRAY) for i in img]
gray = [np.float64(i) for i in gray]
print(gray)
# 创建方差为25的噪声
noise = np.random.randn(*gray[1].shape) * 10
# 图像中增加噪声
noisy = [i + noise for i in gray]

noisy = [np.uint8(np.clip(i, 0, 255)) for i in noisy]

# 3到5帧去噪
dst = cv2.fastNlMeansDenoisingMulti(noisy, 2, 5, None, 4, 7, 35)

plt.subplot(131), plt.imshow(gray[2], 'gray')
plt.subplot(132), plt.imshow(noisy[2], 'gray')
plt.subplot(133), plt.imshow(dst, 'gray')
plt.show()