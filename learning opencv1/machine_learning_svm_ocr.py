# svm进行手写数据OCR

# 使用方向梯度直方图HOG作为特征向量


import cv2
import numpy as np 

SZ = 20
bin_n = 16           # bins的数量

# svm参数
svm_params = dict(kernel_type= cv2.ml.SVM_LINEAR, svm_type= cv2.ml.SVM_C_SVC, c = 2.67, gamma= 5.383)
affine_flags = cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR

# 使用图像的二阶矩对图片进行抗扭斜处理

# cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) → dst
# 其中：
# src - 输入图像。
# M - 变换矩阵。
# dsize - 输出图像的大小。
# flags - 插值方法的组合（int 类型！）
# borderMode - 边界像素模式（int 类型！）
# borderValue - （重点！）边界填充值; 默认情况下，它为0。
# 上述参数中：M作为仿射变换矩阵，一般反映平移或旋转的关系，为InputArray类型的2×3的变换矩阵。
def deskew(img):
    m = cv2.moments(img)     # 求矩
    if abs(m['mu02']) < 1e-2:
        return img.copy()
    skew = m['mu11']/m['mu02']
    M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
    img = cv2.warpAffine(img, M, (SZ, SZ), flags= affine_flags)
    return img


# 使用方向梯度直方图HOG作为特征向量
# 计算图像X方向和Y方向的sobel导数，然后计算得到每个像素的梯度的方向和大小。把这个梯度转换成16位的整数
# 将图像分为4个小的方块，对每一个小的方块计算它们的朝向直方图，使用梯度大小作为权重
# 这样每一个小方块都会得到一个含有16个成员的向量，4个小方块的4个向量就组成了这个图像的特征向量（包含64个成员）

# dst = cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]])
# 函数返回其处理结果。
# 前四个是必须的参数：
# 第一个参数是需要处理的图像；
# 第二个参数是图像的深度，-1表示采用的是与原图像相同的深度。目标图像的深度必须大于等于原图像的深度；
# dx和dy表示的是求导的阶数，0表示这个方向上没有求导，一般为0、1、2。

def hog(img):
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1)
    mag, ang = cv2.cartToPolar(gx, gy)             # 获取梯度幅度和梯度角度, → magnitude, angle
    bins = np.int32(bin_n * ang /(2 * np.pi))
    bin_cells = bins[:10, :10], bins[10:, :10], bins[:10, 10:], bins[10:, 10:]
    mag_cells = mag[:10, :10], mag[10:, :10], mag[:10, 10:], mag[10:, 10:]
    hists = [np.bincount(b.ravel(), m.ravel(), bin_n) for b, m in zip(bin_cells, mag_cells)]
    hist = np.hstack(hists)
    return hist

img = cv2.imread('./data/digits.png', 0)
#切割图像
cells = [np.hsplit(row, 100) for row in np.vsplit(img, 50)]

# 一半为训练数据一半为测试数据
train_cells = [i[:50] for i in cells]
test_cells = [i[50:] for i in cells]

# 对所有的训练图像做抗扭斜处理
deskewed = [list(map(deskew, row)) for row in train_cells]
# 计算所有训练图像的hog
hogdata = [list(map(hog, row)) for row in deskewed]
# 训练数据的特征值和标签
trainData = np.float32(hogdata).reshape(-1, 64)
responses = np.int32(np.repeat(np.arange(10),250)[:, np.newaxis])

# 初始化svm
svm = cv2.ml.SVM_create()
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setType(cv2.ml.SVM_C_SVC)
svm.setC(2.67)
svm.setGamma(5.383)
svm.train(trainData, cv2.ml.ROW_SAMPLE, responses)
svm.save('svm_data.dat')

# 现在测试
deskewed = [list(map(deskew, row)) for row in test_cells]
hogdata = [list(map(hog, row)) for row in deskewed]
testData = np.float32(hogdata).reshape(-1, bin_n * 4)
# 检测准确率
result = svm.predict(testData)[1]   # 注意该地方为tuple元祖类型
print(result.size)
mask = result == responses
correct = np.count_nonzero(mask)
accuracy = correct * 100.0 / result.size
print(accuracy)





# 问题一：
# trainData = np.float32(hogdata).reshape(-1, 64)
# TypeError: float() argument must be a string or a number, not 'map'
# 答案：hogdata = [list(map(hog, row)) for row in deskewed]    加入list(map())，只包含在map中即可


# 问题二：
# cv2.error: OpenCV(4.1.2) C:\projects\opencv-python\opencv\modules\ml\src\svm.cpp:1630: error: (-5:Bad argument) 
# in the case of classification problem the responses must be categorical; either specify varType when creating TrainData,
#  or pass integer responses in function 'cv::ml::SVMImpl::train'
#  答案：responses = np.float32(np.repeat(np.arange(10),250)[:, np.newaxis]) 标签改为np.int32