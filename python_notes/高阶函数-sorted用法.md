# sorted 排序算法
Python内置的sorted()函数就可以对list进行排序：
```py
>>> sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
```
此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
```py
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
```
key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
我们给sorted传入key函数，即可实现忽略大小写的排序：
```py
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
['about', 'bob', 'Credit', 'Zoo']

要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：

>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
```
用sorted()排序的关键在于实现一个映射函数