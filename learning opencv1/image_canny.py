# canny边缘检测
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

path = 'img.jpg'
img = cv2.imread(path, 0)
canny = cv2.Canny(img, 150, 200)
plt.subplot(1,2,1), plt.imshow(img, 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2), plt.imshow(canny, 'gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])
plt.show()