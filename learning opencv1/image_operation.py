'''
opencv中的图像处理
'''
# 13颜色空间转换
'''
import cv2
import numpy as np

path = 'cs4.mp4'
cap = cv2.VideoCapture(path)

while(1):
    ret,frame = cap.read()  #获取每一帧
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #转换到HSV
    lower_blue = np.array([110, 50, 50]) # 设置蓝色的阈值
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue) # 根据阈值构建掩膜
    res = cv2.bitwise_and(frame, frame, mask) #对原图像和掩膜进行位运算

    cv2.imshow('frame', frame)
    cv2.waitKey(0)
    cv2.imshow('mask', mask)
    cv2.waitKey(0)
    cv2.imshow('res', res)
    cv2.waitKey(0)
    k = cv2.waitKey(5)&0xff
    if k == 27:
        break
cv2.destroyAllWindows()
'''

#14空间变换
#扩展缩放
'''
import cv2
import numpy as np
path = 'img.jpg'
img = cv2.imread(path)
#下面的None本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子
#因此这里为None
res = cv2.resize(img, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
#or
#这里呢，我们直接设置输出图像的尺寸，所以不用设置缩放因子
height, width = img.shape[:2]
res = cv2.resize(img, (width*2, height*2), interpolation = cv2.INTER_CUBIC)
while(1):
    cv2.imshow('res', res)
    cv2.imshow('img', img)
    if cv2.waitKey(1)&0xff == 27:
        break
cv2.destroyAllWindows()
'''

#平移
#旋转

import cv2
import numpy as np
path = 'img.jpg'
img = cv2.imread(path, 0)
rows, cols = img.shape
#这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
#可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.6)
#第三个参数是输出图像的尺寸中心
dst = cv2.warpAffine(img, M, (2*cols, 2*rows))
while(1):
    cv2.imshow('img', dst)
    if cv2.waitKey(1)&0xff == 27:
        break   
cv2.destroyAllWindows()
