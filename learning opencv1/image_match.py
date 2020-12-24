# 模板匹配
'''
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

path = './data/ball.jpg'
img = cv2.imread(path, 0)
img2 = img.copy()
template = cv2.imread('./data/ball_face.jpg', 0)
w, h = template.shape[::-1] # template.shape对应的是高和宽，需要反向转换为宽和高
print(template.shape)
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    # eval语句用来计算存储在字符串中的有效python表达式
    method = eval(meth)
    # cv2.matchTemplate()提供查询模版图像位置方法，cv2.minMaxLoc()来找到其中的最小值和最大值的位置
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # 使用不同的比较方法，对结果的解释不同
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121), plt.imshow(res, cmap= 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap= 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    
    plt.show()

'''

# 多对象的模板匹配
# 你的目标对象在图像中出现了多次情况，函数cv2.imMaxLoc()只会给出最大值和最小值

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

path = './data/mario.jpg'
img_rgb = cv2.imread(path)
img_gray = cv2.imread(path, 0)
template = cv2.imread('./data/mario_coin.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8    # 设置阈值是为了找寻目标框所在的位置

loc = np.where(res >= threshold)   #　找出值所在的坐标位置
for pt in zip(*loc[::-1]):          # *表示可选参数
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow('img_rgb', img_rgb)
cv2.waitKey(0)
# cv2.imwrite('./data/res.jpg', img_rgb)

