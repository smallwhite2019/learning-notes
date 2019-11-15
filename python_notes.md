# 使用list和tuple
## list
```py
list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates = ['Michael', 'Bob', 'Tracy']
classmates.append('Adam')
```
```py
也可以吧元素插入到指定位置，比如索引号为1的位置：
classmates = ['Michael', 'Bob', 'Tracy']
classmates.insert(1, 'Adam')
```
```py
要删除list末尾的元素，用pop()方法；删除指定位置用pop(i)：
classmates = ['Michael', 'Bob', 'Tracy']
classmates.pop()
```
```py
要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = ['Adam']
```
```
list里面的元素数据类型可以不同，list元素也可以是另一个list。
```
## tuple
tuple一旦初始化就不能修改，是指指向不变。
```
python在显示只有一个元素的tuple时，会加一个逗号，，以免你误解成数学计算意义上的括号。
t = (1,)
>>> (1,)
```