# 构建深度地图

import cv2
import numpy as np
from matplotlib import pyplot as plt 

img1 = cv2.imread('./data/messigray.png', 0)
img2 = cv2.imread('./data/messigray.png', 0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=11)

# numDisparities：即最大视差值与最小视差值之差, 窗口大小必须是16的整数倍，int 型
# blockSize：匹配的块大小。它必须是> = 1的奇数。通常情况下，它应该在3--11的范围内。这里设置为大于11也可以，但必须为奇数。

stereo = cv2.StereoBM_create(numDisparities= 32, blockSize= 5)
disparity = stereo.compute(img1, img2)


plt.imshow(disparity, 'gray')
plt.show()