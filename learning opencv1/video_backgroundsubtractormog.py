# 背景减除法

# createBackgroundSubtractorMOG2()这个函数可以决定是否检测阴影

'''
import cv2
import numpy as np 

filename = './data/cs4.mp4'
cap = cv2.VideoCapture(filename)

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)

    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

'''

# cv2.BackgroundSubtractorGMG()
# 结合了静态背景图像估计和每个像素的贝叶斯分割

import cv2
import numpy as np 

filename = './data/cs4.mp4'
cap = cv2.VideoCapture(filename)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
fgbg = cv2.BackgroundSubtractorGMG()

while(1):
    ret, frame = cap.read()

    fgmask = frame.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.release()
cv2.destroyAllWindows()


# 运行过程中暴露的错误

'''
问题：AttributeError: module 'cv2.cv2' has no attribute 'BackgroundSubtractorGMG'

# 暂时安装opencv-contrib=4.0.1未成功

'''