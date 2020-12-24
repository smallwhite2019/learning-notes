# 4.opencv图像处理
# 改变颜色空间、图像的几何变换、图像阈值、图像平滑、形态转换、图像梯度、canny边缘检测、图像金字塔、opencv中的轮廓、
# 轮廓特征、轮廓属性、轮廓分层、直方图、傅里叶变换、模板匹配、霍夫线变换、霍夫圈变换、图像分割与分水岭算法、交互式前景提取使用GrabCUT算法


import cv2
import numpy as np
from matplotlib import pyplot as plt

class ImageProcessing():
    def __init__(self, path_picture, path_video, path_picture2):
        self.path_picture = path_picture
        self.path_video = path_video
        self.path_picture2 = path_picture2

    # 常用BGR→灰色空间（cv2.COLOR_BGR2GRAY），BGR→HSV(cv2.COLOR_BGR2HSV)
    def change_color(self):
        # flags = [i for i in dir(cv2) if i.startswith('COLOR_')]       # dir(cv2)要去找cv2所在的文件夹才能运行
        # print(flags)

        '''
        在HSV空间比BGR空间更容易表示颜色，实现对象跟踪功能。
        '''
        # 捕获视频
        cap = cv2.VideoCapture(self.path_video)
        while(True):
            # 读取帧
            ret, frame = cap.read()
            if not ret:
                break
            # 转换颜色空间，HSV→BGR
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # 定义hsv中蓝色的范畴
            lower_hsv = np.array([110, 10, 50])
            higher_hsv = np.array([130, 255, 255])
            # 设hsv的阈值使得只取蓝色
            mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
            # 将掩膜和图像相加
            res = cv2.bitwise_and(frame, frame, mask=mask)
            cv2.imshow('frame',frame)
            cv2.imshow('mask', mask)
            cv2.imshow('res', res)
            k = cv2.waitKey(10) & 0xff
            if k==27:
                break
            cv2.destroyAllWindows()


    def image_transform(self):
        '''     缩放 /平移 /旋转 /仿射变换 /透视变换   '''
        img = cv2.imread(self.path_picture)             # 用于缩放、平移、旋转、仿射变换
        img2 = cv2.imread(self.path_picture2)           # 用于透视变换
        print("原图尺寸：", img.shape[:2])
        # res = cv2.resize(img, None, fx= 2, fy= 2, interpolation= cv2.INTER_CUBIC)       # cv2.INTER_CUBIC用于缩放
        # 或者
        height, width = img.shape[:2]
        rows, cols = img.shape[:2]
        res = cv2.resize(img, (2*width, 2*height), interpolation= cv2.INTER_CUBIC)
        # 平移
        M = np.float32([[1,0,100], [0,1,50]])
        img_pingyi = cv2.warpAffine(img, M, (rows, cols))
        # 旋转
        # cols-1和rows-1是坐标限制
        M_rotate = cv2.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)  # 类似于（x,y）中心点坐标
        img_rotate = cv2.warpAffine(img, M_rotate, (cols, rows))  # cols=宽width rows=高height

        # 仿射变换：平面
        pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
        pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
        M_transform = cv2.getAffineTransform(pts1, pts2)
        img_transform = cv2.warpAffine(img2, M_transform, (cols, rows))
        plt.subplot(121), plt.imshow(img2), plt.title('Input')
        plt.subplot(122), plt.imshow(img_transform), plt.title('Output')
        plt.show()

        # 透视变换：空间
        img2_rows, img2_cols = img2.shape[:2]
        img2_pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
        img2_pts2 = np.float32([[0,0], [300, 0], [0, 300], [300, 300]])
        M_im2 = cv2.getPerspectiveTransform(img2_pts1, img2_pts2)
        img2_transform = cv2.warpPerspective(img2, M_im2, (img2_cols, img2_rows))
        plt.subplot(121), plt.imshow(img2), plt.title("origin input")
        plt.subplot(122), plt.imshow(img2_transform), plt.title("output")
        plt.show()

        print("放大后的尺寸：", res.shape[:2])
        cv2.imshow('res', res)
        cv2.imshow('img_pingyi', img_pingyi)
        cv2.imshow('img_rotate', img_rotate)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def image_threshold(self):
        '''  图像阈值/简单阈值/otsu的二值化   '''
        # 简单阈值，如果像素值小于阈值，则将其设置为 0，否则将其设置为最大值。
        img1 = cv2.imread(self.path_picture, 0)
        ret, thresh1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)
        ret, thresh3 = cv2.threshold(img1, 127, 255, cv2.THRESH_TRUNC)
        ret, thresh4 = cv2.threshold(img1, 127, 255, cv2.THRESH_TOZERO)
        ret, thresh5 = cv2.threshold(img1, 127, 255, cv2.THRESH_TOZERO_INV)
        titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
        imgs = [img1, thresh1, thresh2, thresh3, thresh4, thresh5]
        for i in range(6):
            plt.subplot(2,3,i+1), plt.imshow(imgs[i], 'gray'), plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
        plt.show()

        # 自适应阈值：解决光照问题
        img2 = cv2.imread(self.path_picture2, 0)
        img2 = cv2.medianBlur(img2, 5)
        ret, th1 = cv2.threshold(img2, 175, 255, cv2.THRESH_BINARY)
        # 11为Block size, 2为C值
        th2 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        th3 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)        # 高斯效果好
        titles = ['Original image', 'Global Thresholding', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
        images = [img2, th1, th2, th3]
        for i in range(4):
            plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray'), plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
        plt.show()
    # otsu二值化避免了必须选择一个值并自动确定它的情况


    def image_filter(self):
        '''    2D卷积（图像过滤）/图像模糊（图像平滑）/      '''
        '''
        blur = cv2.blur(img, (5,5))         # 平均
        blur = cv2.GaussianBlur(img, (5,5), 0)          # 高斯模糊
        median = cv2.medianBlur(img, 5)                 # 中值滤波
        blur = cv2.bilateralFilter(img, 9, 75, 75)      # 双边滤波
        '''


        img = cv2.imread(self.path_picture2)
        kernel = np.ones((5,5), np.float32) / 25
        img_filter = cv2.filter2D(img, -1, kernel)
        plt.subplot(121), plt.imshow(img), plt.title('original'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img_filter), plt.title('averaging'), plt.xticks([]), plt.yticks([])
        plt.show()

    def image_morphological_transformations(self):
        '''  形态学转换 /侵蚀'''
        # 一般在二进制图像上执行
        img = cv2.imread(self.path_picture, 0)
        kernel = np.ones((5,5), np.uint8)
        erosion = cv2.erode(img, kernel, iterations= -1)





if __name__ == '__main__':
    path_picture = './data/meixi.jpg'
    path_video = './data/cs4.mp4'
    path_picture2 = './data/sudoku.jpg'
    image_processing = ImageProcessing(path_picture, path_video, path_picture2)
    # image_processing.change_color()       # 改变色彩
    # image_processing.image_transform()    # 图像几何变换
    # image_processing.image_threshold()    # 图像阈值
    image_processing.image_filter()         # 图像平滑

