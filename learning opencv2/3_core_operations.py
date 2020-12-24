# 3.核心操作 
# 图像的基本操作、图像上的算法运算、性能衡量和提升技术
# 学会：访问像素值并修改它们-访问图像属性-设置感兴趣区域(ROI)-分割和合并图像

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

class ImageCoreOperations(object):
    def __init__(self, path, ):
        self.path = path
        pass

    # 访问并修改像素值
        '''
        numpy用于快速数组计算的优化库，因此不建议对单个像素进行修改。
        '''
    def read_resize_img(self):
        img = cv2.imread(self.path)
        # 通过行和列坐标来访问像素值
        px = img[100,100]
        print("图像Img的行列像素值：", px)
        # 仅访问蓝色像素
        px_blue = img[100, 100, 0]
        print("图像img的蓝色像素值：", px_blue)
        # 使用相同方式修改像素值
        img[100, 100] = [255, 255, 255]
        print("修改后的像素值为：", img[100, 100])

    # 访问图像属性
    # 图像属性包括行数、列数、通道数、图像数据类型、像素数等
    def image_properties(self):
        img = cv2.imread(self.path)
        print("图像的形状，返回行、列、通道的元祖：", img.shape)   # h,w
        print("像素的总数：", img.size)
        print("图像的数据类型：", img.dtype)    # 调试时可使用dtype查看数据类型，避免无效的数据类型

    # 图像感兴趣区域ROI
    def image_roi(self):
        img = cv2.imread(self.path, 1)
        ball = img[260:310, 300:390]
        img[250:300, 100:190] = ball
        b, g, r = cv2.split(img)
        print("b, g, r分别为：", b, g, r)
        img = cv2.merge((b, g, r))
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 为图像设置边框
    def image_fill_border(self):
        img = cv2.imread(self.path)
        blue = [255, 0, 0]
        replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
        reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
        reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT101)
        wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
        constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=blue)

        plt.subplot(231), plt.imshow(img, 'gray'), plt.title('original')
        plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('replicate')
        plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('reflect')
        plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('reflect101')
        plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('wrap')
        plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('constant')
        plt.show()



class ImageOperation():

    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2

    # opencv加法是饱和运算，numpy加法是模运算
    def image_add(self):
        x = np.uint8([255])
        y = np.uint8([10])
        print("opencv加法为饱和运算 255+10=265 => 255 ：", cv2.add(x, y))
        print("numpy加法为模运算 265%256 = 4 :", (x+y))

    # 图像融合也是图像加法，但是赋予不同的权重，以使其具有融合或透明的感觉。
    # 图像融合cv2.addWeighted()要求二者图像大小一致，要不然会报维数错误
    # error: (-209:Sizes of input arguments do not match) The operation is neither 'array op array' (where arrays have the same size
    # and the same number of channels), nor 'array op scalar', nor 'scalar op array' in function 'cv::arithm_op'
    def image_fusion(self):
        img1 = cv2.imread(self.path1)
        img2 = cv2.imread(self.path2)
        img2_gray = cv2.imread(self.path2, 0)
        img1 = cv2.resize(img1, img2_gray.shape[::-1])
        img_dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
        cv2.imshow('img', img_dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 在图像特定区域按位AND/OR/NOT/XOR操作，避免混合出现透明现象。
    # 在黑色背景下，就不会出现透明现象。
    def image_bitwise(self):
        img1 = cv2.imread(self.path1)
        img2 = cv2.imread(self.path2)
        # 把logo放置在左上角，故创建ROI
        rows, cols, channels = img2.shape      # rows对应图像高H， cols对应图像宽W
        roi = img1[0:rows, 0:cols]
        cv2.imshow('roi', roi)
        # 现在创建logo掩码,让其logo为黑色，并同时创建相反掩码，logo为白色
        img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        # 现将ROI中的logo区域涂黑, 取roi中与mask中不为0的值对应的像素的值，其他值为0
        # 自己与自己AND运算，mask的作用在于前面两幅图AND后再与掩码做AND，使原图中掩码为1的像
        # roi与mask元素取与,使用带掩码的位操作扣出logo形状
        img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
        # 仅从logo图像中提取logo区域
        img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
        # 将logo放入ROI并修改主图像
        # add为饱和运算，故任何颜色与黑色相加都等于原色，即170(原色)+0(黑色)=170
        # 要突出的地方在img1_bg（背景）中为白色，其他还是背景色
        # 要突出的地方在img2_fg（前景）中为原色，其他为黑色
        # img1_bg+img2_fg（原色》0+黑色=0， 故0=原色）
        dst = cv2.add(img1_bg, img2_fg)
        img1[0:rows, 0:cols] = dst
        cv2.imshow('img2gray', img2gray)
        cv2.imshow('mask', mask)
        cv2.imshow('mask_inv', mask_inv)
        cv2.imshow('img1_bg', img1_bg)
        cv2.imshow('img2_fg', img2_fg)
        cv2.imshow('dst', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imshow('res', img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 使用opencv衡量性能
    # 使用time.time()函数效果更好
    def image_performance(self):
        img1 = cv2.imread(self.path1)
        e1 = cv2.getTickCount()
        for i in range(5, 49, 2):
            img1 = cv2.medianBlur(img1, i)
        e2 = cv2.getTickCount()
        t = (e2 - e1)/cv2.getTickFrequency()
        print(t)




if __name__ == "__main__":

    '''
    # 访问图像的属性
    path = './data/meixi.jpg'
    img_core_operations = ImageCoreOperations(path)
    # img_core_operations.read_resize_img()           # 访问图像的像素
    # img_core_operations.image_properties()          # 访问图像的属性
    # img_core_operations.image_roi()                 # 为图像设置ROI
    # img_core_operations.image_fill_border()         # 为图像设置边框
    '''

    # 图像算术运算
    path1 = './data/meixi.jpg'
    path2 = './data/img-opencv.jpg'
    img_core_operations2 = ImageOperation(path1, path2)
    # img_core_operations2.image_add()
    # img_core_operations2.image_fusion()
    img_core_operations2.image_bitwise()
    # img_core_operations2.image_performance()



    

