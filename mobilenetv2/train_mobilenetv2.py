
# 模块导入

import os
import pathlib
import tensorflow as tf
from keras.optimizers import Adam
from keras.utils import plot_model
from matplotlib import pyplot as plt
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from keras.preprocessing import image
from keras.models import Model
from keras.callbacks import ModelCheckpoint
from keras.models import load_model, model_from_json
from keras.layers import Dense, GlobalAveragePooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from datetime import datetime
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # 禁用GPU

##############################################
# 图片路径
##############################################
data_path = pathlib.Path('./dataset/')
train_data = data_path / 'train'
val_data = data_path / 'validation'

##############################################
# 获取类别数
##############################################
# 获取数据集目录下，所有子目录的名称。把子目录的名称，作为类别的名称。比如：
# ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
train_labels_name = sorted(
    item.name for item in train_data.glob('*/') if item.is_dir())
# 为每个类别名称，分配一个labels的索引值，一般从0开始，比如：
# {'daisy': 0, 'dandelion': 1, 'roses': 2, 'sunflowers': 3, 'tulips': 4}
train_labels_index = dict(
    (name, index) for index, name in enumerate(train_labels_name))
print(train_labels_index)   

##############################################
# 模型参数配置
##############################################

batch_size = 1   # batch大小
train_image_count = len(list(train_data.glob('*/*')))  # 训练图片数量
val_image_count = len(list(val_data.glob('*/*')))     # 测试图片数量
transfer_learning_epoch = 1  # 预训练epoch
fine_tune_epoch = 40  # 迁移学习训练epoch
input_shape = (1120,1120,3)
CLASSIFY_COUNT = len(train_labels_name)


##############################################
# 模型搭建
##############################################
# 构建不带分类器的预训练模型,权重模型可以放在其他的文件夹中,但是要预先下载好放入
base_model = MobileNetV2(input_shape=input_shape,
                         weights='mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5', include_top=False)
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
# 添加一个分类器，我们有9个类，激活函数为softmax
predictions = Dense(CLASSIFY_COUNT, activation='softmax')(x)
# 构建完整的训练网络模型
model = Model(inputs=base_model.input, outputs=predictions)

##############################################
# 模型搭建,利用以训练好的模型
##############################################
# model = model_from_json(
#     open('model/mobilenetv2/model_architecture_mobilenetv2.json', 'r').read())
# model.load_weights(
#     'model/mobilenetv2/rice_mobilenetv2_weight_fine_tune.h5', by_name=True)





##############################################
# 训练验证数据生成器
##############################################
# 训练数据生成
train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,  # ((x/255)-0.5)*2  归一化到±1之间
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest")

train_generator = train_datagen.flow_from_directory(            # 以文件夹路径为参数,自动生成经过数据提升/归一化后的数据和标签,训练数据路径，train 文件夹下包含每一类的子文件夹
    train_data,
    target_size=input_shape[:2],
    batch_size=batch_size,
    class_mode='categorical')

# 验证数据生成器
val_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
val_generator = val_datagen.flow_from_directory(
    val_data,
    target_size=input_shape[:2],
    batch_size=batch_size,
    class_mode='categorical')


##############################################
# 训练启动，编译模型（一定要在锁层以后操作）
##############################################

# 锁住所有的卷积层，只训练顶部的全连接层
for layer in model.layers:
    layer.trainable = False
# 编译模型
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy', metrics=['accuracy'])
# 在新的数据集上训练
model.fit_generator(
    train_generator,
    steps_per_epoch=train_image_count//batch_size,
    epochs=transfer_learning_epoch,
    validation_data=val_generator,
    validation_steps=val_image_count//batch_size)


# 现在顶层应该训练好了，让我们开始微调 densenet 的卷积层。
# 我们会锁住底下的几层，然后训练其余的顶层。

# 让我们看看每一层的名字和层号，看看我们应该锁多少层呢：
# for i, layer in enumerate(base_model.layers):
#    print(i, layer.name)


# # 我们选择训练最上面的两个 Inception block
# # 也就是说锁住前面249层，然后放开之后的层。
for layer in model.layers[:117]:
    layer.trainable = False
for layer in model.layers[117:]:
    layer.trainable = True


#############################################################################
# 在解开迁移训练中，利用keras中回调函数进行参数保存
#############################################################################
file_path = './log/mobilenetv2/'+datetime.now().strftime('%Y%m%d_%H%M%S')
if not os.path.exists(file_path):
    os.makedirs(file_path)
weights_name = 'weights_{epoch:02d}-{val_acc:.5f}.hdf5'
weights_path = os.path.join(file_path, weights_name)
checkpoint = ModelCheckpoint(weights_path, monitor='val_acc', verbose=1,
                             save_best_only=False, save_weights_only=False, mode='auto', period=1)
callback_list = [checkpoint]



# 重新编译模型
model.compile(optimizer=Adam(lr=0.0001),
              loss='categorical_crossentropy', metrics=['accuracy'])

# 再次训练模型
model.fit_generator(
    train_generator,
    steps_per_epoch=train_image_count//batch_size,
    epochs=fine_tune_epoch,
    validation_data=val_generator,
    validation_steps=val_image_count//batch_size,
    callbacks=[checkpoint])



