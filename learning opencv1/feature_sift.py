# 放弃，因为opencv4.0.1已不再有cv2.xfeatures2d.SIFT_create()函数，而在opencv3.4.2中还保留，可安装3.4.2版本
# 此程序可用yolo环境运行
# 尺度不变特征变换匹配算法详解
# Scale Invariant Feature Transform(SIFT)



import cv2
import numpy as np 
from matplotlib import pyplot as plt 

filename = './data/img3.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)

img = cv2.drawKeypoints(gray, kp)
cv2.imwrite('./data/img_sift.jpg', img)