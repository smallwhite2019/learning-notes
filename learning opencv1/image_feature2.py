
'''
#凸缺陷

import cv2
import numpy as np 

path = 'rect.jpg'
img = cv2.imread(path)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #转换为灰度图
ret, thresh = cv2.threshold(imgray, 127, 255, 0)  #阈值时，imgray应该为灰度图，127为阈值，255为赋值，0为阈值方法
contours, hierarchy = cv2.findContours(thresh, 2, 1) #findContours用来绘制轮廓
cnt = contours[0] #取第0个轮廓

hull = cv2.convexHull(cnt, returnPoints = False) #检测一个曲线是否具有凸性缺陷，返回为True或False
defects = cv2.convexityDefects(cnt, hull)  #帮助找到凸缺陷；返回一个数组，其中每一行包含的值是[起点，终点，最远的点，到最远点的近似距离]

for i in range(defects.shape[0]):
    s,e,f,d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0,255,0],2)
    cv2.circle(img, far, 5, [0, 0, 255], -1)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#point polygon test 求解图像中的一个点到一个对象轮廓的最短距离
#若点在轮廓外部，返回值为负；在轮廓上，为0；在轮廓内部，返回值为正。
#第三个参数measureDist:True,计算最短距离；measureDist:False,判断点与轮廓关系（返回值为+1，-1,0）
dist = cv2.pointPolygonTest(cnt, (50, 50),False)
print(dist)
'''

#形状匹配 matchShapes()
#匹配是根据Hu矩来进行计算的，Hu矩是归一化中心矩的线性组合。

import cv2
import numpy as np

img1 = cv2.imread('img-rect.jpg')
img2 = cv2.imread('rect.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img1, 127, 255, 0)
ret, thresh2 = cv2.threshold(img2, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt1 = contours[0]
contours, hierarchy = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]

ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
print(ret)

