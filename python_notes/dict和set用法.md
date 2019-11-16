# dict
```py
一是通过in判断key是否存在：
>>>'thomas' in d
False
二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己制定的value：
d.get('thomas')

要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
>>>d.pop('bob)
```
牢记第一条的是dict的key必须是不可变对象

# set
set中没有重复的key
```py
要创建一个set，需要提供一个list作为输入集合：
>>>s = set([1,2,3])
>>>s
{1,2,3}
注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。

重复元素在set()中自动过滤：
>>>s = set([1,2,3,4,3,4])
>>>s
{1,2,3}

通过add()方法添加元素到set中，可以重复添加，但不会有效果：
>>>s.add(4)

删除remove()方法删除元素：
>>>s.remove(4)

set可以做交并集等操作
>>>s1 & s2
>>>s1 | s2
```