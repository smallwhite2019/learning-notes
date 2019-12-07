# re:内容很多，这只是一部分作为了解
```py
import re 
因此我们强烈建议使用Python的'r'前缀，就不用考虑转义的问题了：

s = r'ABC\-001' # Python的字符串

re.match()  #匹配match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None

re.split()  # 切分字符串

如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。

>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
>>> m
<_sre.SRE_Match object; span=(0, 9), match='010-12345'>
>>> m.group(0)  #原始字符串
'010-12345'
>>> m.group(1)  #子串
'010'
>>> m.group(2)
'12345'

```

#  贪婪匹配：正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符

## 编译：re.compile()