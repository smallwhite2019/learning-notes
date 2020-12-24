# fast算法、BRIEF描述符、

'''
# 角点检测的FAST算法
# 运行完该程序没多大变化

import cv2
import numpy as np
from matplotlib import pyplot as plt 

filename = './data/img.jpg'
img = cv2.imread(filename, 0)
# 初始化fast默认值
fast = cv2.FastFeatureDetector_create(threshold= 20, nonmaxSuppression=True, type= cv2.FAST_FEATURE_DETECTOR_TYPE_5_8)   # opencv3.4之后的版本
# 找关键点
kp = fast.detect(img, None)
img2 = cv2.drawKeypoints(img, kp, None, color = (255, 0, 0))

print("Threshold: ", fast.getThreshold())
print("nonmaxSuppression: ", fast.getNonmaxSuppression())
print("neighborhood: ", fast.getType())
print("Total Keypoints with nonmaxSuppression: ", len(kp))

cv2.imwrite('./data/img22.jpg', img2)
# 未使用nms
fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)
print("Total Keypoints without nonmaxSuppression: ", len(kp))

img3 = cv2.drawKeypoints(img, kp, None, color = (255, 0, 0))
cv2.imwrite('./data/img33.jpg', img3)
'''

# BRIEF算法
'''
# 该算法有问题
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

filename = './data/img.jpg'
img = cv2.imread(filename, 0)
# 初始化star检测器
star = cv2.FeatureDetector_create("STAR")

# 初始化BRIEF提取器
brief = cv2.DescriptorExtractor_create('BRIEF')

# 寻找star关键点
kp = star.detect(img, None)

# 计算关键点
kp, des = brief.compute(img, kp)
print(brief.getInt('bytes'))
print(des.shape)
'''

# ORB算法
# 快速特征点提取和描述的算法
'''
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

filename = './data/img.jpg'
img = cv2.imread(filename, 0)
# 创建orb
orb = cv2.ORB_create()
# 找到orb中的关键点
kp = orb.detect(img, None)
# 使用orb计算描述符
kp, des = orb.compute(img, kp)
# 只绘制关键点、位置，不绘制大小和方向
img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags= 0)
plt.imshow(img2), plt.show()
# cv2.imshow('img2', img2)
# cv2.waitKey(0)
'''