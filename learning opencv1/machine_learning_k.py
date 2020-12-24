# opencv中的K值聚类

# 特征为一列
'''
# cv2.kmeans()
# 输入参数：
# samples: 应该为np.float32类型的数据，每个特征应该放在一列
# nclusters(K): 聚类的最终数目
# criteria： 终止迭代条件，三个成员(type, max_iter, epsilon)
# attempts: 使用不同的起始标记来执行算法的次数。算法会返回紧密度最好的标记。紧密度也会作为输出被返回。
# flags: 用来设置如何选择起始重心。两个选择：cv2.KMEANS_PP_CENTERS和cv2.KMEANS_RANDOM_CENTERS

# 输出参数：
# compactness: 紧密度，返回每个点到相应重心的距离的平方和。
# labels: 标志数组(与上一节提到的代码相同)， 每个成员被标记为0,1等
# centers: 由聚类的中心组成的数组

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

x = np.random.randint(25, 100, 25)
y = np.random.randint(175, 255, 25)
z = np.hstack((x, y))
z = z.reshape((50, 1))   # 将特征转化为一列
z = np.float32(z)
plt.hist(z, 256, [0, 256])  # 长度为50，取值范围为0到255的向量z
plt.show()

# 设置终止条件
criteria = (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 10, 10)
# 设置标志位
flags = cv2.KMEANS_RANDOM_CENTERS

# 使用kmeans
compactness, labels, centers = cv2.kmeans(z, 2, None, criteria, 10, flags)

A = z[labels == 0]
B = z[labels == 1]

plt.hist(A, 256, [0, 256], color= 'r')
plt.hist(B, 256, [0, 256], color= 'g')
plt.hist(centers, 32, [0, 256], color= 'y')
plt.show()
'''

# 特征为两列
'''
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

x = np.random.randint(25, 50, (25, 2))
y = np.random.randint(60, 85, (25, 2))
print((x, y))
z = np.vstack((x, y))
z = np.float32(z)

criteria = (cv2.TERM_CRITERIA_COUNT + cv2.TERM_CRITERIA_EPS, 10, 10)
conpactness, labels, centers = cv2.kmeans(z, 2, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

A = z[labels.ravel() == 0]
print(labels.ravel())
B = z[labels.ravel() == 1]

plt.scatter(A[:, 0], A[:, 1])
plt.scatter(B[:, 0], B[:, 1], c= 'r')
plt.scatter(centers[:, 0], centers[:, 1], s = 80, c= 'y', marker= 's')
plt.xlabel('Height'), plt.ylabel('Weight')
plt.show()

'''

# 颜色量化
import cv2
import numpy as np
from matplotlib import pyplot as plt 

img = cv2.imread('./data/ball.jpg')
z = img.reshape(-1, 3)
z = np.float32(z)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 10)
k = 8
compactness, labels, center = cv2.kmeans(z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
res = center[labels.flatten()]
res2 = res.reshape((img.shape))


cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()

