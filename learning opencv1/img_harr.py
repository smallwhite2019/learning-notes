# haar特征分类器为基础的面部检测技术

import cv2
import numpy as np 

# 创建人脸检测的对象
face_cascade = cv2.CascadeClassifier('D:\\Program Data\\Anaconda3\\envs\\opencv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
# 创建眼睛检测的对象
eye_cascade = cv2.CascadeClassifier('D:\\Program Data\\Anaconda3\\envs\\opencv\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

# 读取图片并转化为灰度图
img = cv2.imread('./data/img.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 检测面部再检测眼部
# 参数：输入图像， 每次图像尺寸减小的比例尺度， 表示每一个目标至少要被检测到5次才算是真的目标（因为周围的像素和不同的窗口大小都可以检测到人脸）
faces = face_cascade.detectMultiScale(gray, 1.3, 5)   

for (x, y, w, h) in faces:
    # 画出人脸的矩形，传入左上角和右下角坐标 矩形颜色和线条宽度
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # 把脸单独拿出来
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # 在脸上检测眼睛，
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
