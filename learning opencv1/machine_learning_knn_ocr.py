# KNN


'''
# 手写数字识别OCR

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('./data/digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 把图片分成5000个，每个20*20大小
# np.hsplit()横向切分，np.vsplit()纵向切分
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]

# 再转换成numpy数组
x = np.array(cells)

# 准备训练数据和测试数据
train = x[:, :50].reshape(-1, 400).astype(np.float32)  # size = (2500, 400)
test = x[:, 50:100].reshape(-1, 400).astype(np.float32)  # size = (2500, 400)

# 为训练数据和测试数据创建标签
k = np.arange(10)
train_labels = np.repeat(k, 250)[:, np.newaxis]    # np.repeat()重复，np.newaxis()为在当前增加一维
test_labels = train_labels.copy()

# 训练knn
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k = 3)

# 最终检查测试精确度，比较结果，检测哪些是错误的，最终输出正确率
matches = result == test_labels
correct = np.count_nonzero(matches)            # np.count_nonzero（）用于统计数组中非零元素的个数
accuracy = correct * 100.0 /result.size
print("accuracy: ", accuracy)


# 保存数据
# 数据格式保存为np.uint8()格式占用空间小，在加载数据时再转回为float32
np.savez('knn_data.npz', train= train, train_labels= train_labels)

# 加载数据
with np.load('knn_data.npz') as data:
    print(data.files)
    train = data['train']
    train_labels = data['train_labels']

'''
# 英文字母
import cv2
import numpy as np
from matplotlib import pyplot as plt 

# 加载数据
data = np.loadtxt('./data/letter-recognition.data', dtype= 'float32', delimiter= ',', converters= {0: lambda ch: ord(ch) - ord('A')})

# 分离训练数据和测试数据
train, test = np.vsplit(data, 2)
# 分离训练数据和测试数据的特征和响应
responses, trainData = np.hsplit(train, [1])    # [1]代表按列划分的索引位置
labels, testData = np.hsplit(test, [1])

# 初始化knn
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
ret, result, neighbours, dist = knn.findNearest(testData, 5)

correct = np.count_nonzero(result == labels)
accuracy = correct * 100.0 / result.size
print(accuracy)


# 可增加训练样本的数量来提高准确率，尤其是判断错误的样本