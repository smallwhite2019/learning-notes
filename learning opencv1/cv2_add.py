import cv2
import numpy as np 

# 图像加法
# x = np.uint8([250])
# y = np.uint8([10])
# print(cv2.add(x,y))

# #图像混合
# path1 = 'img.jpg'
# path2 = 'messigray.png'
# img1 = cv2.imread(path1)
# print(img1.size, img1.dtype)
# img2 = cv2.imread(path2)
# print(img2.size, img2.dtype)
# dst = cv2.addWeighted(img1, 0.2, img2, 0.8, 0) 


# 按位运算
path1 = 'img3.jpg'
path2 = 'img2.png'
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# img2gray：输入的图片，需要是灰度图  mask ：输出的图片  ret = 175   阈值，既比较值 Maxval = 255，模式：  1、cv2.THRESH_BINARY， 大于Thresh ，取maxval。反之取 0
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask) #按位非运算

cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.waitKey(0)
#分别从背景中抠出logo的位置，以及从logo图中抠出logo
#自己与自己AND运算，mask的作用在于前面两幅图AND后再与掩码做AND，使原图中掩码为1的像素变为1（全黑）
img1_bg = cv2.bitwise_and(roi, roi, mask = mask)

img2_fg = cv2.bitwise_and(img2, img2, mask = mask_inv)

cv2.imshow('img1_bg',img1_bg)
cv2.imshow('mask_inv',img2_fg)
cv2.waitKey(0)

dst = cv2.add(img1_bg,  img2_fg)# 结合背景和logo
img1[0:rows, 0:cols] = dst



cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindow()