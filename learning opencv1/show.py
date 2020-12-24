'''
import numpy as np 
import cv2
img = cv2.imread("img.jpg", 0)  #load an color in grayscale
cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # 窗口调整大小
cv2.imshow('image', img)
cv2.waitKey(0)  # 键盘绑定函数
cv2.destroyAllWindows() #可以轻易删除任何我们建立的窗口
cv2.imwrite('messigray.png', img)


import numpy as np
import cv2
img = cv2.imread('img.jpg', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)&0xFF
if k == 27:   # wait for ESC to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('messigray2.png',img)
    cv2.destroyAllWindows()

'''
# 使用matplotlib
import numpy as np
import cv2
from matplotlib import pyplot as plt 
img = cv2.imread('img.jpg', 0) #0为读取灰度图,1为读取原图
result = np.asarray(img)
print(result)
img_data = np.array(img, dtype= 'float32')
#print(img_data.shape)
img_data = np.expand_dims(img_data, 0)
#print(img_data.shape)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([])  # to hide tick values on x and y axis
plt.yticks([])
plt.show()

