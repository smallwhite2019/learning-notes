import cv2
import numpy as np
from matplotlib import pyplot as plt 
import tensorflow as tf 
'''
def mouse_paint(event, x, y, flags, param):
        # events = [i for i in dir(cv2) if 'EVENT' in i]      # 获得鼠标事件和状态
        # print(events)
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
        # 创建一个黑色图像，一个窗口，并绑定到窗口的功能

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_paint)
while(1):
    cv2.imshow('img', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
'''
'''
drawing = False         # 如果按下鼠标为，则为真
mode = True             # 如果为真，绘制矩形。按m键切换到曲线
ix, iy = -1, -1
# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy =x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0,255,0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0,0,255), -1)
    elif event == cv2.EVENT_MOUSEMOVE:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0,255,0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0,0,255), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('img')
cv2.setMouseCallback('img', draw_circle)
while(1):
    cv2.imshow('img', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()


'''

# 创建一个跟踪栏，创建一个显示颜色的窗口

def nothing(x):
    pass

# 创建一个黑色图像，一个窗口
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('img')
# 创建颜色变化的轨迹栏

cv2.createTrackbar('R', 'img', 0, 255, nothing)
cv2.createTrackbar('G', 'img', 0, 255, nothing)
cv2.createTrackbar('B', 'img', 0, 255, nothing)

# 为ON/OFF功能创建开关
switch = '0:OFF\n 1: ON'
cv2.createTrackbar(switch, 'img', 0, 1,nothing)
while(1):
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xff ==27:
        break
    # 得到四条轨迹的当前位置
    # cv2.createTrackbarPos()函数，第一个参数是轨迹栏名称，第二个参数是它附加到的窗口名称，第三个参数是默认值，第四个参数是最大值，
    # 第五个是执行的回调函数每次跟踪栏值更改
    r = cv2.getTrackbarPos('R', 'img')
    g = cv2.getTrackbarPos('G', 'img')
    b = cv2.getTrackbarPos('B', 'img')
    s = cv2.getTrackbarPos(switch, 'img')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv2.destroyAllWindows() 