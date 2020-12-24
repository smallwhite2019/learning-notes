# 使用calib3D模块在图像中创建3D效果
# 加载上面camera_biaoding.py文件中的B.npz读取摄像机参数

import cv2
import numpy as np
import glob

# 加载之前保存的摄像机参数
with np.load('./data/chessjpg/B.npz') as X:
    mtx, dist, _, _ = [X[i] for i in ('mtx', 'dist', 'rvecs', 'tvecs')]

# 创建一个函数：draw， 它的参数有棋盘上的角点（使用cv2.findChessboardCorners得到）和要绘制的3D坐标轴上的点。
def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())  # ravel()将多维数组降为一维，会影响原始矩阵
    img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255, 0, 0), 5)
    img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0, 255, 0), 5)
    img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0, 0, 255), 5)
    return img

# 渲染一个立方体
# 需要对draw()函数进行修改

# cv2.drawCountours()函数
# cv2.drawCountours(img, contours, contourIdx, color, thickness)
# 参数说明:
# 1、img：表示输入的需要画的图片；
# 2、contours：findContours函数返回的轮廓；
# 3、contourIdx：轮廓的索引，-1表示绘制所有轮廓；
# 4、color:绘制的轮廓的颜色；
# 5、thickness：绘制的轮廓的线条厚度；

def draw2(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1, 2)
    # 画出绿色背景
    img = cv2.drawContours(img, [imgpts[:4]], -1, (0, 255, 0), -3)
    # 画蓝色线条
    for i,j in zip(range(4), range(4, 8)):  # zip打包为元祖的列表 [(0,4), (1,5), (2,6), (3, 7)]
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]), (255), 3)
    # 画红色线条
    img = cv2.drawContours(img, [imgpts[4:]], -1, (0, 0, 255), 3)
    return img

# 立方体8个角点
axis2 = np.float32([[0, 0, 0], [0, 3, 0], [3, 3, 0], [3, 0, 0], [0, 0, -3], [0, 3, -3], [3, 3, -3], [3, 0, -3]])



# 设置终止条件
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.001)
objp = np.zeros((9*6, 3), np.float32)
objp[:,:2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)
# 设置坐标轴
axis = np.float32([[3, 0, 0], [0, 3, 0], [0, 0, -3]]).reshape(-1, 3)
print(axis)
# 加载图片
filename = './data/chessjpg/*.jpg'
images = glob.glob(filename)

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)

    if ret == True:
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

        # 找到旋转向量和平移向量
        _, rvecs, tvecs, inliers= cv2.solvePnPRansac(objp, corners2, mtx, dist)
        # 对应3D点到图像
        # imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
        # img = draw(img, corners2, imgpts)

        # 立方体
        imgpts, jac = cv2.projectPoints(axis2, rvecs, tvecs, mtx, dist)
        img = draw2(img, corners2, imgpts)

        cv2.imshow('img', img)
        k = cv2.waitKey(0) & 0xff
        if k == 's':
            cv2.imwrite(fname[:6] + '.jpg', img)
cv2.destroyAllWindows()



# 注意问题
# 问题一：
# cv2.solvePnPRansac()返回为四个参数
