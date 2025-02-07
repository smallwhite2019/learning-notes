# 18图像梯度 sobel/scharr/laplacian算子

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

path = 'img.jpg'
img = cv2.imread(path, 0)
#cv2.CV_64F输出图像的深度（数据类型），可以使用-1，与原图像保持一致np.uint8
laplacian = cv2.Laplacian(img, cv2.CV_64F)
#参数1,0为只在x方向求一阶导数，最大可以求2阶导数
sobelx = cv2.Sobel(img, cv2.CV_64F, 1,0, ksize = 5)
#参数0,1为只在y方向求一阶导数，最大可以求2阶导数
sobely = cv2.Sobel(img, cv2.CV_64F, 0,1, ksize = 5)

plt.subplot(2,2,1), plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(laplacian, cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(sobelx, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(sobely, cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()