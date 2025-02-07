# python strip与rstrip
Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
```py
str = "00000003210Runoob01230000000"
print(str.strip( '0' ))  # 去除首尾字符 0

str2 = "   Runoob      "  # 去除首尾空格
print (str2.strip())
```
```
返回结果：3210Runoob0123

          Runoob
```
Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）
```py
str = "     this is string example....wow!!!     "
print (str.rstrip())
str = "88888888this is string example....wow!!!8888888"
print (str.rstrip('8'))
```
```
返回结果：
        this is string example....wow!!!
88888888this is string example....wow!!!
```

# argparse模块：从命令行读取参数
```py
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", help = "横坐标", type= int)
parser.add_argument("y", help= "纵坐标", type= int)
args = parser.parse_args()
x = args.x
y = args.y
print(x,y)

python指令：python no.py 3 4
返回结果: 3 4

```

# tf.gfile 类
tf.gfile.GFile(filename, mode)

获取文本操作句柄，类似于python提供的文本操作open()函数，filename是要打开的文件名，mode是以何种方式去读写，将会返回一个文本操作句柄。

tf.gfile.Open()是该接口的同名，可任意使用其中一个！


# tf.placeholder()作用
因为每一个tensor值在graph上都是一个op,每传一次便是op，这样会使得一副graph上的op太多，产生过大的开销；此时利用placeholder()在构建graph时在模型中占位，此时并没有把输入的数据传入模型，它只会分配必要的内存。

# tf.python_io.tf_record_iterator()
解析一个.tfrecords文件，读取record数据
# tf.python_io.TFRecordWriter()
打开文件路径并创建一个TFRecordWriter写入文件。
# Python enumerate() 内置函数
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

语法：enumerate(sequence, [start=0])
```py
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)

运行结果：
0 one
1 two
2 three
```
# Python zip() 函数
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

在python3.x中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。

```py
a = [1,2,3]
b = [4,5,6]
c = zip(a,b)
print(zip(a,b))
print(list(zip(a,b)))
运行结果：
<zip object at 0x00000275DC1CE508>
[(1, 4), (2, 5), (3, 6)]
```

# python tostring()
将array转化为string（or bytes）；再用fromstring()转化为原来的矩阵
```py
import numpy as np
a = np.arange(15).reshape(3,5)
print(a)
b = a.tostring()
print(b)
c = np.fromstring(b,np.int32).reshape(3,5)
print(c)
运行结果：
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

 b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\r\x00\x00\x00\x0e\x00\x00\x00'
 
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
```

# tfrecord
从TFRecords文件中读取数据， 首先需要tf.train.string_input_producer生成一个解析队列。之后调用tf.TFRecordReader的tf.parse_single_example解析器。解析器首先读取解析队列，返回serialized_example对象，之后调用tf.parse_single_example操作将Example协议缓冲区(protocol buffer)解析为张量。
# tf.train.string_input_producer
把输入的数据进行按照要求排序成一个队列。最常见的是把一堆文件名整理成一个队列
# tf.TFRecordReader()
 _, serialized_example = reader.read(filename_queue)   #返回文件名和文件
# tf.parse_single_example
解析队列
# tf.FixedLenFeature 和 tf.VarLenFeature的区别
前者返回的是一个定长的tensor，后者返回的是一个不定长的sparse tensor，用于处理可变长度的输入，在处理ctc问题时，会用到tf.VallenFeature解析存储在tfrecord中的label。
# tf.decode_raw
tf.decode_raw函数的意思是将原来编码为字符串类型的变量重新变回来，这个方法在数据集dataset中很常用，因为制作图片源数据一般写进tfrecord里用to_bytes的形式，也就是字符串。这里将原始数据取出来 必须制定原始数据的格式，原始数据是什么格式这里解析必须是什么格式，要不然会出现形状的不对应问题！
