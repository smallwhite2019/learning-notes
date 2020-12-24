# 傅里叶变换
'''
# numpy中的fft变换

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

path = './data/ball.jpg'
img = cv2.imread(path, 0)
# 时域变换
# np.fft.fft2()对信号进行频率转换；
# 直流分量（频率为0）的部分在输出图像的左上角
f = np.fft.fft2(img) 
# 将直流分量在输出图像的中心，np.fft.fftshift()可实现两个方向平移N/2
fshift = np.fft.fftshift(f)

# 构建振幅图
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap= 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# 频域变换
rows, cols = img.shape
print(rows, cols)
crow, ccol = rows//2, cols//2
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
# 逆平移操作
f_ishift = np.fft.ifftshift(fshift)
# FFT逆变换
img_back = np.fft.ifft2(f_ishift)
# 取绝对值
img_back = np.abs(img_back)

plt.subplot(131), plt.imshow(img, cmap= 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_back, cmap= 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()
'''

# opencv中的傅里叶变换

import cv2
import numpy as np
from matplotlib import pyplot as plt

path = './data/ball.jpg'
img = cv2.imread(path, 0)

dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, : , 0], dft_shift[:, :, 1]))

plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap= 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# 逆DFT操作
# LPF（低通滤波）将高频部分去除，就是对图像进行模糊操作
rows, cols = img.shape
crow, ccol = rows//2, cols//2
# 低通滤波
mask = np.zeros((rows, cols,2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# idft
fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

plt.subplot(121), plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap= 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()


# 确定图像最佳大小 cv2.getOptimalDFTSize()
img = cv2.imread(path, 0)
rows, cols = img.shape
print(rows, cols)
nrows = cv2.getOptimalDFTSize(rows)
ncols = cv2.getOptimalDFTSize(cols)
print(nrows, ncols)

# 把数组大小（1050，1680）改变为（1080， 1728），将数据拷贝过去或使用函数cv2.copyMakeBoder()
nimg = np.zeros((nrows, ncols))
nimg[:rows, :cols] = img

# 或者
right = ncols - cols
bottom = nrows - rows

bordertype = cv2.BORDER_CONSTANT
nimg = cv2.copyMakeBoder(img, 0, bottom, 0, right, bordertype, Value = 0)