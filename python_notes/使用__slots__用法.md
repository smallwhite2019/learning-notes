# 使用__slots__：限制实例的属性

正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该<font color=red size =4>实例绑定任何属性和方法</font>，这就是动态语言的灵活性。
```py
>>> class Student(object):
...   pass
...
>>> s = Student()
>>>
>>> s.name = "Bob"
>>> print(s.name)
Bob
>>> def set_age(self, age):
...   self.age = age
...
>>> from types import MethodType    
>>> s.set_age = MethodType(set_age,s)        #实例s绑定方法
>>> s.set_age(25)
>>> s.age
25
>>> def set_score(self,score):   #设定方法
...  self.score = score
...
>>> Student.set_score = set_score   #类Student绑定方法
>>> s.set_score(100)
>>> s.score
100

>>> s2 = Student()    #类绑定方法使得所有实例均可调用
>>> s2.set_score(10)
>>> s2.score
10

```
上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。<font color=red >只是为了说动态这件事</font>

## 使用__slots__:

Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
```py
>>> class Student(object):
...   __slots__ = ('name', 'age')  #使用tuple定义允许绑定的属性名称
...
>>> s = Student()
>>> s.name = 'M'
>>> s.age = 10
>>> s.score = 99  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'

由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

>>> class GraduateStudent(Student):
...   pass
...
>>> g = GraduateStudent()
>>> g.score = 99  
```

除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。