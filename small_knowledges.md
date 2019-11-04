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