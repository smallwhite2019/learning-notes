# 摄像机标定与3D重构

# 在机器视觉领域，摄像头的标定指通过技术手段拿到相机的内参、外参及畸变参数。
#     [fx 0  cx]
# P = |0  fy cy|
#     [0  0  0 ]
# init(对象点，图像点)--->对每一张图进行操作--->寻找角点--->寻找亚像素精度角点--->画出角点
# --->通过图像点和对象点找出摄像机的内部参数和畸变矩阵--->畸变矫正--->去除畸变--->计算误差


import cv2
import numpy as np 
import glob


# 设置寻找亚像素角点的参数，采用的停止准则是最大循环次数30和最大误差容限0.001
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.001)
# 要注意的是，棋盘的行、列角点数是内棋盘的，比如上图的行角点数为8，列角点数为5.
# 设置标定板角点的规格。9和6分别根据现有图片进行设置的
objp = np.zeros((9*6, 3), np.float32)   
# 将世界坐标系建在标定板上，所有点的Z坐标全部为0，所以只需赋值x和y
# np.mgrid 创造两个二维数组，每个数组的大小相同（行数由start1:end1:step1决定，列数由start2:end2:step2决定）。其中第一个二维数组b是按列存储，
# 即从start1到end1，然后第二列start1到end1，第三列…；第二个二维数组a是按行存储，第一行从start2到end2，第二行重复…

# >>> a = np.mgrid[0:2, 0:3]
# >>> a
# array([[[0, 0, 0],
#         [1, 1, 1]],

#        [[0, 1, 2],
#         [0, 1, 2]]])

objp[:,:2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)

objpoints = []       # 存储3D点
imgpoints = []       # 存储2D点
# 此代码至少要10张图片进行摄像机标定
# glob符合相应模式的文件列表，需要注意的一点是，该函数对大小写不敏感，.jpg与.JPG是一样的
filename = './data/chessjpg/*.jpg'
images = glob.glob(filename)   # 读取文件夹中.jpg格式的文件
print(images)
# images = './data/chessjpg/chess0.jpg'
for fname in images:
    
    img = cv2.imread(fname)
    # 灰度化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', gray)
    # cv2.waitKey(0)

    # 角点检测
    # ret：输出是否找到角点，找到角点返回1，否则返回0
    # conrers:shape(54, 1, 2) 54是坐标个数，2是（x,y）
    # [[[545.3228 343.05032]] [[602.6792 342.8268]] ...]
    ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
    print(ret, corners)
    # 若找到，则增加物体点和图像点
    if ret == True:
        objpoints.append(objp)

        # 亚像素点级角点检测，基于提取的角点，进一步提高精确度
        # cornerSubPix()参数：
        # image：输入图像，即上式中的gray，最好是8位灰度图，检测效率高；
        # corners：角点初始坐标，即在上个函数中找到的角点的坐标信息；
        # winsize：搜索窗口为 2*winsize+1；
        # zerozone：死区，不计算区域，避免自相关矩阵的奇异性。没有死区，参数为（-1，-1）；
        # criteria：求角点的迭代终止条件。
        # 返回值：
        # corner：角点位置。

        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1),criteria)
        imgpoints.append(corners2)

        # 在图片中绘制棋盘格角点
        img = cv2.drawChessboardCorners(img, (9, 6), corners2, ret)   # opencv绘制函数一般无返回值
        cv2.imshow('img', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

# 标定
# ret为是否解到相机参数，mtx为内参数矩阵，dist为畸变系数，rvecs为旋转向量，tvecs为平移向量
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# 畸变校正
img = cv2.imread('./data/fruit_jibian0.jpg')
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
'''
# 方法一：使用cv2.undistort()和ROI对结果进行裁剪
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# 裁剪图片
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('./data/chessjpg/calibresult.jpg', dst)
'''
# 方法二：使用remapping
mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w, h), 5)
dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# 裁剪图片
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('./data/fruit/fruit_jibian.jpg', dst)

# 存取数据用于3D计算
np.savez('./data/fruit/B.npz', mtx= mtx, dist= dist, rvecs= rvecs, tvecs= tvecs)

# 读取文件

with np.load('./data/fruit/B.npz') as f:
    mtx = f["mtx"]
    dist = f["dist"]
    print("mtx= ", mtx)
    
# 反向投影误差：用来对我们所找到的参数的准确性进行估计
# cv2.projectPoints将对象点转换到图像点
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
    mean_error += error
print("total error: ", mean_error/len(objpoints))


# 注意报错
# 问题一：若无图片显示，即55行ret==False，说明角点找的不对
# 重新在18行选取角点，即可显示图形