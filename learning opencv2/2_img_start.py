# 图像入门
# 读取图像、写入图像、相机中读取视频、文件中播放视频、保存视频、绘图功能、鼠标作为画笔、轨迹栏作为调色板
# opencv 环境：4.1.2
# OpenCV加载的彩色图像处于BGR模式。但是Matplotlib以RGB模式显示

import cv2
import numpy as np
from matplotlib import pyplot as plt 
import tensorflow as tf 


class ImgGetStart():
    def __init__(self, path):
        self.path = path
        

    # 读取图像cv2.imread()
    def read_image(self):
       
        # 第二个参数是一个标志，它指定了读取图像的方式。
        # cv2.IMREAD_COLOR:加载彩色图像，忽视图像透明度。可传递标志位1替代。
        # cv2.IMREAD_GRAYSCALEL:以灰度模式加载图像。可传递标志位0替代。
        # cv2.IMREAD_UNCHANGED:加载图像，包括alpha。可传递标志位-1替代。
        # 加载彩色灰度图像
        img = cv2.imread(self.path)

        img = tf.divide(tf.cast(img, tf.float32), 255.0)
        img = tf.uint8(np.array(img))
        
        # 显示图像:cv2.imshow()
        # 第一个参数为窗口名称，是一个字符串。第二个参数为我们的对象。
        cv2.namedWindow('img', cv2.WINDOW_NORMAL) # 规定窗口大小
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    # 保存图像
    def save_img(self):
        # cv2.imwrite()
        # 第一个参数是文件名，第二个参数是要保存的图像
        img = cv2.imread(self.path, 0)
        cv2.imshow('img', img)
        k = cv2.waitKey(0) & 0xff      # 计算机64位要加0xff
        if k==27:                       # 等待esc退出
            cv2.destroyAllWindows()
        elif k == ord('s'):             # 等待关键字保存和退出
            cv2.imwrite('./data/messigray_class.jpg', img)
            cv2.destroyAllWindows()


    def read_image_matplotlib(self):
        # matplotlib显示图像，为RGB格式
        img = cv2.imread(self.path, 0)
        plt.imshow(img, cmap='gray', interpolation='bicubic')
        plt.xticks([]), plt.yticks([])   # 隐藏x轴和y轴的刻度值
        plt.show()

    # 文件播放视频
    def read_video(self):
        cap = cv2.VideoCapture(self.path)
        if not cap.isOpened():
            print("cannot open camera")
        while(True):
            ret, frame = cap.read()   # 逐帧捕获
            # 如果正确读取帧，ret为True
            if not ret:
                print("can't receive frame (stream end?). Exiting ...")
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 显示结果
            cv2.imshow('gray', gray)
            if cv2.waitKey(1) == ord('q'):
                break
        # 完成后释放捕获器
        cap.release()
        cv2.destroyAllWindows()

    # 保存视频，沿垂直方向
    def save_video(self):
        cap = cv2.VideoCapture(self.path)
        # 定义编码器并创建VideoWriter对象
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
        frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)      
        out = cv2.VideoWriter('./data/output.avi', fourcc, 20.0, ( int(frame_width), int(frame_height)))
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ... ")
                break
            frame = cv2.flip(frame, 0)
            # 写翻转的框架
            out.write(frame)
            cv2.imshow('frame', frame)
            k = cv2.waitKey(1) & 0xff
            if k == ord('q'):
                break
        # 完成工作后释放所有内容
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    

    # 绘图功能
    def draw_picture(self):
        # 创建黑色图像 0是黑色，255是白色
        img = np.zeros((512, 512, 3), np.uint8)
        # 绘制一条厚度为5的蓝色对角线
        cv2.line(img, (0, 0), (512, 512), (255, 0, 0), 5)
        # 画矩形
        cv2.rectangle(img, (384,0), (510,128), (0, 255, 0), 3)
        # 画圆圈
        cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
        # 画椭圆
        cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
        # 画多边形,首先需要顶点的坐标，形状为ROWSx1x2
        pts = np.array([[10,5], [20,30], [70,20], [50, 10]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        # 若第三个参数为False，将获得一条连接所有点的折线，而不是闭合形状。
        # cv2.ploylines()用于绘制多条线，只需将绘制的所有线条的列表传递给函数即可。
        cv2.polylines(img, [pts], True, (0, 255, 255))
        # 向图像中添加文本
        # 需指定文字数据、放置的位置坐标、字体类型、字体比例、常规内容（颜色、厚度、线条类型）
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    










if __name__ == "__main__":
    path_img = './data/img.jpg'
    path_video = './data/cs4.mp4'
    # img_start = ImgGetStart(path_img)   # 只需切换图片路径和视频路径即可
    # img_start.read_image()     # cv2读取图像
    # img_start.save_img()         # cv2保存图像
    # img_start.read_video()        # 视频读取   路径：path_video
    # img_start.save_video()          # 视频保存     路径：path_video
    # img_start.draw_picture()



    
        



