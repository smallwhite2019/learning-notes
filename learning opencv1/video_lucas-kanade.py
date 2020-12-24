# opencv版本:4.0.1
# opencv中的Lucas-Kanade光流

'''
# 函数说明：
# p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, maxCorners, qualityLevel, minDistance)

# 输入参数：
# old_gray：灰度图像
# mask：掩码
# maxCorners：角点最大数量
# qualityLevel：品质因子，特征值越大的越好，用来筛选，品质因子越大，得到的角点越少
# minDistance：最小距离，相当于在这个距离中有其他角点比这个角点更适合，就舍弃这个弱的角点



import numpy as np 
import cv2

# 导入视频
filename = './data/cs4.mp4'
cap = cv2.VideoCapture(filename)



# cv::TermCriteria::TermCriteria ( int  type, int maxCount, double epsilon） 

# 这个类里面的三个参数意思是：

# 1) type:The type of termination criteria, 判定迭代终止的条件类型，要么只按count算，要么只按EPS算，要么两个条件达到一个就算结束
# COUNT：按最大迭代次数算
# EPS：就是epsilon，按达到某个收敛的阈值作为求解结束标志
# COUNT + EPS：要么达到了最大迭代次数，要么按达到某个阈值作为收敛结束条件。
# 2) maxCount:The maximum number of iterations or elements to compute. 具体的最大迭代的次数是多少
# 3) epsilon:  The desired accuracy or change in parameters at which the iterative algorithm stops. 具体epsilon值是多少。

# 定义lucas-kanade 算法所需的光流参数
# maxLevel为使用的金字塔层数
lk_params = dict(winSize = (15, 15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT, 10, 0.03))

# 创建随机颜色, size(100, 3)为100行3列
color = np.random.randint(0, 255, (100, 3))

# 使用第一帧图像并做灰度处理
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
# shiTomasi中心点检测参数， 角点检测
feature_params = dict(maxCorners = 100, qualityLevel = 0.3, minDistance = 7, blockSize = 7)
p0 = cv2.goodFeaturesToTrack(old_gray, mask= None, **feature_params)

# 创建掩膜用于画框
mask = np.zeros_like(old_frame)

while(1):
    ret, frame = cap.read()
    if frame is None:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 需要传入前一帧和当前图像以及前一帧检测到的角点
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # 读取运动了的角点st ==1 表示检测到的运动物体， 即v和u表示为0
    good_new = p1[st == 1]
    good_old = p0[st == 1]
    
    # 绘制跟踪轨迹
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)     # 源图像，左上顶点，右下顶点，颜色，线条
        frame = cv2.circle(frame, (int(a), int(b)), 5, color[i].tolist(), 1)                # 源图像，圆心，半径，颜色，线条
    # 将两个图片进行结合，并进行图片展示
    img = cv2.add(frame, mask)

    cv2.imshow('frame', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
    # 更新之前的帧和点
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)

cv2.destroyAllWindows()
cap.release()
'''

#稠密光流算法
# Gunner_Farneback()算法 :计算稠密光流的方法，返回带有光流向量（u,v）的双通道数组。
# 光流的大小和方向通过计算得到，使用颜色对结果编码便于观察。方向对应H(Hue)通道，大小对应V(Value)通道。

import cv2
import numpy as np 

filename = './data/cs4.mp4'
cap = cv2.VideoCapture(filename)

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255

while(1):
    ret, frame2 = cap.read()
    if frame2 is None:
        break 
    next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    # cv2.calcOpticalFlowFarneback(prev,next,flow,pyr_scale,levels,winsize,iterations,poly_n,poly_sigma,flags)
    # flow 计算的流量图像具有与prev相同的大小并为CV_32FC2类型;
    # pyr_scale 参数，为每张图描述图片比例以构建金字塔。取0.5意味经典金字塔，下一层比上一层小两倍。
    # poly_n 使用像素邻域大小查找每个像素的多项式展开，经验值5,7.
    # poly_sigma 高斯分布的标准偏差，用来平滑的导数用于多项式展开的基础。经验值1.1或1.5.
    # flag 取0计算快，取1计算慢但准确。


    flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    # cv2.cartToPolar 计算二维向量的大小和角度。
    # 省略所有的冒号来用省略号代替,大家看这个a[:, :, None]和a[…, None]的输出是一样的，就是因为…代替了前面两个冒号。
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180/np.pi/2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow('frame2', rgb)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('opticalfb.jpg', frame2)
        cv2.imwrite('opticalhsv.jpg', rgb)
    prvs = next

cap.release()
cv2.destroyAllWindows()







# 运行过程中暴露的错误

'''
问题一：DeprecationWarning: an integer is required (got type numpy.float32).  Implicit conversion to integers using __int__ is deprecated, and may be removed in a future version of Python.

# 将69行坐标(a, b)(c, d)修改为(int(a), int(b)), (int(c), int(d))，转化为int型

问题二：cv2.error: OpenCV(4.1.2) C:\projects\opencv-python\opencv\modules\imgproc\src\color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'

# 54行添加 非空语句
if frame is None:
    break
'''