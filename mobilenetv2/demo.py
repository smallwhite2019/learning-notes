
#模块导入
# from keras.applications.imagenet_utils import decode_predictions
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
import os
import pathlib
# from keras.models import load_model
from keras.preprocessing import image
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model, model_from_json
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model
import cv2
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # 禁用GPU
##############################################
# 标签
##############################################
label = ['cabbage', 'pumpkin']


##############################################
#
##############################################
model = load_model('./log/mobilenetv2/20201110_095907/weights_22-0.50000.hdf5')

##############################################
# 读取单张图片
##############################################

# img = cv2.imread('./test_image/11-demo/20200109_170806IMG_20200109_170553.jpg')*
# img = cv2.resize(img, (1120, 1120), interpolation=cv2.INTER_AREA)
img = image.load_img('pitaya_07_0013.jpg', target_size=(1120, 1120))
# plt.imshow(img)
# plt.show()
# 将图片转化为4d tensor形式
x = image.img_to_array(img)
# print(x.shape)  # (224, 224, 3)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
print(x.shape)  # (1, 224, 224, 3)

##############################################
# 预测
##############################################
pres = model.predict(x)
# pres = model.predict_on_batch(x)
max_value = max(pres[0])
i = pres[0].tolist().index(max_value)
name = label[i]
plt.title('本张图片为:%s,准确率为:%.5f' % (name, max_value))
plt.imshow(img)
# print('本张图片为:%s,准确率为:%.5f'%(name,max_value))
plt.show()


