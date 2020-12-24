# 图像特征提取

# 角点特征 cv2.Harris()
# params: img, blockSize(邻域), ksize(Sobel孔径), k(公式中参数)
'''
import cv2
import numpy as np 

filename = './data/chessboard.jpg'
img = cv2.imread(filename)
print(img.max(), img.min())
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)  # 输入图像必须是float32,

dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)  # dilate()图像膨胀
img[dst > 0.01*dst.max()] = [0, 0, 255]   # 设置阈值，角点位置用红色标识

cv2.imshow('img', img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destoryAllWindows()

'''

# 亚像素级精确度的角点

'''
# ret, labels, stats, centroids  = cv2.connectedComponentsWithStats(image, connectivity, ltype)
# image：8位单通道图像
# labels：输出标签
# stats：Nx5的矩阵（CV_32S）：[x0, y0, width0, height0, area0;  ... ; x(N-1), y(N-1), width(N-1), height(N-1), area(N-1)]
# centroids：Nx2 质心矩阵（CV_64F ）: [ cx0, cy0; ... ; cx(N-1), cy(N-1)]
# connectivity：默认为8，4- or 8-connected components
# ltype：默认为CV_32S，标签类型 (CV_32S or CV_16U)

# cv2.cornerSubPix(image, corners, winSize, zeroZone, criteria)
# image：输入图像
# corners：角点的初始坐标
# winSize：搜索窗口边长的一半
# zeroZone：搜索区域中间的dead region边长的一半
# criteria：迭代过程的终止条件


import cv2
import numpy as np 

filename = './data/chessboard.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)  # 输入图像必须是float32
# 寻找Harris角点
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
ret, dst = cv2.threshold(dst, 0.01*dst.max(), 255, 0)       # param: 源图像，阈值， 最大阈值， 类型算法（常为0）
dst = np.uint8(dst)
# 找到Harris角点重心
# stats 是bounding box的信息，N*5的矩阵，行对应每个label，五列分别为[x0, y0, width, height, area]
# centroids 是每个域的质心坐标
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
# 定义迭代停止条件
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
# 返回值由角点坐标组成的一个数组（而非图像）
corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)

# 绘制图
res = np.hstack((centroids, corners))
# np.int0可以用来省略小数点后面的数字（非四舍五入）
res = np.int0(res)
img[res[:, 1], res[:, 0]] = [0, 0, 255]   # 红点为Harris角点 
img[res[:, 3], res[:, 2]] = [0, 255, 0]   # 绿色为精度修正后的角点

cv2.imshow('img', img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destoryAllWindows()

# cv2.imwrite('cornerSubPix.jpg', img)
'''

# Shi-Tomasi角点检测&适合于跟踪的图像特征
# cv2.goodFeaturesToTrack()

# cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, corners, mask, blockSize, useHarrisDetector, k)

# image：输入图像（CV_8UC1 CV_32FC1）
# maxCorners：最大角点数目
# qualityLevel：质量水平系数（小于1.0的正数，一般在0.01-0.1之间）
# minDistance：最小距离，小于此距离的点忽略
# corners：输出角点
# mask：掩膜
# blockSize：默认为3，使用的邻域数
# useHarrisDetector：用于指定角点检测的方法，如果是true则使用Harris角点检测，false则使用Shi Tomasi算法。
# k：默认为0.04，Harris角点检测时使用


import cv2
import numpy as np 
from matplotlib import pyplot as plt 

filename = './data/chessboard.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)     # 图像，最大角点数，质量水平系数，最小距离
# 返回的结果是[[311., 250.]]
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()          # a.ravel() #ravel()方法将数组维度拉成一维数组
    cv2.circle(img, (x,y), 3, 255, -1)

plt.imshow(img), plt.show()
