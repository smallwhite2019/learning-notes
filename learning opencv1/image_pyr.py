# 图像金字塔
'''
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

path = 'img.jpg'
img = cv2.imread(path)
#cv2.pyrDown从一个高分辨率大尺寸的图像向上构建一个金字塔（尺寸变小，分辨率降低）
lower_reso = cv2.pyrDown(img)
#cv2.pyrUp从一个低分辨率小尺寸的图像向上构建一个金字塔（尺寸变大，但分辨率不会增加）
higher_reso = cv2.pyrUp(img)

while(1):
    cv2.imshow('image', img)
    cv2.imshow('lower', lower_reso)
    cv2.imshow('higher', higher_reso)
    if cv2.waitKey(0) == ord('q'):
        break
cv2.destroyAllWindows()
'''


#图像融合

import cv2
import numpy as np, sys 

A = cv2.imread('img.jpg')
B = cv2.imread('img.jpg')

#生成高斯图像金字塔
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

#对A产生laplacian
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1], GE)
    lpA.append(L)
#对B产生laplacian
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1], GE)
    lpB.append(L)

LS = []
for la,lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols/2], lb[:, 0:cols/2:]))
    LS.append(ls)

ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

real = np.hstack((A[:, :cols/2], B[:, cols/2:]))

cv2.imwrite('Pyramid_blending2.jpg', ls_)
cv2.imwrite('Direct_blending.jpg', real)