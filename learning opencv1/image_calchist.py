
# 绘制直方图

import cv2
import numpy as np
from matplotlib import pyplot as plt
'''
img = cv2.imread('img.jpg')
# cv2.calcHist([images], [channels], mask, [histSize], [range][,hist[,accumulate]] )
hist = cv2.calcHist([img], [0], None, [256], [0,256])

plt.plot(hist)
plt.show()
# cv2.imshow('hist', hist)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 

# img.ravel()将图像转成一维数组，这里没有中括号
hist_np, bins = np.histogram(img.ravel(), 256, [0,256])
plt.plot(hist_np)
plt.show()

#plt.hist(img.ravel(), 256, [0, 256])
#plt.show()

# 绘制多通道直方图
colors = ('b', 'g', 'r')

#对一个列表或数组既要遍历索引又要遍历元素时，使用内置enumerate函数会更加直接，优美的做法
#enumerate会将数组或列表组成一个索引序列，使我们再获取索引和索引内容的时候更加方便
for i, col in enumerate(colors):
    histr = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
plt.show()


# 1.3 使用掩膜
img = cv2.imread('img.jpg', 0)
#create a mask
mask = np.zeros(img.shape[:2], np.uint8)
print(img.shape)
mask[100:300, 100:400] = 255
# cv2.bitwise_and()是对二进制数据进行“与”操作
masked_img = cv2.bitwise_and(img, img, mask = mask)

# calculate histogram with mask and without mask
# check third argument for mask
hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_mask = cv2.calcHist([img], [0], mask, [255], [0, 256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_P40 = cv2.imread('./data/P40.jpg')
img_iphone = cv2.imread('./data/iphone.jpg')
print(img_P40.shape)
print(img_iphone.shape)
mask_P40 = np.zeros(img_P40.shape[:2], np.uint8)
mask_iphone = np.zeros(img_iphone.shape[:2], np.uint8)

mask_P40[900:3300, 200:2800] = 255
mask_iphone[720:1500, 100:900] = 255

masked_P40 = cv2.bitwise_and(img_P40, img_P40, mask = mask_P40)
masked_iphone = cv2.bitwise_and(img_iphone, img_iphone, mask = mask_iphone)
#等比例缩放图片大小
masked_P40=cv2.resize(masked_P40,(int(img_P40.shape[1]/5),int(img_P40.shape[0]/5)))
cv2.imshow('masked_P40',masked_P40)
cv2.waitKey(0)

masked_iphone=cv2.resize(masked_iphone,(int(img_iphone.shape[1]/2),int(img_iphone.shape[0]/2)))
cv2.imshow('masked_iphone',masked_iphone)
cv2.waitKey(0)

