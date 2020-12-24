# 图像修补
# 利用坏点周围的像素取代坏点，这样它看起来和周围像素就比较像啦

import cv2 
import numpy as np

img = cv2.imread('./data/meixi.jpg', 0)
# mask = np.zeros(img.shape[:2], np.uint8)
img2 = cv2.imread('./data/meixi2.jpg', 0)

mask = cv2.inRange(img, 0, 100)
res = cv2.bitwise_and(img, img, mask= mask)

# mask = np.zeros(img.shape[:2], np.uint8)
# mask[100:300, 100:400] = 255
cv2.imshow('mask', mask)
cv2.waitKey(0)


res = cv2.bitwise_and(img, img, mask= mask)

cv2.imshow('res', res)
cv2.waitKey(0)

cv2.imwrite('./data/mask_mei.jpg', mask)
mask = cv2.imread('./data/mask_mei.jpg', 0)
# mask = cv2.imread('mask2.jpg', 0)

dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()