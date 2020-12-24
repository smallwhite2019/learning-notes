# 使用GrabCut算法进行交互式前景提取

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

path = './data/ball.jpg'
img = cv2.imread(path)
print(img.shape)
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (50, 50, 1500, 1020)
# 返回值是更新的mask，bgdModel, fgdModel
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
# cv2.imwrite('./data/newmask.jpg', img)
#plt.imshow(img), plt.colorbar(), plt.show()

# 需要的地方使用白色绘制，不需要的地方使用黑色绘制
# 新的掩膜图像
newmask = cv2.imread('./data/newmask.jpg', 0)

mask[newmask == 0] = 0      # 黑色的设置为0
mask[newmask == 255] = 1    # 白色的设置为1

mask, bgdModel, fgdModel = cv2.grabCut(img, mask, None, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')
img = img * mask[:,:,np.newaxis]
plt.imshow(img), plt.colorbar(), plt.show()
