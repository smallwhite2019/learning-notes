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
返回结果：this is string example....wow!!!
         88888888this is string example....wow!!!
```

# argparse模块：从命令行读取参数
```
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
解析一个.tfrecords文件


