# 部分VIII 机器学习
# K近邻（K-Nearest Neighbour）

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

# 设置25个包含（x,y）的训练数据
# np.random.randint()返回一个随机整型数，范围从低（包括）到高（不包括），即[low, high)。
trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
print(np.array(trainData))
# 创建标签，红色为0，蓝色为1
responses = np.random.randint(0,2, (25,1)).astype(np.float32)
print(responses)
# 绘制红色家庭
red = trainData[responses.ravel() == 0]
# print(red)
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')

# 绘制蓝色家庭分布
blue = trainData[responses.ravel() == 1] 
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')

'''
# 一个新的测试数据
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')
'''

# 若有大量数据进行测试，可以直接传入一个数组
newcomer = np.random.randint(0, 100, (10, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')

# KNN算法
knn = cv2.ml.KNearest_create()
knn.train(trainData,  cv2.ml.ROW_SAMPLE, responses)
ret, results, neighbour, dist = knn.findNearest(newcomer, 3)

print("results: ", results, "\n")
print("neighbour: ", neighbour, "\n")
print("dist: ", dist, "\n")

plt.show()



# 注意问题：

# 问题一：
# cv2.error: OpenCV(4.1.2) C:\projects\opencv-python\opencv\modules\ml\src\knearest.cpp:82: 
# error: (-215:Assertion failed) new_samples.type() == CV_32F in function 'cv::ml::Impl::train'
# 答： 修改astype(np.float32)

# 问题二：
# TypeError: only integer scalar arrays can be converted to a scalar index
# 答：将knn.train(trainData, responses)改为knn.train(trainData,  cv2.ml.ROW_SAMPLE, responses)

# 问题三：
# 注意opencv版本导致knn不一，此处为knn = cv2.ml.KNearest_create()