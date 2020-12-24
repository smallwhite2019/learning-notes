
'''
# 对ORB描述符进行蛮力匹配

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

filename = './data/ball.jpg'
filename2 = './data/ball_face.jpg'
img = cv2.imread(filename, 0)
img2 = cv2.imread(filename2, 0)

# 创建ORB
orb = cv2.ORB_create()
# 寻找并检测关键点
kp1, des1 = orb.detectAndCompute(img, None)
kp2, des2 = orb.detectAndCompute(img2, None)
# 创建BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck= True)
# 匹配描述，Matcher.match()获取最佳匹配
# 返回一个DMatch对象列表，具有下列属性：
# DMatch.distance-描述符之间的距离。越小越好
# DMatch.trainIdx-目标图像中描述符的索引
# DMatch.queryIdx-查询图像中描述符的索引
# DMatch.imgIdx-目标图像的索引
matches = bf.match(des1, des2)    
# 按照距离排序
matches = sorted(matches, key= lambda x: x.distance)
# cv2.drawMatches()绘制匹配的点
img3 = cv2.drawMatches(img, kp1, img2, kp2, matches[:10], None, flags=2)
plt.imshow(img3), plt.show()

'''

# 对SIFT描述符进行蛮力匹配和比值测试
'''
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

filename = './data/ball.jpg'
filename2 = './data/ball_face.jpg'
img = cv2.imread(filename, 0)
img2 = cv2.imread(filename2, 0)

# 创建sift
sift = cv2.xfeatures2d.SIFT_create()
# 寻找并检测关键点
kp1, des1 = sift.detectAndCompute(img, None)
kp2, des2 = sift.detectAndCompute(img2, None)
# 创建BFMatcher
bf = cv2.BFMatcher()
# 匹配描述，Matcher.match()获取最佳匹配
# 返回一个DMatch对象列表，具有下列属性：
# DMatch.distance-描述符之间的距离。越小越好
# DMatch.trainIdx-目标图像中描述符的索引
# DMatch.queryIdx-查询图像中描述符的索引
# DMatch.imgIdx-目标图像的索引
matches = bf.knnMatch(des1, des2, k=2)    
# 比值测试，首先获取与A距离最近的点B（最近）和C（次近），只有当B/C小于阈值时（0.75）才被认为是匹配，
# 因为假设匹配是一一对应的，真正的匹配的理想距离为0
good = []
for m, n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m]) 
# cv2.drawMatches()绘制匹配的点
img3 = cv2.drawMatchesKnn(img, kp1, img2, kp2, good[:10], None, flags=2)
plt.imshow(img3), plt.show()

'''

# FLANN匹配器


# 联合使用特征提取和calib3d模块中的findHomography在复杂图像中查找已知对象

